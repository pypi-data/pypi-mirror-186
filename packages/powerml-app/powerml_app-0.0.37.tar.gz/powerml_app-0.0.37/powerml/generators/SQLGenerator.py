from powerml import Generator
from powerml import AutocompleteSQLModel
from powerml.utils.generator import create_schema, tables_to_schema

class SQLGenerator(Generator):
    '''
    This is a class that can be used to generate more queries for AutocompleteSQLModels.
    '''

    def __init__(self, schema):
        super().__init__(schema, 'code-davinci-002', max_output_tokens=1250)

    def _fit_and_predict(self, model, queries, reformatted_queries):
        model.fit(tables_to_schema(self.gold_types), queries)
        model_predictions = []
        for query in reformatted_queries:
            query = query.split()[0]
            model_predictions.append(query + ' ' + model.predict(query))
        generated_schema = create_schema(model_predictions)
        return generated_schema

    def get_rare(self, queries, return_metrics=True):
        """
        Parameters
        ----------
        queries: list[str]
            List of queries
        return_metrics: bool
            If True, return metrics

        Returns
        generated_data : The generated list of queries
        metrics (optional): Metrics on data coverage before and after generating queries
        -------
        """
        return super().get_rare(queries, return_metrics, AutocompleteSQLModel())