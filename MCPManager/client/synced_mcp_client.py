import asyncio
import atexit
import pickle
from typing import Any, Tuple, Dict

from mcp import StdioServerParameters

from client.async_mcp_client import AsyncMCPClient


class SyncedMcpClient:
    """
    A synchronous MCP client that runs the AsyncMCPClient in a separate process
    and communicates with it using multiprocessing Queues and pickle.
    """

    def __init__(self, params: str | StdioServerParameters = None):
        self.async_client = AsyncMCPClient()
        self.params= params
        self.connected = False

    async def async_connect(self):
        if isinstance(self.params, StdioServerParameters):
            await self.async_client.connect_stdio(self.params)
        else:
            await self.async_client.connect_sse(self.params)
        self.connected = True

    async def async_disconnect(self):
        return await self.async_client.disconnect()

    async def async_call_tool(self, tool_name: str, tool_args: Dict = None) -> str:
        if not self.connected:
            await self.async_connect()
        return await self.async_client.execute(tool_name, tool_args)

    async def async_list_tools(self):
        """
        Lists all available tools synchronously.
        """
        if not self.connected:
            await self.async_connect()
        return await self.async_client.list_tools()

    def call_tool(self, tool_name: str, tool_args: Dict = None) -> str:
        return asyncio.run(self.async_call_tool(tool_name, tool_args))

    def list_tools(self):
        return asyncio.run(self.async_list_tools())