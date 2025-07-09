from cons.log import LOGGER
from process.evaluator import Evaluator
from process.models import LLMCallRecord
from cons.constants import *


from mcp_program import MCPPredict


class MathPredict(MCPPredict):
    def __init__(self, max_steps=5, prompt_template=REACT_PROMPT.strip(), task_name="math"):
        super().__init__(max_steps, prompt_template, task_name)

    def evaluate_prediction(self, question: str, ground_truth: str, prediction: str, record: LLMCallRecord):
        return Evaluator.question_scorer(self.eval_llm, question, prediction, ground_truth, record, LOGGER)

    def extract_last_answer(self, text):
        matches = ANSWER_PATTERN.findall(text)

        if matches and matches[-1]!='':
            return matches[-1]
        else:
            return text