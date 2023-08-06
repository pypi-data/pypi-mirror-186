from powerml import Generator
from powerml import ForecastSequenceModel
from powerml.utils.generator import get_types


class ForecastGenerator(Generator):
    '''
    This is a class that can be used to generate more data for ForecastSequenceModels.
    '''

    def __init__(self, gold_types=['monotonically increasing']):
        super().__init__(gold_types)
    
    def _reformat_data(self, data):
        reformatted_data = []
        for datum in data:
            revenue = ", ".join([str(forecast) for forecast in datum['revenue']])
            reformatted_data.append({'prompt': f"Release Date: {datum['release_date']}\nTitle: {datum['title']}", 'completion': revenue})
        return reformatted_data
    
    def _reformat_generated_data(self, data):
        reformatted_data = []
        for datum in data:
            prompt, completion = datum.split('\nCompletion: ')
            release_date, title = prompt.split('\n')
            revenue = [int(forecast) for forecast in completion.split(', ')]
            reformatted_data.append({'release_date': release_date.split('Release Date: ')[1], 'title': title.split('Title: ')[1], 'revenue': revenue})
        return reformatted_data

    def _fit_and_predict(self, model, data, _):
        model.fit(data)
        titles = [datum['title'] for datum in data]
        model_predictions = []
        for title in titles:
            model_predictions.append(model.predict(title))
        generated_types = get_types(model_predictions, self.gold_types)
        return generated_types

    def _get_modifier(self, rare_type):
        return f'be {rare_type}'

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
        return super().get_rare(data, return_metrics, ForecastSequenceModel())
