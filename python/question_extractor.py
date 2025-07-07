import json
from dataclasses import dataclass
from typing import List

from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from bean.bean import ManagerServer, ToolQuery
from config.config import MODEL_NAME, API_KEY, BASE_URL
from utils.file_util import read_file, dataclass_to_json, read_jsonl_file, append_jsonl_file, from_dict


class PydanticToolQuery(BaseModel):
    category: str
    query: str


if __name__ == "__main__":
    SYSTEM_PROMPT = read_file("prompts/TASK_GENERATE_NEW.txt")
    servers = read_jsonl_file("data/mcp-manager/manager_servers_old.jsonl", ManagerServer)
    output_file = "data/mcp-manager/manager_server_with_task_0.jsonl"
    chat_model = ChatOpenAI(model=MODEL_NAME, api_key=API_KEY, base_url=BASE_URL)
    parser = PydanticOutputParser(pydantic_object=PydanticToolQuery)
    for server in servers:
        for tool in server.tools:
            tool_desc = {'server':tool.server, 'name': tool.name, 'description': tool.description, 'parameter':tool.parameter}
            response = chat_model.invoke([SystemMessage(content=SYSTEM_PROMPT.format(tool=json.dumps(tool_desc)))])
            print(f"tool:{dataclass_to_json(tool)}:===========\n {response.content}")
            pydantic_tool_query = parser.parse(response.content)
            tool.task = ToolQuery(category=pydantic_tool_query.category, query=pydantic_tool_query.query)
        append_jsonl_file(output_file, server)
