import json
from typing import List, Set

from pydantic import BaseModel, Field
from bean.bean import ZeroServer, ManagerServerNew, ManagerTool, Domain, ServerMetaData
from config.config import API_KEY, BASE_URL, MODEL_NAME

from utils.file_util import read_json_file, remove_file, read_jsonl_file, append_jsonl_file, read_file, \
    dataclass_to_json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain.output_parsers import PydanticOutputParser

SUMMARIZE_PROMPT = read_file("prompts/SERVER_SUMMARIZE_NEW.txt")
CORRECT_PROMPT = read_file("prompts/CORRECTION.txt")
DEFAULT_DOMAINS = [dataclass_to_json(domain) for domain in read_jsonl_file("data/domain/default.jsonl", Domain)]


# class ToolSetModel(BaseModel):
#    summary: str = Field(description="工具集能力总结")
#    domains: List[Domain] = Field(description="工具集所属领域（可能多个）")

class ToolSetModel(BaseModel):
    functionalities: List[str]
    product_or_platform: str
    domains: List[str]


def get_visited(output_path, use_cache):
    if use_cache:
        lst = read_jsonl_file(output_path, ManagerServerNew)
    else:
        remove_file(output_path)
        lst = []
    visited = set()
    for manager_server in lst:
        visited.add(f'{manager_server.name}')
    return visited


def to_manager_server(zero_server: ZeroServer, chatModel: ChatOpenAI) -> ManagerServerNew:
    tools = "-----".join([f'{tool.name}:{tool.description}' for tool in zero_server.tools])
    parser = PydanticOutputParser(pydantic_object=ToolSetModel)
    system_msg_str = SUMMARIZE_PROMPT.format(server=zero_server.name, tools=tools)
    msg = SystemMessage(content=system_msg_str)
    response = chatModel.invoke([msg])
    toolSet = parser.parse(response.content)
    server_meta = ServerMetaData(functionalities=toolSet.functionalities, product_or_platform=toolSet.product_or_platform, domains=toolSet.domains)
    # TODO- 判断提取的domain是否合理？
    # msg = SystemMessage(content=CORRECT_PROMPT.format(initial_domains=f'[{",".join(toolSet.domains)}]', known_domains=f'[{",".join(toolSet.domains)}]', tools=tools))
    # response = chatModel.invoke([msg])
    # print(response.content)
    manager_tools = [ManagerTool(name=tool.name, server=zero_server.name, description=tool.description,
                                 parameter=tool.parameter, task="") for tool in
                     zero_server.tools]
    return ManagerServerNew(name=zero_server.name, meta_data=server_meta, tools=manager_tools)


def main(data_path, output_path, use_cache=True):
    zero_servers = read_jsonl_file(data_path, ZeroServer)
    chat_model = ChatOpenAI(model=MODEL_NAME, api_key=API_KEY, base_url=BASE_URL)
    visited = get_visited(output_path, use_cache)
    for zero_server in zero_servers:
        name = zero_server.name
        if name in visited:
            continue
        manager_server = to_manager_server(zero_server, chat_model)
        visited.add(name)
        tools = [f'name:{tool.name}' for tool in manager_server.tools]
        print(f"""============= Convert Server {manager_server.name} to Success ==============
DESC:   {manager_server.meta_data} 
TOOLS:  {len(tools)}""")
        append_jsonl_file(output_path, manager_server)


if __name__ == '__main__':
    org_data_path = "data/mcp-zero/mcp_tools.jsonl"
    output_data_path = "data/mcp-manager/manager_servers.jsonl"
    main(data_path=org_data_path, output_path=output_data_path, use_cache=False)
