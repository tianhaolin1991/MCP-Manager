from dataclasses import dataclass
from typing import Set


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
    tools: list[ZeroTool]


@dataclass
class ManagerTool:
    name: str
    description: int
    parameter: dict[str, str]
    domain: str

@dataclass
class ManagerServer:
    name: str
    description: str
    tools: list[ManagerTool]

    @property
    def domains(self) -> Set[str]:
        return {b.domain for b in self.tools}