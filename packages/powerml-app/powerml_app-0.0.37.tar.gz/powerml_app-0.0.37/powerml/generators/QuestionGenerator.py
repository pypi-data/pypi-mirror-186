from powerml import Generator
from powerml import QuestionAnswerModel
from powerml.utils.generator import get_types
from collections import defaultdict

class QuestionGenerator(Generator):
    '''
    This is a class that can be used to generate more data for QuestionAnswerModels.
    '''

    def __init__(self, gold_types=['True-or-False']):
        super().__init__(gold_types, max_output_tokens=1000)

    def _reformat_data(self, data):
        reformatted_data = []
        for datum in data:
            for question in datum['questions']:
                reformatted_data.append({'prompt': f"Lesson: {datum['lesson']}\nAnswer: {datum['answer']}", 'completion': question})
        return reformatted_data
    
    def _reformat_generated_data(self, data):
        reformatted_data_dict = defaultdict(list)
        for datum in data:
            prompt, completion = datum.split('\nCompletion: ')
            reformatted_data_dict[prompt].append(completion)
        reformatted_data = [
            {
                'lesson': prompt.split('\nAnswer: ')[0].split('Lesson: ')[1],
                'answer': prompt.split('\nAnswer: ')[1],
                'questions': completion
            }
            for prompt, completion in reformatted_data_dict.items()
        ]
        return reformatted_data

    def _fit_and_predict(self, model, data, _):
        model_predictions = []
        for datum in data:
            model.fit(datum['lesson'], datum['answer'], datum['questions'])
            model_predictions.append(model.predict())
        generated_types = get_types(model_predictions, self.gold_types)
        return generated_types

    def get_rare(self, data, return_metrics=True):
        """
        Parameters
        ----------
        data: list[dict]
            List of data examples
        return_metrics: bool
            If True, return metrics

        Returns
        generated_data : The generated list of data examples
        metrics (optional): Metrics on data coverage before and after generating data examples
        -------
        """
        return super().get_rare(data, return_metrics, QuestionAnswerModel(), completion_only=True)