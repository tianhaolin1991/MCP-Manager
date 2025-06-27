import asyncio
from typing import List, Set

from pydantic import BaseModel, Field
from bean.bean import ZeroServer, ManagerServer, ManagerTool
from utils.file_util import read_json_file, remove_file, read_jsonl_file, append_jsonl_file, read_file
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain.output_parsers import PydanticOutputParser

SYSTEM_PROMPT = read_file("prompts/SERVER_DOMAIN_SUMMARIZE.txt")
API_KEY = "f3c853c7-2505-4219-b9d5-73f4a945707a"
base_url = 'https://api.openai.com/v1/'


class DomainItem(BaseModel):
    name: str = Field(description="工具名称")
    domain: str = Field(description="工具功能所属领域")


class ToolsetModel(BaseModel):
    summary: str = Field(description="工具集能力总结")
    domains: List[DomainItem] = Field(description="工具所属领域集合")

    @property
    def domain_dict(self):
        return {domain.name: domain.domain for domain in self.domains}


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
    msg = SystemMessage(content=SYSTEM_PROMPT.format(domains=domains, tools=tools))
    response = chatModel.invoke([msg])
    parser = PydanticOutputParser(pydantic_object=ToolsetModel)
    toolSet = parser.parse(response.content)
    domain_dict = toolSet.domain_dict
    tools = [ManagerTool(name=tool.name, description=tool.description, parameter=tool.parameter, domain=domain_dict[tool.name]) for tool in zero_server.tools]
    domains.update([domain_model.domain for domain_model in toolSet.domains])
    return ManagerServer(name=zero_server.name, description=toolSet.summary, tools=tools)


def main(data_path, output_path, use_cache=True):
    zero_servers = read_jsonl_file(data_path, ZeroServer)
    chat_model = ChatOpenAI(model='deepseek-v3-250324', api_key=API_KEY,
                            base_url='https://ark.cn-beijing.volces.com/api/v3')
    domains = set()
    visited = get_visited(output_path, use_cache)
    for zero_server in zero_servers:
        name = zero_server.name
        if name in visited:
            continue
        manager_server = to_manager_server(zero_server, domains, chat_model)
        visited.add(name)
        tools = [f'name:{tool.name},domain:{tool.domain}\n' for tool in manager_server.tools]
        print(f"""============= Convert Server {manager_server.name} to Success ==============
{manager_server.description}
{tools}""")
        append_jsonl_file(output_path, manager_server)


if __name__ == '__main__':
    org_data_path = "./data/mcp-zero/mcp_tools_with_embedding_test.jsonl"
    output_data_path = "./data/mcp-manager/tool_mananger_with_embedding_test.jsonl"
    main(data_path=org_data_path, output_path=output_data_path, use_cache=False)
