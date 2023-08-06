from datetime import datetime
from powerml.utils.run_ai import batch_query_openai
from powerml.utils.constants import PARALLEL_REQUEST_LIMIT
from powerml.utils.metrics import FilterMetrics
from collections import defaultdict


class Filter():
    '''
    This is a general class that can be used to filter noise from data.
    '''

    # NOTE: Would like to add a general filter for near duplicates using Greg's Presto method
    general_filters = {}

    def __init__(self, prompt, model='text-davinci-003'):
        self.prompt = prompt
        self.model = model
        self.filters = {**self.general_filters,
                        'Duplicate': self.__filter_duplicate,
                        'Invalid': self.__filter_invalid,
        }

    def __add_prompt(self, data):
        reformatted_data = []
        for datum in data:
            if type(datum) == dict:
                reformatted_data.append(
                    {'prompt': f"{datum['prompt']}\n", 'completion': datum['completion']})
            else:  # if type(datum) == str
                reformatted_data.append({'prompt': '', 'completion': datum})
        return reformatted_data

    def __fuzzy_is_valid(self, data):  # NOTE: could add reference data for this
        valid_examples = []
        for i in range(0, len(data), PARALLEL_REQUEST_LIMIT):
            curr_data = data[i:i+PARALLEL_REQUEST_LIMIT]
            prompt_prepend = f'Is this a valid {self.prompt}:\n\n'
            prompt_append = '\n\nAnswer Yes if it is valid and No if it is not valid, and explain why or why not.'
            prompts = [
                f"{prompt_prepend}{datum['prompt']}\"{datum['completion']}\"{prompt_append}" for datum in self.__add_prompt(curr_data)]
            is_valid = batch_query_openai(prompts,
                                          stop='\nEND',
                                          model=self.model,
                                          max_tokens=6,
                                          temperature=0.0,
                                          )
            if type(is_valid) != list:
                is_valid = [is_valid]
            is_valid = [False if 'no' in output.strip(
            ).lower() else True for output in is_valid]
            valid_examples.extend(
                [datum for j, datum in enumerate(curr_data) if is_valid[j]])
        return valid_examples

    def __filter_duplicate(self, data):
        filtered_data = []
        for datum in data:
            if datum not in filtered_data:
                filtered_data.append(datum)
        return filtered_data

    def __filter_invalid(self, data):
        print('Start Filtering Invalid Data:', datetime.now())
        filtered_data = self.__fuzzy_is_valid(data)
        print('End Filtering Invalid Data:', datetime.now())
        return filtered_data

    def _reformat_data(self, data):
        return data

    def _reformat_filtered_data(self, filtered_data):
        return filtered_data

    def get_passing(self, data, return_metrics=True):
        """
        Parameters
        ----------
        data: list[]
            List of data examples
        return_metrics: bool
            If True, return metrics

        Returns
        filtered_data : The filtered list of data examples
        metrics (optional): Metrics on how many examples pass or fail the filters
        -------
        """
        data = self._reformat_data(data)
        metrics = defaultdict(dict)
        len_data = len(data)
        filtered_data_intersect = data
        for filter in self.filters:
            filtered_data = self.filters[filter](data)
            metrics[f'{filter} Filter']['Pass'] = len(filtered_data)
            metrics[f'{filter} Filter']['Fail'] = len_data - len(filtered_data)
            filtered_data_intersect = [
                datum for datum in filtered_data_intersect if datum in filtered_data]
        metrics['All Filters']['Pass'] = len(filtered_data_intersect)
        metrics['All Filters']['Fail'] = len_data - \
            len(filtered_data_intersect)
        filtered_data_intersect = self._reformat_filtered_data(
            filtered_data_intersect)
        if return_metrics:
            return filtered_data_intersect, FilterMetrics(metrics)
        return filtered_data_intersect
