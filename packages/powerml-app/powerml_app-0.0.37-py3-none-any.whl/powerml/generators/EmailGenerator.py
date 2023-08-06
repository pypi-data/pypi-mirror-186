from powerml import Generator
from powerml import WriteEmailModel

class EmailGenerator(Generator):
    '''
    This is a class that can be used to generate more data for WriteEmailModels.
    '''

    def __init__(self, gold_types=['Announcement']):
        super().__init__(gold_types)

    def _reformat_data(self, data):
        reformatted_data = []
        for datum in data:
            reformatted_data.append({'prompt': datum['subject'], 'completion': datum['email']})
        return reformatted_data
    
    def _reformat_generated_data(self, data):
        reformatted_data = []
        for datum in data:
            prompt, completion = datum.split('\nCompletion: ')
            reformatted_data.append({'subject': prompt, 'email': completion})
        return reformatted_data

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
        return super().get_rare(data, return_metrics, WriteEmailModel())