import asyncio
import copy
from typing import List, Set

from pydantic import BaseModel, Field
from bean.bean import ZeroServer, ManagerServer, ManagerTool
from bean.domain import Domain
from utils.file_util import read_json_file, remove_file, read_jsonl_file, append_jsonl_file, read_file, \
    dataclass_to_json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain.output_parsers import PydanticOutputParser

SUMMARIZE_PROMPT = read_file("prompts/SERVER_SUMMARIZE.txt")
CORRECT_PROMPT = read_file("prompts/CORRECTION.txt")
BASE_URL = 'https://ark.cn-beijing.volces.com/api/v3'
API_KEY = "f3c853c7-2505-4219-b9d5-73f4a945707a"
DEFAULT_DOMAINS = [dataclass_to_json(domain) for domain in read_jsonl_file("data/domains.jsonl", Domain)]


class ToolSetModel(BaseModel):
    summary: str = Field(description="工具集能力总结")
    domains: List[Domain] = Field(description="工具集所属领域（可能多个）")


def get_visited(output_path, use_cache):
    if use_cache:
        lst = read_jsonl_file(output_path, ManagerServer)
    else:
        remove_file(output_path)
        lst = []
    visited = set()
    for manager_server in lst:
        visited.add(f'{manager_server.name}')
    return visited


def to_manager_server(zero_server: ZeroServer, domains: Set[str], chatModel: ChatOpenAI) -> ManagerServer:
    tools = "-----".join([f'{tool.name}:{tool.description}' for tool in zero_server.tools])
    parser = PydanticOutputParser(pydantic_object=ToolSetModel)
    msg = SystemMessage(content=SUMMARIZE_PROMPT.format(domains=f'{"\n".join(domains)}', tools=tools,
                                                        output_schema=ToolSetModel.model_json_schema()))
    print(msg.content)
    response = chatModel.invoke([msg])
    toolSet = parser.parse(response.content)
    # TODO- 判断提取的domain是否合理？
    # msg = SystemMessage(content=CORRECT_PROMPT.format(initial_domains=f'[{",".join(toolSet.domains)}]', known_domains=f'[{",".join(toolSet.domains)}]', tools=tools))
    # response = chatModel.invoke([msg])
    # print(response.content)
    manager_tools = [ManagerTool(name=tool.name, description=tool.description, parameter=tool.parameter) for tool in
                     zero_server.tools]
    domains.update(toolSet.domains)
    return ManagerServer(name=zero_server.name, description=toolSet.summary, tools=manager_tools,
                         domains=toolSet.domains)


def main(data_path, output_path, use_cache=True):
    zero_servers = read_jsonl_file(data_path, ZeroServer)
    chat_model = ChatOpenAI(model='deepseek-v3-250324', api_key=API_KEY, base_url=BASE_URL)
    domains = set(DEFAULT_DOMAINS)
    visited = get_visited(output_path, use_cache)
    for zero_server in zero_servers:
        name = zero_server.name
        if name in visited:
            continue
        manager_server = to_manager_server(zero_server, domains, chat_model)
        visited.add(name)
        tools = [f'name:{tool.name}' for tool in manager_server.tools]
        print(f"""============= Convert Server {manager_server.name} to Success ==============
DESC:   {manager_server.description} 
DOMAIN: {manager_server.domains}
TOOLS:  {len(tools)}""")
        append_jsonl_file(output_path, manager_server)


if __name__ == '__main__':
    org_data_path = "./data/mcp-zero/mcp_tools_with_embedding_test.jsonl"
    output_data_path = "./data/mcp-manager/tool_mananger_with_embedding_test.jsonl"
    main(data_path=org_data_path, output_path=output_data_path, use_cache=False)
