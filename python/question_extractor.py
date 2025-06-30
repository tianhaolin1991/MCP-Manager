from dataclasses import dataclass
from typing import List

from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from bean.bean import ManagerServer
from config.config import MODEL_NAME, API_KEY, BASE_URL
from utils.file_util import read_file, dataclass_to_json, read_jsonl_file, append_jsonl_file

if __name__ == "__main__":
    SYSTEM_PROMPT = read_file("prompts/TASK_GENERATE.txt")
    servers = read_jsonl_file("data/mcp-manager/manager_servers.jsonl", ManagerServer)
    output_file = "data/mcp-manager/manager_server_with_task.jsonl"
    chat_model = ChatOpenAI(model=MODEL_NAME, api_key=API_KEY, base_url=BASE_URL)
    for server in servers:
        for tool in server.tools:
            response = chat_model.invoke([SystemMessage(content=SYSTEM_PROMPT.format(tool=dataclass_to_json(tool)))])
            print(f"tool:{dataclass_to_json(tool)}:===========\n {response.content}")
            tool.task = response.content
        append_jsonl_file(output_file, server)
