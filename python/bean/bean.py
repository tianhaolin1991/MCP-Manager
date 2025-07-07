from dataclasses import dataclass
from typing import List, Union


@dataclass
class ZeroTool:
    name: str
    description: str
    parameter: dict[str, str]


@dataclass
class ZeroServer:
    name: str
    description: str
    url: str
    readme_file: str
    summary: str
    tools: List[ZeroTool]


@dataclass
class ManagerTool:
    name: str
    server: str
    description: str
    parameter: dict[str, str]
    task: Union[str, 'ToolQuery'] = ""


@dataclass
class Domain:
    name: str
    description: str

@dataclass
class ServerMetaData:
    functionalities: List[str]
    product_or_platform: str
    domains: List[str]


@dataclass
class ManagerServerOld:
    name: str
    description: str
    tools: List[ManagerTool]
    domains: List[Domain]

    def tool(self, name: str):
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None

@dataclass
class ManagerServer:
    name: str
    meta_data: ServerMetaData
    tools: List[ManagerTool]

    def tool(self, name: str):
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None

@dataclass
class ManagerServerEmbeddings:
    name: str
    server: dict[str, List[float]]
    tools: dict[str, List[float]]


@dataclass
class ToolQuery:
    category: str
    query: str