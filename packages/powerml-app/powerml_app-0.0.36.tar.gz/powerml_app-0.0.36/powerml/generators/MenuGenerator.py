from powerml import Generator
from powerml import ExtractMenuItemsModel
from powerml.utils.generator import load_menu_from_files
import re

class MenuGenerator(Generator):
    '''
    This is a class that can be used to generate more data for ExtractMenuItemsModels.
    '''

    def __init__(self, menu=None):
        self.menu = menu
        if not self.menu:
            self.menu = load_menu_from_files()
        super().__init__(list(self.menu.values()))

    def __strip_count(self, name_and_count):
        match = re.search(r"^\d+x", name_and_count)

        if match is None:
            return name_and_count

        return name_and_count[match.end(0):].strip()
    
    def __convert_item(self, item):
        item = self.__strip_count(item)
        return self.menu[item] if item in self.menu else item

    def _order_to_items(self, order):
        items = [self.__convert_item(item.lstrip()) for item in order.split('\n')]
        return items
    
    def _reformat_data(self, data):
        reformatted_data = []
        for datum in data:
            reformatted_data.append({'prompt': datum['conversation'], 'completion': datum['order']})
        return reformatted_data
    
    def _reformat_generated_data(self, data):
        reformatted_data = []
        for datum in data:
            prompt, completion = datum.split('\nCompletion: ')
            completion = completion.replace(' and ', '\n').replace('.', '')
            reformatted_data.append({'conversation': prompt, 'order': completion})
        return reformatted_data

    def _fit_and_predict(self, model, data, reformatted_data):
        model.fit(data)
        generated_items = set()
        for datum in reformatted_data:
            generated_items.update(self._order_to_items(model.predict(datum['prompt'])))
        return generated_items

    def _get_modifier(self, item):
        return f'include 1x \'{item}\''

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
        return super().get_rare(data, return_metrics, ExtractMenuItemsModel())