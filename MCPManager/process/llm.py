from tenacity import retry, stop_after_attempt, wait_exponential
from typing import List, Dict, Any
from openai import OpenAI
import copy
from cons.constants import *
import logging

from cons.log import LOGGER
from process.models import LLMCallRecord


class LLM:
    def __init__(self, model: str, lm_api_base: str, lm_api_key: str):
        self.model = model
        self.lm_api_base = lm_api_base
        self.lm_api_key = lm_api_key
        self.cli = OpenAI(api_key=self.lm_api_key, base_url=self.lm_api_base)

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )
    def call(self,
             messages: List[Dict],
             record: LLMCallRecord,
             temperature: float = 0.3,
             stop_word: str = None,
             logger: logging.Logger = LOGGER
             ) -> tuple[str, int, int]:
        response = None
        try:
            response = self.cli.chat.completions.create(
                extra_body={},
                model=self.model,
                messages=messages,
                temperature=temperature,
                top_p=0.9,
                stop=stop_word
            )
            response_text = response.choices[0].message.content
            print(f"LLM Response: {response_text.replace("\\n", "\n")}")
            completion_tokens = response.usage.completion_tokens
            prompt_tokens = response.usage.prompt_tokens
            record.lm_usages.append({
                "completion_tokens": completion_tokens,
                "prompt_tokens": prompt_tokens,
            })
            return response_text, completion_tokens, prompt_tokens
        except Exception as e:
            logger.error(f"ID: {record.id}, Error in call_lm: {str(e)}")
            logger.error(f"ID: {record.id}, Response: {response}")
            raise e

    @staticmethod
    def build_init_messages(system_prompt: str, question: str) -> List[Dict]:
        messages = [
            {
                ROLE: Role.SYSTEM,
                CONTENT: system_prompt
            },
            {
                ROLE: Role.USER,
                CONTENT: question
            },
        ]
        return messages

    def build_messages(self,
                       messages: List[Dict],
                       message_to_append: List[Dict],
                       ) -> List[Dict]:
        assert messages[0][ROLE] == Role.SYSTEM

        final_message = copy.deepcopy(messages)

        if message_to_append:
            final_message.extend(message_to_append)
            # if message_to_append[-1][ROLE] == Role.USER:
            #    assert len(message_to_append) == 1
            #    assert final_message[-1][ROLE] in {Role.ASSISTANT, constants.TOOL, Role.SYSTEM}
            #    final_message.extend(message_to_append)
            # elif message_to_append[-1][ROLE] == Role.ASSISTANT:
            #    assert len(message_to_append) == 1
            #    assert final_message[-1][ROLE] in {Role.USER, constants.TOOL}
            #    final_message.extend(message_to_append)
            # elif message_to_append[-1][ROLE] == constants.TOOL:
            #    assert len(message_to_append) == 2
            #    assert final_message[-1][ROLE] in {Role.USER, constants.TOOL}
            #    final_message.extend(message_to_append)

        # TODO: 超过最长上下文长度处理

        return final_message


class DotDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{key}'"
            )

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{key}'"
            )
