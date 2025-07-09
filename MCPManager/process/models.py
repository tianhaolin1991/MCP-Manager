import json
from dataclasses import field, dataclass
from typing import List, Dict, Optional

from cons.constants import Role
from utils.synced_mcp_client import SyncedMcpClient


@dataclass
class LLMCallRecord:
    id: str = ""
    lm_usages: List[Dict] = field(default_factory=list)
    mcp_rts: List[Dict] = field(default_factory=list)
    mcp_retry_times: List[Dict] = field(default_factory=list)


@dataclass
class Message:
    role: Role
    content: str


### ===================MCP====================
@dataclass
class MCPConfig:
    mcp_pool: List['ServerConfig']


@dataclass
class ServerConfig:
    name: str
    description: Optional[str]
    run_config: List['RunConfig']


@dataclass
class RunConfig:
    command: str
    port: int


@dataclass
class MCPPool:
    servers: List['MCPServer'] = field(default_factory=list)
    nested_dict: Dict[str, Dict[str, 'MCPTool']] = field(default_factory=dict)
    server_dict: Dict[str, 'MCPServer'] = field(default_factory=dict)

    def __post_init__(self):
        for server in self.servers:
            self.server_dict[server.name] = server
            self.nested_dict[server.name] = {}
            for tool in server.tools:
                tool.server = server.name
                self.nested_dict[server.name][tool.name] = tool

    def add_servers(self, servers:[]):
        for server in servers:
            self.servers.append(server)
            self.server_dict[server.name] = server
            self.nested_dict[server.name] = {}
            for tool in server.tools:
                tool.server = server.name
                self.nested_dict[server.name][tool.name] = tool

    def get_tool(self, server: str, tool: str) -> 'MCPTool':
        return self.nested_dict.get(server).get(tool)

    def get_server(self, server) -> 'MCPServer':
        return self.server_dict.get(server)


@dataclass
class MCPServer:
    name: str = ""
    description: str = ""
    tools: List['MCPTool'] = field(default_factory=list)
    client: Optional[SyncedMcpClient] = field(
        default=None,
        metadata={'exclude': True}
    )


@dataclass
class MCPTool:
    server: str = ""
    name: str = ""
    description: str = ""
    input_schema: Dict = field(default_factory=dict)

    def to_string(self) -> str:
        tool_schema = {
            "server": self.server,
            "name": self.name,
            "inputSchema": self.input_schema
        }
        return json.dumps(tool_schema, indent=4)
