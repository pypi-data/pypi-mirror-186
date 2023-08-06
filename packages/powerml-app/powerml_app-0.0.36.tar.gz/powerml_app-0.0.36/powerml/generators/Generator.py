from datetime import datetime
from powerml import PowerML
from powerml.utils.run_ai import batch_query_openai
from powerml.utils.generator import get_types
from powerml.utils.constants import PARALLEL_REQUEST_LIMIT
from powerml.utils.metrics import GeneratorMetrics
from random import sample
from math import ceil


class Generator():
    '''
    This is a general class that can be used to generate examples that are not already covered by data.
    '''

    def __init__(self, gold_types=['Llama'], model='text-davinci-003', max_output_tokens=256):
        self.model = model
        self.max_output_tokens = max_output_tokens
        assert len(gold_types) >= 1, 'Please provide at least 1 gold type.'
        self.gold_types = gold_types

    def __add_prompt(self, data):
        reformatted_data = []
        for datum in data:
            if type(datum) == dict:
                reformatted_data.append(
                    {'prompt': f"Prompt: {datum['prompt']}\n", 'completion': f"Completion: {datum['completion']}"})
            else:  # if type(datum) == str
                reformatted_data.append(
                    {'prompt': 'Prompt:\n', 'completion': f"Completion: {datum}"})
        return reformatted_data

    # NOTE: could add reference data for this
    def __fuzzy_modify(self, data, prompt, completion_only):
        modified_examples = []
        for i in range(0, len(data), PARALLEL_REQUEST_LIMIT):
            curr_data = data[i:i+PARALLEL_REQUEST_LIMIT]
            prompt_append = f'\n\nModify this example to {prompt}.\n\n\"Prompt:'
            if completion_only:
                prompt_append += '\nCompletion:'
            prompts = [
                f"\"{datum['prompt']}{datum['completion']}\"{prompt_append}" for datum in self.__add_prompt(curr_data)]
            generations = batch_query_openai(prompts,
                                             stop='',
                                             model=self.model,
                                             max_tokens=self.max_output_tokens,
                                             temperature=0.5,
                                             )
            if type(generations) != list:
                generations = [generations]
            if completion_only:
                generations = [f"{curr_data[i]['prompt']}\nCompletion: {generation.strip()}" for i,
                               generation in enumerate(generations)]
            generations = [generation.strip()[:-1] if generation.strip()[-1]
                           == '\"' else generation.strip() for generation in generations]
            modified_examples.extend(generations)
        return modified_examples

    def __generate_modified(self, data, modifier, num_generate, completion_only=False):
        print('Start Generating Modified Data:', datetime.now())
        generated_data = self.__fuzzy_modify(
            sample(data, num_generate), modifier, completion_only)
        print('End Generating Modified Data:', datetime.now())
        return generated_data

    def _compute_coverage(self, generated_types):
        generated_types = set(generated_types)
        gold_types = set(self.gold_types)
        num_matched_items = len(gold_types.intersection(generated_types))
        num_real_items = len(gold_types)
        coverage = num_matched_items / num_real_items
        rare_types = gold_types.difference(generated_types)
        return {
            'Coverage': coverage,
            'Rare Types': rare_types,
        }

    def _merge_metrics(self, old_metrics, new_metrics):
        return {
            'Old Coverage': old_metrics['Coverage'],
            'New Coverage': new_metrics['Coverage'],
            'Rare Types': old_metrics['Rare Types'],
        }

    def _reformat_data(self, data):
        return data

    def _reformat_generated_data(self, generated_data):
        reformatted_generated_data = []
        prepend = 'Completion: '
        for datum in generated_data:
            if prepend in datum:
                datum = datum.split(prepend)[1]
            reformatted_generated_data.append(datum)
        return reformatted_generated_data

    def _fit_and_predict(self, model, data, reformatted_data):
        model.fit(data)
        model_predictions = []
        for datum in reformatted_data:
            model_predictions.append(model.predict(datum['prompt']))
        generated_types = get_types(model_predictions, self.gold_types)
        return generated_types

    def _get_modifier(self, rare_type):
        return f'include \'{rare_type}\''

    def get_rare(self, data, return_metrics=True, model=PowerML(), completion_only=False):
        """
        Parameters
        ----------
        data: list[]
            List of data examples
        return_metrics: bool
            If True, return metrics
        model: PowerML
            Model that will be used to get rare types in the data
        completion_only:
            If True, generate only completion for each example, rather than prompt and completion

        Returns
        generated_data : The generated list of data examples
        metrics (optional): Metrics on data coverage before and after generating examples
        -------
        """
        reformatted_data = self._reformat_data(data)
        old_generated_types = self._fit_and_predict(
            model, data, reformatted_data)
        old_metrics = self.__compute_coverage(old_generated_types)
        coverage = old_metrics['Coverage']
        rare_types = old_metrics['Rare Types']
        generated_data = []
        if rare_types:
            # generate at least 1 example per rare_type, proportional to the amount of coverage of the data
            num_generate = ceil(
                (1 - coverage) * len(reformatted_data) / len(rare_types))
            print(f'Number of Generations per Rare Type: {num_generate}')
            for rare_type in rare_types:
                modifier = self._get_modifier(rare_type)
                generated_data.extend(self.__generate_modified(
                    reformatted_data, modifier, num_generate, completion_only))
        generated_data = self._reformat_generated_data(generated_data)
        if return_metrics:
            reformatted_generated_data = self._reformat_data(generated_data)
            new_generated_types = self._fit_and_predict(
                model, data + generated_data, reformatted_data + reformatted_generated_data)
            new_metrics = self.__compute_coverage(new_generated_types)
            return generated_data, GeneratorMetrics(self.__merge_metrics(old_metrics, new_metrics))
        return generated_data
