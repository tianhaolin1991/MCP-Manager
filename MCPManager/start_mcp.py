import os
import sys
import json
import subprocess
import time
import socket
import threading
from typing import List, Dict, Optional


def check_port(port: int, timeout: int = 10) -> bool:
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(("localhost", port), timeout=1) as sock:
                return True
        except (ConnectionRefusedError, OSError):
            time.sleep(0.5)  # 等待后重试
    return False


def log_watcher(proc: subprocess.Popen, name: str, prefix: str):
    if proc.stdout:
        for line in iter(proc.stdout.readline, ''):
            print(f"[{name}][{prefix}] {line.strip()}")
    if proc.stderr:
        for line in iter(proc.stderr.readline, ''):
            print(f"[{name}][{prefix}][ERROR] {line.strip()}")


def main(config_file):
    if not os.path.isfile(config_file):
        print(f"配置文件 '{config_file}' 不存在。")
        sys.exit(1)

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        print(f"配置文件解析错误: {e}")
        sys.exit(1)

    # 检查 mcp_pool 字段
    mcp_pool: List[Dict] = config.get('mcp_pool', [])
    if not mcp_pool:
        print("mcp_pool 中未定义服务器。")
        sys.exit(1)

    # 存储启动的进程和相关信息
    server_processes = []

    # 遍历 mcp_pool 启动服务器
    for server in mcp_pool:
        name: str = server.get('name', '未知服务器')
        url: Optional[str] = server.get('url')

        if url:
            # 存在 URL 时跳过启动命令
            print(f"服务器 '{name}' 已配置 URL: {url}，跳过运行命令。")
            continue

        # 提取 run_config 中的参数
        run_configs: List[Dict] = server.get('run_config', [])
        command = None
        args = None
        port = None
        env = {}

        for rc in run_configs:
            if not command:
                command = rc.get('command')
            if not args:
                args = rc.get('args')
            if not port:
                port = rc.get('port')
            if not env:
                env = rc.get('env', {})

        # 校验必要参数
        if not all([command, port]):
            print(f"服务器 '{name}' 配置不完整（缺少 command 或 port），跳过启动。")
            continue

        # 提取工具名称
        tools: List[Dict] = server.get('tools', [])
        tool_name = tools[0].get('tool_name', '') if tools else ''
        tool_keyword = ''

        # 构建启动命令
        cmd_args = [
            'cmd.exe', '/C', 'npx', '-y', 'supergateway',
            '--stdio', f"{args or ''} {command}",
            '--port', str(port),
            '--baseUrl', f"http://localhost:{port}",
            '--ssePath', '/sse',
            '--messagePath', '/message',
            '--name', tool_name,
            '--keyword', tool_keyword
        ]

        # 清理空参数
        cmd_args = [arg for arg in cmd_args if arg.strip() != '']
        print(f"启动命令: {' '.join(cmd_args)}")
        print(f"启动服务器: {name} on port {port}")

        # 配置环境变量
        sub_env = os.environ.copy()
        for key, value in env.items():
            sub_env[key] = value
        print(f"环境变量: {env}")

        try:
            # 启动进程并捕获输出
            proc = subprocess.Popen(
                cmd_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=sub_env,
                bufsize=1,
                universal_newlines=True
            )

            # 启动日志监控线程
            stdout_thread = threading.Thread(target=log_watcher, args=(proc, name, "STDOUT"))
            stderr_thread = threading.Thread(target=log_watcher, args=(proc, name, "STDERR"))
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            stdout_thread.start()
            stderr_thread.start()

            # 检查端口是否可访问
            print(f"正在检查端口 {port} 是否可访问...")
            if check_port(port):
                print(f"服务器 '{name}' 已成功启动并监听端口 {port}")
            else:
                print(f"警告: 服务器 '{name}' 启动后端口 {port} 无法访问")

            server_processes.append({
                'name': name,
                'process': proc,
                'port': port,
                'threads': [stdout_thread, stderr_thread]
            })
            print(f"服务器 '{name}' 已启动，PID: {proc.pid}")

        except Exception as e:
            print(f"启动服务器 '{name}' 失败: {e}")

    # 等待所有后台进程结束
    if server_processes:
        print("按 Ctrl+C 停止所有服务器...")
        try:
            for info in server_processes:
                info['process'].wait()
        except KeyboardInterrupt:
            print("\n接收到停止信号，正在关闭所有服务器...")
            for info in server_processes:
                if info['process'].poll() is None:  # 进程仍在运行
                    info['process'].terminate()
                    try:
                        info['process'].wait(timeout=5)
                        print(f"服务器 '{info['name']}' 已成功关闭")
                    except subprocess.TimeoutExpired:
                        info['process'].kill()
                        print(f"服务器 '{info['name']}' 已强制终止")
        finally:
            print("所有服务器进程已退出")


if __name__ == "__main__":
    config_file = "./servers/mcp_config_gaia.json"
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    main(config_file)