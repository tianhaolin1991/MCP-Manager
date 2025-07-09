import asyncio
import atexit
import threading
from typing import Any, Dict, Optional

from mcp import StdioServerParameters

from client.async_mcp_client import AsyncMCPClient


class SyncedMcpClient:
    def __init__(self, params: str | StdioServerParameters = None):
        self.async_client = AsyncMCPClient()
        self.params = params
        self._connected = False
        self._lock = threading.Lock()  # 线程锁：确保状态操作安全
        self._loop = asyncio.new_event_loop()  # 创建单例事件循环
        self._loop_thread = threading.Thread(
            target=self._run_loop, daemon=True  # 后台线程运行事件循环
        )
        self._loop_thread.start()
        atexit.register(self._sync_disconnect)  # 程序退出时自动清理

    def _run_loop(self):
        """在后台线程中运行事件循环"""
        asyncio.set_event_loop(self._loop)
        self._loop.run_forever()

    def _sync_disconnect(self):
        """同步调用异步的disconnect()"""
        if self._loop.is_running():
            # 在事件循环中调度disconnect，并等待完成
            asyncio.run_coroutine_threadsafe(self.async_client.disconnect(), self._loop).result()
        # 停止事件循环并等待线程结束
        self._loop.call_soon_threadsafe(self._loop.stop)
        self._loop_thread.join()

    def _run_async(self, coro) -> Any:
        """同步执行异步协程（线程安全）"""
        if not self._loop.is_running():
            raise RuntimeError("事件循环已停止，无法执行异步操作")
        # 在后台事件循环中调度协程，并阻塞等待结果（设置超时避免无限阻塞）
        future = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return future.result(timeout=60)  # 60秒超时

    def _ensure_connected(self):
        """确保连接已建立（线程安全）"""
        with self._lock:
            if not self._connected:
                if isinstance(self.params, StdioServerParameters):
                    self._run_async(self.async_client.connect_stdio(self.params))
                else:
                    self._run_async(self.async_client.connect_sse(self.params))
                self._connected = True

    def call_tool(self, tool_name: str, tool_args: Dict = None) -> str:
        self._ensure_connected()
        return self._run_async(self.async_client.execute(tool_name, tool_args))

    def list_tools(self) -> Any:
        self._ensure_connected()
        return self._run_async(self.async_client.list_tools())