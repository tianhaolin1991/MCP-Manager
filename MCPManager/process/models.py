import json
from dataclasses import field, dataclass
from typing import List, Dict, Optional
from cons.constants import Role


@dataclass
class LLMCallRecord:
    id: str
    lm_usages: List[Dict] = field(default_factory=list)
    mcp_rts: List[Dict] =  field(default_factory=list)
    mcp_retry_times: List[Dict] =  field(default_factory=list)


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
    servers: List['MCPServer']
    nested_dict: Dict[str, Dict[str, 'MCPTool']] = field(default_factory=dict)
    server_dict: Dict[str, 'MCPServer'] = field(default_factory=dict)

    def __post_init__(self):
        for server in self.servers:
            self.server_dict[server.name] = server
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
    url: str = ""
    tools: List['MCPTool'] = field(default_factory=list)


@dataclass
class MCPTool:
    server: str = ""
    name: str = ""
    description: str = ""
    arguments: List['ToolArgument'] = field(default_factory=list)

    def to_string(self) -> str:
        properties = {}
        required = []
        for argument in self.arguments:
            properties[argument.name] = {"type": argument.type, "description": argument.description}
            if argument.required:
                required.append(argument.name)
        tool_schema = {
            "server": self.server,
            "name": self.name,
            "inputSchema": {
                "type": "object",
                "properties": properties,
                "required": required
            }
        }
        return json.dumps(tool_schema, indent=4)


@dataclass
class ToolArgument:
    name: str
    description: str
    type: str
    required: bool = True

from pydantic import BaseModel
class MCPCall(BaseModel):
    mcp_server_name: Optional[str] = None
    mcp_tool_name: Optional[str] = None
    mcp_args: Optional[Dict] = None


class MCPCallList(BaseModel):
    shutdown: bool = False
    mcps: Optional[List[MCPCall]] = None
    raw_content: Optional[str] = None