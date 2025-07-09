import copy
import os
from contextlib import AsyncExitStack
from datetime import timedelta
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.sse import sse_client
from mcp.client.stdio import stdio_client
from mcp.types import TextContent
from cons.log import LOGGER


class AsyncMCPClient:
    def __init__(self):
        self.name = "mcp"  # Keep name for backward compatibility
        self.exit_stack:AsyncExitStack = AsyncExitStack()
        self.session = None
        self.id = None

    async def execute(self, name: str, arguments: dict[str, Any] | None = None, ) -> str:
        try:
            LOGGER.info(f"Executing tool: {name}")
            result = await self.session.call_tool(name, arguments, timedelta(seconds=600))
            content_str = ", ".join(
                item.text for item in result.content if isinstance(item, TextContent)
            )
            return content_str
        except Exception as e:
            LOGGER.error(f"Executing tool: {name} error: {e}")
            raise e

    async def connect_sse(self, server_url: str) -> None:
        """Connect to an MCP server using SSE transport."""
        if not server_url:
            raise ValueError("Server URL is required.")
        self.id = server_url
        streams_context = sse_client(url=server_url)
        streams = await self.exit_stack.enter_async_context(streams_context)
        self.session = await self.exit_stack.enter_async_context(ClientSession(*streams))
        await self._initialize()

    async def connect_stdio(self, org_params: StdioServerParameters) -> None:
        """Connect to an MCP server using stdio transport."""
        params = copy.deepcopy(org_params)
        self.id = params.command
        args = ['/C', f"{params.args or ''} {params.command}"]
        params.args =  args
        params.command = 'cmd'
        env_copy = os.environ.copy()
        for key, value in params.env.items():
            env_copy[key] = value
        LOGGER.info(f"command: {self.id}, env: {params.env}")
        params.env = env_copy
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(params))
        read, write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(read, write))
        await self._initialize()

    async def _initialize(self) -> None:
        await self.session.initialize()

    async def list_tools(self):
        return await self.session.list_tools()

    async def disconnect(self) -> None:
        """Disconnect from a specific MCP server or all servers if no server_id provided."""
        try:
            # Close the exit stack which will handle session cleanup
            try:
                await self.exit_stack.aclose()
            except RuntimeError as e:
                if "cancel scope" in str(e).lower():
                    LOGGER.warning(
                        f"Cancel scope error during disconnect from {self.id}, continuing with cleanup: {e}"
                    )
                else:
                    raise
            LOGGER.info(f"Disconnected from MCP server {self.id}")
        except Exception as e:
            LOGGER.error(f"Error disconnecting from server {self.id}: {e}")
        LOGGER.info("Disconnected from all MCP servers")
