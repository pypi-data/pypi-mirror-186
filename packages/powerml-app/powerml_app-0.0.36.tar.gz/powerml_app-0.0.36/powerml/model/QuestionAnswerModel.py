
from powerml import PowerML
import logging

logger = logging.getLogger(__name__)


class QuestionAnswerModel:
    def __init__(self,
                 config={},
                 max_output_tokens=256,
                 ):
        self.model = PowerML(config)
        self.model_name = "quizlet/questions"
        self.max_output_tokens = max_output_tokens

    def fit(self,
            lesson: str,
            answer: str,
            examples: list[str]):
        """
        Parameters
        ----------
        lesson : str
            The broader context where the question is being asked
        answer : str
            The correct answer for the questions
        examples : list[str]
            A list of questions which correspond to the answer
        """
        self.lesson = lesson
        self.question_count = str(len(examples) + 1)
        self.answer = answer
        self.examples = examples

    def predict(self):
        """
        Returns
        -------
        str : A question for which the answer is the answer the model if fitted to.
        """
        examples_string = "\n".join(
            [f'{i + 1}. ' + example for i, example in enumerate(self.examples)])
        prompt = {
            "{{lesson}}": self.lesson,
            "{{question_count}}": self.question_count,
            "{{answer}}": self.answer,
            "{{examples}}": examples_string,
        }
        output = self.model.predict(
            prompt, max_tokens=self.max_output_tokens, temperature=0.7, model=self.model_name)
        return self.__post_process(output)

    def __post_process(self, output):
        return output.strip()
