from abc import abstractmethod

from dspy import Prediction

import time

from cons.log import LOGGER
from process.llm import LLM
from process.mcp_executor import MCPExecutor
from process.models import LLMCallRecord
from process.evaluator import Evaluator
from cons.constants import *
import json

from process.react import ReactParser

SYSTEM_PROMPT = """# Role
You are a helpful assistant. You are able to answer questions using different tools. """


class MCPProgram():
    def setup_predict_llm(self, llm: LLM):
        self.llm = llm

    def setup_eval_llm(self, llm: LLM):
        self.eval_llm = llm

    def setup_mcp_executor(self, executor:MCPExecutor):
        self.executor = executor

    @abstractmethod
    def evaluate_prediction(self, question: str, ground_truth: str, prediction: str, record: LLMCallRecord):
        pass

    @abstractmethod
    def eval(self, **kwargs) -> Prediction:
        pass

    def log_messages(self, messages, question, success, time_cost, prompt_tokens_cost, completion_tokens_cost):
        log_entry = {
            "question": question,
            "messages": messages,
            "success": success,
            "time_cost": time_cost,
            "prompt_tokens_cost": prompt_tokens_cost,
            "completion_tokens_cost": completion_tokens_cost
        }
        LOGGER.info(json.dumps(log_entry, ensure_ascii=False))

class MCPPredict(MCPProgram):
    def __init__(self, max_steps=20, prompt_template=(REACT_PROMPT + SYSTEM_PROMPT).strip(),
                 task_name="mcp_sample"):
        super().__init__()
        self.prompt_template = prompt_template
        self.task_name = task_name
        self.max_steps = max_steps
        self.max_length = 30000
        self.system_prompt = None

    def evaluate_prediction(self, question: str, ground_truth: str, prediction: str, record: LLMCallRecord):
        answer_eval_record = LLMCallRecord(record.id)
        return Evaluator.evaluate_final_answer(self.eval_llm, question, ground_truth, prediction, answer_eval_record, LOGGER)

    def _build_system_content(self):
        servers = self.executor.mcp_pool.servers
        tools_section = ""
        for server in servers:
            for tool in server.tools:
                tools_section += tool.to_string() + '\n'
        self.system_prompt = self.prompt_template.format(TOOLS=tools_section.strip())


    def eval(self, **kwargs) -> Prediction:
        unique_id = kwargs.get('id')
        question = kwargs.get('question')
        gt = kwargs.get('answer')

        record = LLMCallRecord(unique_id)
        LOGGER.info(f"ID: {record.id}, Starting forward pass for question: {question}")

        if self.system_prompt is None:
            self._build_system_content()
        messages = LLM.build_init_messages(self.system_prompt, question)
        steps = 0
        all_completion_tokens = 0
        all_prompt_tokens = 0
        start_time = time.time()

        while not messages[-1][ROLE] == Role.ASSISTANT and steps < self.max_steps:
            messages.append(STEP_MESSAGE)
            """
               The LLM may generates [Observation] itself,
               I.e., it may generate
               [Thought] ... [Thought]
               [Action] ... [/Action]
               [Observation] ... [Observation],
               so we truncate it with `stop` words.
            """
            response, completion_tokens, prompt_tokens = self.llm.call(messages, record, stop_word=Tag.OBSERVATION.value, logger=LOGGER)
            message_tuples = ReactParser.parse(response)
            all_completion_tokens += completion_tokens
            all_prompt_tokens += prompt_tokens
            messages.pop()
            for message, tag in message_tuples:
                if tag == Tag.THOUGHT:
                    messages.append(message)
                if tag == Tag.ACTION:
                    messages.append(message)
                    observation = self.executor.call(message[CONTENT], LOGGER)
                    messages.append({ROLE: Role.USER, CONTENT: observation})
                    steps += 1
                if tag == Tag.ANSWER:
                    messages.append(message)
                    break

        end_time = time.time()

        if messages[-1][ROLE] != Role.ASSISTANT:
            LOGGER.warning("Maximum steps reached without getting an answer")
            messages.append({
                ROLE: Role.ASSISTANT,
                CONTENT: "超过最长次数限制，该问题无法解决",
            })

        LOGGER.info(f"ID: {record.id}, Forward pass completed successfully")
        success = self.evaluate_prediction(question, gt, messages[-1][CONTENT], record)
        self.log_messages(messages, question, success, (end_time - start_time), all_prompt_tokens,
                          all_completion_tokens)
        LOGGER.info(f"ID: {record.id}, Evaluation completed successfully")

        return Prediction(
            success=success,
            question=question,
            ground_truth=gt,
            answer=messages[-1][CONTENT],
            trace=messages,
            process_report=record
        )

    def evaluate(self, devset, metric):
        results = []
        for idx, item in enumerate(devset):
            prediction = self.eval(**item.inputs())
            score = metric(item, prediction)
            results.append((prediction, score))
        results = [((Prediction(), 0.0) if r is None else r) for r in results]
        results = [(example, prediction, score) for example, (prediction, score) in zip(devset, results)]
        ncorrect, ntotal = sum(score for *_, score in results), len(devset)
        return round(100 * ncorrect / ntotal, 2), results
