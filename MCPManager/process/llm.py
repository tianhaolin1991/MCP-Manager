
from openai.types.chat import ChatCompletionMessageParam
from tenacity import retry, stop_after_attempt, wait_exponential
from typing import List, Dict
from openai import OpenAI
import copy
from cons.constants import *
import logging

from process.mcp_executor import MCPExecutor





class LLM:
    def __init__(self, model, lm_api_base, lm_api_key):
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
             messages: List[ChatCompletionMessageParam],
             record: LLMCallRecord,
             logger: logging.Logger,
             ) -> tuple[str | None, int, int]:

        response = None
        try:
            response = self.cli.chat.completions.create(
                extra_body={},
                model=self.model,
                messages=messages,
                stop=Tag.OBSERVATION.value
            )
            print("Response is " + str(response.choices))
            response_text = response.choices[0].message.content
            completion_tokens = response.usage.completion_tokens
            prompt_tokens = response.usage.prompt_tokens
            record.lm_usages.append({
                "completion_tokens": completion_tokens,
                "prompt_tokens": prompt_tokens,
            })
            return response_text, completion_tokens, prompt_tokens

        except Exception as e:
            logger.error(f"ID: {record.id}, Error in call_lm: {str(e)}")
            if response:
                logger.error(f"ID: {record.id}, Response: {response}")
            raise

    def build_system_content(base_system: str,
                             mcps: List) -> str:
        tools_section = "## Available Tools\n"
        for mcp in mcps:
            tools_section += f"### {mcp['name']}\n"
            tools_section += f"{mcp['description']}\n\n"

            for t in mcp['tools']:
                tools_section += f"- {t['tool_name']}: {t['tool_description']}\n"
                tools_section += "  Input parameters:\n"
                for inp in t['inputs']:
                    required = "Required" if inp['required'] else "Optional"
                    tools_section += f"    - {inp['name']} ({inp['type']}, {required}): {inp['description']}\n"
                tools_section += "\n"

        prompt = base_system + f"""{tools_section}"""

        return prompt

    def build_init_messages(self,
                            base_system: str,
                            mcp_executor: MCPExecutor,
                            user_question: str, ) -> List[Dict]:
        system_content = self.build_system_content(base_system, mcp_executor)
        messages = [
            {
                ROLE: Role.SYSTEM,
                CONTENT: system_content
            },
            {
                ROLE: Role.USER,
                CONTENT: user_question
            }
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
