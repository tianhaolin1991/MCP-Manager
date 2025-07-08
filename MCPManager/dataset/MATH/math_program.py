import time
from typing import Tuple, Optional
from utils.evaluation_utils import question_scorer
from cons.constants import REACT_PROMPT, ANSWER_PATTERN
import dspy

from mcp_program import MCPPredict
from process.llm import (
    call_lm,
    build_init_messages,
    build_messages,
    response_parsing,
    mcp_calling,
    LLMCallRecord
)


class MathPredict(MCPPredict):
    def __init__(self, max_steps=5, system_prompt=REACT_PROMPT.strip(), task_name="math"):
        super().__init__(max_steps, system_prompt, task_name)

    def evaluate_prediction(self, question: str, ground_truth: str, prediction: str, record: LLMCallRecord) -> Tuple[bool, Optional[str]]:
        return question_scorer(question, prediction, ground_truth, manager, self.run_logger)

    def extract_last_answer(self, text):
        matches = ANSWER_PATTERN.findall(text)

        if matches and matches[-1]!='':
            return matches[-1]
        else:
            return text

    def forward(self, **kwargs) -> dspy.Prediction:
        unique_id = kwargs.get('id')
        question = kwargs.get('question')
        gt = kwargs.get('answer')

        manager = LLMCallRecord()
        manager.lm_api_key = self.lm.api_key
        manager.lm_api_base = self.lm.api_base
        manager.model = self.lm.model
        manager.id = unique_id

        self.run_logger.info(f"ID: {record.id}, Starting forward pass for question: {question}")

        mcps = self.mcp_config['mcp_pool']

        messages = build_init_messages(self.system_prompt, mcps, question)
        steps = 0
        all_completion_tokens = 0
        all_prompt_tokens = 0
        start_time = time.time()

        while not messages[-1][ROLE] == Role.ASSISTANT and steps < self.max_steps:
            response, completion_tokens, prompt_tokens = call_lm(messages, manager, self.run_logger)
            all_completion_tokens += completion_tokens
            all_prompt_tokens += prompt_tokens
            mcp_calls = response_parsing(response)

            new_messages = mcp_calling(mcp_calls, manager, self.run_logger, self.mcp_config)
            messages = build_messages(messages, new_messages)
            steps += 1

        end_time = time.time()

        if messages[-1][ROLE] != Role.ASSISTANT:
            self.run_logger.warning("Maximum steps reached without getting an answer")
            messages.append({
                ROLE: Role.ASSISTANT,
                CONTENT: "超过最长次数限制，该问题无法解决",
            })

        self.run_logger.info(f"ID: {record.id}, Forward pass completed successfully")
        success = self.evaluate_prediction(question, gt, self.extract_last_answer(messages[-1][CONTENT]), manager)
        self.log_messages(messages, question, success, (end_time - start_time), all_prompt_tokens,
                          all_completion_tokens)
        self.run_logger.info(f"ID: {record.id}, Evaluation completed successfully")

        return dspy.Prediction(
            success=success,
            question=question,
            ground_truth=gt,
            answer=messages[-1][CONTENT],
            trace=messages,
            process_report=manager
        )