from powerml import MenuGenerator
from powerml import ExtractMenuItemsModel
from powerml.utils.run_ai import query_powerml
from powerml.utils.generator import load_menu_from_files
from powerml.utils.metrics import GeneratorMetrics
from powerml.utils.constants import TOP_ITEM_COUNT, MAX_STRING_LENGTH, MAX_INPUT_CHARS, MAX_NEW_TOKENS, GENERATOR_MODEL, MAX_GEN_STYLES
from collections import Counter
from tqdm import tqdm
import random

import logging

logger = logging.getLogger(__name__)


class PrestoGenerator(MenuGenerator):
    '''
    This is a class that can be used to generate more Presto data for ExtractMenuItemsModels.
    '''

    def __init__(self, menu=None, top_item_count=TOP_ITEM_COUNT, max_gen_styles=MAX_GEN_STYLES):
        self.top_item_count = top_item_count
        self.max_gen_styles = max_gen_styles
        super().__init__(menu)

    def __get_top_menu_items(self, data):
        histogram = Counter()

        for conversation in data:
            items = self._order_to_items(conversation["completion"])

            histogram.update(items)

        sorted_menu_items = sorted(
            [(count, item) for item, count in histogram.items()], reverse=True)

        sorted_menu_items = sorted_menu_items[:self.top_item_count]

        return [item for _, item in sorted_menu_items]

    def __make_prompt(self, data, style, seed):
        data_copy = list(data)

        random.seed(seed)
        random.shuffle(data_copy)

        prompt = ""

        for item in data_copy:
            new_prompt = "\n\n-- This is a conversation where a customer orders the following items:\n"

            new_prompt += item["completion"]

            new_prompt += "\n\nConversation:\n"
            new_prompt += item["prompt"]

            if len(prompt) + len(new_prompt) > MAX_INPUT_CHARS:
                break

            prompt += new_prompt

        prompt += "\n\n-- " + style + "\n"
        prompt += "1x {{input}}"
        prompt += "\n\nConversation:"

        return prompt

    def __trim_end(self, string):
        if len(string) > MAX_STRING_LENGTH:
            return string[-MAX_STRING_LENGTH:]

        return string

    def __postprocess(self, string):
        location = string.find("--")

        if location > 0:
            return string[:location].strip()

        return string

    def __trim_begin(self, string):
        if len(string) > MAX_STRING_LENGTH:
            return string[:MAX_STRING_LENGTH]

        return string

    def __generate_conversations_for_item(self, item_name, data, index):
        styles = [
            "This is a conversation where the customer orders the following items:",
            "This is a conversation where the customer asks about a different menu item before finally ordering the following items:",
            "This is a conversation where the customer orders another item by mistake before finally ordering the following items:",
            "This is a conversation where the customer talks about the weather before finally ordering the following items:",
            "This is a conversation where the customer says something mean to the AI before finally ordering the following items:",
            "This is a conversation where the customer tries to confuse the AI before finally ordering the following items:",
            "This is a conversation where the customer changes their mind about the size before finally ordering the following items:",
            "This is a conversation where the customer is talking too softly before finally ordering the following items:",
            "This is a conversation where the ai asks the customer to repeat their order three times before finally ordering the following items:",
            "This is a conversation where the customer misspells every other word in their order before finally ordering the following items:",
            "This is a conversation where the customer says something sarcastic before finally ordering the following items:",
            "This is a conversation where the customer asks about a coupon before finally ordering the following items:",
            "This is a conversation where the customer tries to order an item that is not available before finally ordering the following items:",
            "This is a conversation where the customer asks to talk to a live person before finally ordering the following items from the AI:",
            "This is a conversation where the customer says that the AI sounds like a robot like Siri before finally ordering the following items:",
            "This is a conversation where the customer asks why they have to talk to a robot 2 times before finally ordering the following items:",
            "This is a conversation where the customer asks about a payment method like Apple pay or credit card before finally ordering the following items:",
            "This is a conversation where the customer says something mean before finally ordering the following items:",
            "This is a conversation where the customer asks for the price of the items before finally ordering the following items:",
            "This is a conversation where the customer makes a joke about the AI before finally ordering the following items:",
            "This is a conversation where the customer tries to make the AI laugh before finally ordering the following items:",
            "This is a conversation where the customer asks for a discount before finally ordering the following items:",
            "This is a conversation where the customer talks about the weather again before finally ordering the following items:",
            "This is a conversation where the customer asks for a different type of cheese before finally ordering the following items:",
            "This is a conversation where the customer explains why they need the items before finally ordering the following items:",
            "This is a conversation where the customer asks for a substitution before finally ordering the following items:",
            "This is a conversation where the customer asks for more information about an item before finally ordering the following items:",
            "This is a conversation where the customer asks for the ingredients of a dish before finally ordering the following items:",
            "This is a conversation where the customer asks for a different size before finally ordering the following items:",
            "This is a conversation where the customer tries to haggle before finally ordering the following items:",
            "This is a conversation where the customer talks about what they had last time before finally ordering the following items:",
            "This is a conversation where the customer compliments the AI before finally ordering the following items:",
            "This is a conversation where the customer talks about their favorite dish before finally ordering the following items:",
            "This is a conversation where the customer talks about the taste of the food before finally ordering the following items:",
            "This is a conversation where the customer requests a special request before finally ordering the following items:",
            "This is a conversation where the customer asks if they can add something to their order before finally ordering the following items:",
            "This is a conversation where the customer asks for a recommendation before finally ordering the following items:",
            "This is a conversation where the customer requests a special sauce before finally ordering the following items:",
            "This is a conversation where the customer asks for a substitution for a side dish before finally ordering the following items:",
            "This is a conversation where the customer asks for the nutritional information before finally ordering the following items:",
            "This is a conversation where the customer asks for a discount code before finally ordering the following items:",
            "This is a conversation where the customer talks about the size of the portions before finally ordering the following items:",
            "This is a conversation where the customer talks about the freshness of the ingredients before finally ordering the following items:",
            "This is a conversation where the customer asks for a different type of bread before finally ordering the following items:",
            "This is a conversation where the customer asks if the food is gluten-free before finally ordering the following items:",
            "This is a conversation where the customer asks if the food is vegan before finally ordering the following items:",
            "This is a conversation where the customer asks if the food is organic before finally ordering the following items:"
        ]

        generations = []

        for style_index, style in enumerate(styles):

            prompt = self.__make_prompt(
                data, style, index * len(styles) + style_index)

            prompt = prompt.replace("{{input}}", item_name)

            logger.debug(
                "Running with prompt: ----------------------------------------- \n" + self.__trim_end(prompt))

            conversation = query_powerml(
                prompt=prompt, model=GENERATOR_MODEL, max_tokens=MAX_NEW_TOKENS)

            conversation = self.__postprocess(conversation)

            logger.debug("Got completion: ============================================== \n" +
                         self.__trim_begin(conversation))

            generations.append(
                {"prompt": conversation, "completion": "1x " + item_name})

            if style_index + 1 >= self.max_gen_styles:
                break

        return generations

    def __generate_conversations_for_items(self, top_menu_items, data):
        conversations = []
        for index, item in enumerate(tqdm(top_menu_items)):
            for conversation in tqdm(self.__generate_conversations_for_item(item, data, index)):
                conversations.append(conversation)
        return conversations

    def _reformat_generated_data(self, data):
        reformatted_data = []
        for datum in data:
            reformatted_data.append(
                {'conversation': datum['prompt'], 'order': datum['completion']})
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
        model = ExtractMenuItemsModel()
        reformatted_data = self._reformat_data(data)
        old_generated_types = self._fit_and_predict(
            model, data, reformatted_data)
        old_metrics = self._compute_coverage(old_generated_types)
        rare_types = old_metrics['Rare Types']
        reformatted_generated_data = []
        if rare_types:
            top_menu_items = self.__get_top_menu_items(reformatted_data)
            reformatted_generated_data = self.__generate_conversations_for_items(
                top_menu_items, reformatted_data)
        generated_data = self._reformat_generated_data(
            reformatted_generated_data)
        new_generated_types = self._fit_and_predict(
            model, data + generated_data, reformatted_data + reformatted_generated_data)
        new_metrics = self._compute_coverage(new_generated_types)
        if return_metrics:
            return generated_data, GeneratorMetrics(self._merge_metrics(old_metrics, new_metrics))
        return generated_data
