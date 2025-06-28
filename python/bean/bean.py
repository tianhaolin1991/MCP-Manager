from dataclasses import dataclass
from typing import Set, List


@dataclass
class ZeroTool:
    name: str
    description: int
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
    description: int
    parameter: dict[str, str]

@dataclass
class ManagerServer:
    name: str
    description: str
    tools: List[ManagerTool]
    domains: List[str]