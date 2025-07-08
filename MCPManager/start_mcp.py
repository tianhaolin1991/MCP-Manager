import os
import sys
import json
import subprocess
from typing import List, Dict, Optional

def main(config_file):

    # 检查配置文件是否存在
    if not os.path.isfile(config_file):
        print(f"配置文件 '{config_file}' 不存在。")
        sys.exit(1)

    # 读取并解析配置文件
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

    # 存储启动的进程，用于等待结束
    processes: List[subprocess.Popen] = []

    # 遍历 mcp_pool 启动服务器
    for server in mcp_pool:
        name: str = server.get('name', '未知服务器')
        url: Optional[str] = server.get('url')

        if url:
            # 存在 URL 时跳过启动命令
            print(f"服务器 '{name}' 已配置 URL: {url}，跳过运行命令。")
            continue

        # 提取 run_config 中的参数（处理数组中的第一个匹配项）
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

        # 提取工具名称（取第一个工具）
        tools: List[Dict] = server.get('tools', [])
        tool_name = tools[0].get('tool_name', '') if tools else ''
        tool_keyword = ''  # 保持原逻辑为空

        # 构建启动命令
        cmd_args = [
            'cmd.exe','/C' , 'npx', '-y', 'supergateway',
            '--stdio', f"{args or ''} {command}",
            '--port', str(port),
            '--baseUrl', f"http://localhost:{port}",
            '--ssePath', '/sse',
            '--messagePath', '/message',
            '--name', tool_name,
            '--keyword', tool_keyword
        ]

        # 清理空参数（避免影响命令执行）
        cmd_args = [arg for arg in cmd_args if arg.strip() != '']
        print(' '.join(cmd_args))
        print(f"启动服务器: {name} on port {port}")
        sub_env = os.environ.copy()
        for key,value in env.items():
            sub_env[key] = value
        print(f"env: {env}")
        try:
            # 启动进程并放入后台
            proc = subprocess.Popen(
                cmd_args,
                # 屏蔽输出（如需查看可改为 stdout=subprocess.PIPE, stderr=subprocess.PIPE）
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                env=sub_env  # 继承环境变量
            )
            processes.append(proc)
            print(f"服务器 '{name}' 已启动，PID: {proc.pid}")
        except Exception as e:
            print(f"启动服务器 '{name}' 失败: {e}")

    # 等待所有后台进程结束
    if processes:
        print("等待所有服务器进程结束...")
        for proc in processes:
            proc.wait()
        print("所有服务器进程已退出")

if __name__ == "__main__":
    main(config_file="./servers/mcp_config_gaia.json")