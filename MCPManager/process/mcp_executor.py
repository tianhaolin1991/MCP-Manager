import logging

from cons.constants import *
from process.models import *
from utils.file_util import read_json_file
from utils.synced_mcp_client import SyncedMcpClient


class MCPExecutor:
    def __init__(self, config_file: str):
        mcp_config = read_json_file(config_file, MCPConfig)
        for config in mcp_config.mcp_pool:
            url = f"http://localhost:{config.run_config[0].port}/sse"
            client = SyncedMcpClient(server_url=url)
            tools = client.list_tools()
            for tool in tools:
                print(tool)


    def response_parsing(self, content: str) -> MCPTool:
        matches = re.findall(ACTION_PATTERN, content, re.DOTALL)
        mcps = []
        for match in matches:
            try:
                data = json.loads(match)
                mcps.append(MCPCall(
                    mcp_server_name=data['server_name'].strip(),
                    mcp_tool_name=data['tool_name'].strip(),
                    mcp_args=data['inputs']
                ))
            except json.JSONDecodeError as e:
                # Log the error and the problematic content
                logging.error(f"Failed to parse tool call JSON: {e}. Content: '{match}'")
                # Continue to the next match
                continue

        if mcps:
            return MCPCallList(shutdown=False, mcps=mcps, raw_content=content)
        else:
            return MCPCallList(shutdown=True, mcps=None, raw_content=content)

    ## TODO--逻辑不太对
    def mcp_calling(self,
                    mcp_call_list: MCPCallList,
                    record: LLMCallRecord,
                    logger: logging.Logger,
                    config: dict
                    ) -> List[Dict]:
        logger.debug(f"ID:{record.id}, Entering mcp_calling with mcp_call_list: {mcp_call_list}")

        if mcp_call_list.shutdown:
            logger.info(f"ID:{record.id}, Shutdown flag is set. No more MCP calling.")
            messages = [
                {
                    ROLE: Role.ASSISTANT,
                    CONTENT: mcp_call_list.raw_content if mcp_call_list.raw_content else '',
                }
            ]
            logger.debug(f"ID:{record.id}, Shutdown messages prepared: {messages}")
            return messages
        else:
            logger.info(f"ID:{record.id}, Processing MCP call list with {len(mcp_call_list.mcps)} MCPs.")
            mcp_list = mcp_call_list.mcps
            messages = [
                {
                    ROLE: Role.USER,
                    CONTENT: mcp_call_list.raw_content if mcp_call_list.raw_content else '',
                }
            ]
            result_str = "<Observation>{output}</Observation>"
            for idx, mcp in enumerate(mcp_list, start=1):
                logger.info(f"ID:{record.id}, Processing MCP #{idx}: {mcp}")
                mcp_server_name = mcp.mcp_server_name
                mcp_tool_name = mcp.mcp_tool_name
                mcp_args = mcp.mcp_args

                action = f"""<Action>{{
            "name": {mcp_tool_name},
            "arguments": {json.dumps(mcp_args, ensure_ascii=False)}
    }}</Action>
    """
                messages[0][CONTENT] = action
                logger.info(
                    f"ID:{record.id}, Calling MCP Server: {mcp_server_name}, Tool: {mcp_tool_name}, Arguments: {mcp_args}")

                # Manage manager.mcp_rts and manager.mcp_retry_times
                try:
                    parsed_data = config

                    target_name = mcp_server_name
                    port = None
                    url = None
                    for item in parsed_data.get("mcp_pool", []):
                        if item.get("name") != target_name:
                            continue

                        url = item.get("url", "")
                        if url:
                            logger.debug(f"ID:{record.id}, Found URL for MCP Server '{target_name}': {url}")
                            break
                        run_configs = item.get("run_config", [])
                        for config in run_configs:
                            port = config.get("port")
                            if port:
                                url = f"http://localhost:{port}/sse"
                                logger.debug(f"ID:{record.id}, Constructed URL for MCP Server '{target_name}': {url}")
                                break
                        if url:
                            break

                    if not url:
                        logger.error(f"ID:{record.id}, No valid URL found for MCP Server '{target_name}'.")
                        raise ValueError(f"ID:{record.id}, No valid URL found for MCP Server '{target_name}'.")

                    client = SyncedMcpClient(server_url=url)
                    logger.debug(f"ID:{record.id}, Initialized SyncedMcpClient with URL: {url}")
                    client.list_tools()
                    logger.debug(f"ID:{record.id}, Retrieved tool list from MCP Server '{target_name}'.")
                except Exception as e:
                    logger.error(
                        f"ID:{record.id}, Failed to initialize SyncedMcpClient for server '{mcp_server_name}': {str(e)}")
                    client = None

                if client:
                    try:
                        logger.debug(f"ID:{record.id}, Calling tool '{mcp_tool_name}' with arguments: {mcp_args}")
                        result = client.call_tool(mcp_tool_name, mcp_args)
                        texts = [item.text for item in result.content]
                        result_str_segment = ''.join(texts)
                        logger.debug(
                            f"ID:{record.id}, Received result from tool '{mcp_tool_name}': {result_str_segment}")

                        logger.info(
                            f"ID:{record.id}, MCP Server '{mcp_server_name}' returned: {result_str_segment[:5000]}")

                        result_str.format(output=result_str_segment[:5000])
                    except Exception as e:
                        logger.error(
                            f"ID:{record.id}, Error calling tool '{mcp_tool_name}' on MCP Server '{mcp_server_name}': {str(e)}")
                else:
                    logger.warning(
                        f"ID:{record.id}, Skipping tool call for '{mcp_tool_name}' due to client initialization failure.")

            messages.append({
                ROLE: Role.USER,
                CONTENT: result_str,
            })
            logger.debug(f"ID:{record.id}, Final messages prepared: {messages}")
            logger.info(f"ID:{record.id}, mcp_calling completed successfully.")
            return messages


if __name__ == '__main__':
    MCPExecutor(config_file="D://PYTHON//MCP-Manager//MCPManager//servers//mcp_config_gaia.json")
