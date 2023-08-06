import io
import requests
import jsonlines
from powerml.utils.run_ai import query_powerml, powerml_train
from powerml.utils.config import get_config
import logging

logger = logging.getLogger(__name__)

MAX_TEMPLATE_TOKENS = 3072
MAX_TOTAL_TOKENS = 4097


class PowerML:
    '''
    hex_data = get_data()
    powerml = PowerML()
    completion = powerml.predict(model="hex/model_for_hex", prompt)
    powerml.fit(hex_data, model="hex/model_for_hex")
    '''

    def __init__(self, config={}):
        self.config = get_config(config)
        self.current_model = "text-davinci-003"

    def predict(self,
                prompt,
                model: str = None,
                stop: str = "",
                max_tokens: int = 128,
                temperature: int = 0,
                ) -> str:
        if model == "" or model is None:
            model = self.current_model
        logger.debug("Predict using model: " + model)
        # if the model is one of our models, then hit our api
        return query_powerml(prompt,
                             max_tokens=max_tokens,
                             model=model,
                             stop=stop,
                             temperature=temperature,
                             key=self.config["powerml.key"],
                             )

    def fit(self,
            data: list[str],
            model: str = None):
        if model == "" or model is None:
            model = self.current_model
        logger.debug("Fit using model: " + model)
        params = {
            "dataset": self.__make_dataset_string(data),
            "model": model
        }
        response = powerml_train(params, self.config["powerml.key"])
        model_details = response.json()['model']
        self.current_model = model_details["model_name"]
        return model_details

    def __make_dataset_string(self, training_data):
        string = io.StringIO()
        with jsonlines.Writer(string) as writer:
            for item in training_data:
                writer.write({"prompt": item})
        return string.getvalue()
