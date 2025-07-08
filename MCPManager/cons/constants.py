import re
from enum import Enum

ROLE = 'role'
CONTENT = 'content'

class Role(Enum):
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT = 'assistant'

class Tag(Enum):
    THOUGHT = '[Thought]'
    ACTION = '[Action]'
    OBSERVATION = '[Observation]'
    ANSWER = '[Answer]'

    @property
    def close(self):
        return self.value.replace('[', '[/')

REACT_PROMPT = """# Guidelines
Use the following format to accomplish user's request:
[Thought] think about what to do next to solve the question [/Thought]
[Action] use a tool, the action must be a json object wrapped by ```json and ```
```json
{{
    "server": string, tool's corresponding server
    "name": string, name of the tool, it must refer to one of available tools
    "arguments": {{ [key: string]: unknown }}, arguments for the tool, each argument must be a valid json value required by the tool; it can be omitted, if the tool does not accept parameters
}}
```
For example,
```json
{{  
    "server": "myServer",
    "name": "foo"
    "arguments": {{
        "url": "http://example.com",
        "count": 3,
        "items": ["abc", "xyz"]
    }}
}}
```
[/Action]
[Observation] the result of the action [/Observation]
... (Thought/Action/Observation may repeat N times to accomplish user's request)
[Answer] the final answer to the original input question [/Answer]

NEVER generate [Observation] yourself. This is an important requirement.

You must generate either a pair of [Thought] and [Action] or a pair of [Thought] and [Answer]
Examples:
Output: [Thought] I need to search the web to get related knowledge {Tag.THOUGHT.close} [Action] ... [/Action]
Output: [Thought] I know the final answer now {Tag.THOUGHT.close} [Answer] ... [/Answer]

- If there are no available tools, generate final answer directly.
# Available Tools
{TOOLS}

"""
    
THOUGHT_PATTERN = re.compile(rf'{Tag.THOUGHT}(.+?){Tag.THOUGHT.close}', re.DOTALL)
ACTION_PATTERN = re.compile(rf'{Tag.ACTION}(.+?){Tag.ACTION.close}', re.DOTALL)
OBSERVATION_PATTERN = re.compile(rf'{Tag.OBSERVATION}(.+?){Tag.OBSERVATION.close}', re.DOTALL)
ANSWER_PATTERN = re.compile(rf'{Tag.ANSWER}(.+?){Tag.ANSWER.close}', re.DOTALL)

STEP_PROMPT=f"Decide what to do next. Output a pair of {Tag.THOUGHT} and {Tag.ACTION}, a pair of {Tag.THOUGHT} and {Tag.ANSWER}, or a single {Tag.ANSWER}"