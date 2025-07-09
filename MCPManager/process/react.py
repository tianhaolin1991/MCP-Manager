from typing import List

from cons.constants import *


class ReactParser:
    @staticmethod
    def parse(text: str) -> List:
        """
        return message, Tag tuple list
        """
        _, thought = Tag.THOUGHT.extract(text)
        answer, answer_with_tag = Tag.ANSWER.extract(text)
        messages = []
        if thought:
            messages.append(({ROLE: Role.ASSISTANT, CONTENT: thought}, Tag.THOUGHT))
        if answer:
            messages.append(({ROLE: Role.ASSISTANT, CONTENT: answer_with_tag}, Tag.ANSWER))
            return messages
        action, action_with_tag = Tag.ACTION.extract(text)
        if action_with_tag:
            messages.append(({ROLE: Role.ASSISTANT, CONTENT: action_with_tag}, Tag.ACTION))
        return messages