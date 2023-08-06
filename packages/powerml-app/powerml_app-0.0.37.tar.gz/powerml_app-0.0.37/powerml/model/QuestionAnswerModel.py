
from powerml import PowerML
import re
import logging

logger = logging.getLogger(__name__)


class QuestionAnswerModel:
    def __init__(self,
                 config={},
                 max_output_tokens=256,
                 ):
        self.model = PowerML(config)
        self.model_name = "quizlet/questions/v3"
        self.max_output_tokens = max_output_tokens

    def fit(self,
            examples: list[dict]):
        """
        Parameters
        ----------
        examples : list[dict]
            Takes a list of dictionaries where each dictionary has a key
            "note" with a piece of study material and a key
            "questions" with a list of dictionaries where each dictionary has a key
            "Q" with a question for students of "note" and a key
            "A" with a corresponding answer for the question.
        """
        self.examples = examples

    def predict(self, note, num_questions=1):
        """
        Parameters
        ----------
        note : str
            The study material from which to extract question-answer pairs
        num_questions : int
            The number of question-answer pairs to generate for the given note

        Returns
        -------
        list[dict] : A list of {num_questions} dictionaries where each dictionary has a key
        "Q" with a question for students of "note" and a key
        "A" with a corresponding answer for the question.
        """
        examples_string = ''
        if hasattr(self, 'examples'):
            for example in self.examples:
                examples_string += f"{example['note']}\n\n"
                examples_string += f"Generate {len(example['questions'])} question-answer pairs with the question after 'Q:' and the answer after 'A:':\n\n"
                examples_string += "\n\n".join(
            [f"{i + 1}. Q: {question['Q']}\nA: {question['A']}" for i, question in enumerate(example['questions'])])
                examples_string += '\n\n'
        prompt = {
            "{{note}}": note,
            "{{num_questions}}": str(num_questions),
            "{{examples}}": examples_string,
        }
        output = self.model.predict(
            prompt, max_tokens=self.max_output_tokens, temperature=0.7, model=self.model_name)
        return self.__post_process(output)

    def __post_process(self, output):
        tags = {'Answer:': 'Question:', 'A:': 'Q:'}
        list_pattern = r"\d+\."
        items = re.split(list_pattern, output)
        parsed = []
        for question_answer in items:
            for tag in tags:
                if tag in question_answer:
                    question, answer = question_answer.split(tag)
                    extra = tags[tag]
                    if question.strip().startswith(extra):
                        question = question.partition(extra)[2]
                    parsed.append({'Q': question.strip(), 'A': answer.strip()})
                    break
        return parsed
