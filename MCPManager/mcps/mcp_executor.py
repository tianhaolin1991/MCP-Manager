import logging
import os

from mcp import StdioServerParameters
from tenacity import retry, stop_after_attempt, wait_exponential
from cons.constants import *
from cons.log import LOGGER
from process.models import *
from utils.file_util import read_json_file, read_jsonl_file, append_jsonl_file
from client.synced_mcp_client import SyncedMcpClient


class MCPExecutor:
    def __init__(self, config_file: str, max_token=5000, use_cache=True, cache_dir=f"{WORK_DIR}//mcps//cache"):
        mcp_config = read_json_file(config_file, MCPConfig)
        self.mcp_pool = MCPPool()
        self.max_token = max_token
        self.cache_file = f'{cache_dir}//mcp_servers.jsonl'
        server_cnt = 0
        total_tool_cnt = 0
        if use_cache:
            os.makedirs(cache_dir, exist_ok=True)
            servers = read_jsonl_file(self.cache_file, MCPServer)
            self.mcp_pool.add_servers(servers)
        for config in mcp_config.mcp_pool:
            run_config = config.run_config[0]
            if run_config.mode == "stdio" :
                command = run_config.command.replace("[WORK_DIR]", f"{WORK_DIR}")
                client = SyncedMcpClient(params=StdioServerParameters(command=command, args=run_config.args, env=run_config.env))
            else:
                url = run_config.url
                client = SyncedMcpClient(params=url)
            server = MCPServer(name=config.name, description=config.description if config.description else "",
                               client=client)
            cached_server = self.mcp_pool.get_server(server.name)
            if cached_server:
                cached_server.client = server.client
                server_cnt += 1
                total_tool_cnt += len(cached_server.tools)
                server = cached_server
            else:
                list_res = client.list_tools()
                for tool in list_res.tools:
                    mcp_tool = MCPTool(server.name, name=tool.name, description=tool.description,
                                       input_schema=tool.inputSchema)
                    server.tools.append(mcp_tool)
                self.mcp_pool.add_servers([server])
                if use_cache:
                    append_jsonl_file(self.cache_file, server)
                server_cnt += 1
                total_tool_cnt += len(list_res.tools)
            LOGGER.info(f"MCP_EXECUTOR: {server.name} connected, tools-{len(server.tools)}")
        LOGGER.info(f"MCP_EXECUTOR: INIT_FINISHED {server_cnt} servers connected, tools-{total_tool_cnt}")

    @staticmethod
    def extract(content:str):
        match = JSON_PATTERN.search(content)
        if not match:
            return None
        tool_desc = json.loads(match.group(1).strip())
        return tool_desc

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )
    def call(self, content: str, logger: logging.Logger) -> str:
        tool_desc = MCPExecutor.extract(content)
        if not tool_desc:
            logger.error(f"NO TOOLS FOUND FROM, {content}")
            return f"NO TOOLS FOUND FROM YOUR ACTION: {content}"
        server = self.mcp_pool.get_server(tool_desc['server'])
        mcp_cli = server.client
        tool_name = tool_desc['name']
        logger.debug(f"Execute Tool\nServer:{server.name}\nTool:{tool_name}\nArgs:{tool_desc['arguments']}")
        result = mcp_cli.call_tool(tool_name, tool_desc['arguments'])
        logger.debug(f"Execute Tool: {server.name}-{tool_name}, results:{result}")
        return f'{Tag.OBSERVATION.start}{result[0:self.max_token]}{Tag.OBSERVATION.close}'


if __name__ == '__main__':
    executor = MCPExecutor(config_file=f"{WORK_DIR}//mcps//config//GAIA_ALL.json")
    response = executor.call("""```json
{
    "server": "Aliven",
    "name": "list_projects"
}
```""", LOGGER)
    print(response)
