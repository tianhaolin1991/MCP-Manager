from cons.log import LOGGER
from process.evaluator import Evaluator
from process.models import LLMCallRecord
from cons.constants import *

from mcp_program import MCPPredict


SYSTEM_PROMPT = """# Role
You are a helpful assistant. You are able to answer questions using different tools.  
"""


class CodingPredict(MCPPredict):
    def __init__(self, max_steps=20, prompt_template=(REACT_PROMPT + SYSTEM_PROMPT).strip(), task_name="gaia"):
        super().__init__(max_steps, prompt_template, task_name)

    def evaluate_prediction(self, question: str, ground_truth: str, prediction: str, record: LLMCallRecord):
        return Evaluator.question_scorer(self.eval_llm, question, prediction, ground_truth, record, LOGGER)

    def extract_last_answer(self, text):
        matches = ANSWER_PATTERN.findall(text)

        if matches:
            return matches[-1]
        else:
            return text
