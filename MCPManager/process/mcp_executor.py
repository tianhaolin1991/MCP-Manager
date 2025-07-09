import logging
import os

from tenacity import retry, stop_after_attempt, wait_exponential
from cons.constants import *
from cons.log import LOGGER
from process.models import *
from utils.file_util import read_json_file, from_dict, read_jsonl_file, append_jsonl_file
from utils.synced_mcp_client import SyncedMcpClient


class MCPExecutor:
    def __init__(self, config_file: str, max_token=5000, use_cache=True, cache_dir=f"{WORK_DIR}//cache"):
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
            url = f"http://localhost:{config.run_config[0].port}/sse"
            client = SyncedMcpClient(server_url=url)
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
                self.mcp_pool.servers.append(server)
                if use_cache:
                    append_jsonl_file(self.cache_file, server)
                server_cnt += 1
                total_tool_cnt += len(list_res.tools)
            LOGGER.info(f"MCP_EXECUTOR: {server.name} connected, tools-{len(server.tools)}")
            print(f"MCP_EXECUTOR: {server.name} connected, tools-{len(server.tools)}")
        LOGGER.info(f"MCP_EXECUTOR: INIT_FINISHED {server_cnt} servers connected, tools-{total_tool_cnt}")
        print(f"MCP_EXECUTOR: INIT_FINISHED {server_cnt} servers connected, tools-{total_tool_cnt}")

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
            return ""
        server = self.mcp_pool.get_server(tool_desc['server'])
        tool_name = tool_desc['name']
        print(f"Execute Tool\nServer:{server.name}\nTool:{tool_name}\nArgs:{tool_desc['arguments']}")
        result = server.client.call_tool(tool_name, tool_desc['arguments'])
        texts = [item.text for item in result.content]
        result_str_segment = ''.join(texts)
        logger.info(f"Execute Tool: {server.name}-{tool_name}, results:{result_str_segment}")
        return f'{Tag.OBSERVATION}{result_str_segment[0:self.max_token]}{Tag.OBSERVATION.close}'


if __name__ == '__main__':
    executor = MCPExecutor(config_file=f"{WORK_DIR}//mcp_configs//GAIA.json")
    #   response = executor.call("""```json
    #    {
    #      "server": "Fetch",
    #      "name": "fetch",
    #      "arguments": {
    #        "url": "https://www.baidu.com"
    #     }
    #    }
    #    ```""", LOGGER)
    #    print(response)

    response = executor.call("""```json
    { 
      "server": "DuckDuckGo Search Server",
      "name": "search",
      "arguments": {
        "query": "Hot News"
     }
    }
    ```""", LOGGER)
    print(response)
