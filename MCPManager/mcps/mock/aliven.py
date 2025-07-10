import logging
import random
from typing import List, Dict, Any

from mcp.server.fastmcp import FastMCP

MCP_SERVER_NAME = "mcp-aiven"

# 创建MCP服务器实例
mcp = FastMCP(
    name=MCP_SERVER_NAME,
    instructions="Navigate your Aiven projects and interact with the PostgreSQL®, Apache Kafka®, ClickHouse® and OpenSearch® services"
)

# 模拟数据 - 使用固定随机种子确保幂等性
random.seed(42)

MOCK_PROJECTS = [
    {"name": "project1", "id": "prj-12345", "created_at": "2023-01-01T12:00:00Z"},
    {"name": "project2", "id": "prj-67890", "created_at": "2023-02-15T09:30:00Z"},
    {"name": "project3", "id": "prj-54321", "created_at": "2023-03-20T16:45:00Z"}
]

SERVICE_TYPES = ["pg", "kafka", "clickhouse", "opensearch", "valkeyrie"]
SERVICE_NAMES = ["main-db", "analytics", "message-queue", "search-engine", "cache"]

# 缓存生成的服务数据以确保幂等性
SERVICE_CACHE: Dict[str, List[Dict[str, Any]]] = {}


def generate_mock_services(project_id: str) -> List[Dict[str, Any]]:
    """生成模拟服务数据（幂等实现）"""
    if project_id in SERVICE_CACHE:
        return SERVICE_CACHE[project_id]

    count = random.randint(1, 5)
    services = [
        {
            "name": f"{name}-{i + 1}",
            "service_type": random.choice(SERVICE_TYPES),
            "project": project_id,
            "state": "running",
            "cloud": "google-us-east1",
            "plan": "hobbyist",
            "created_at": "2023-04-01T10:00:00Z",
            "id": f"svc-{random.randint(10000, 99999)}"
        }
        for i, name in enumerate(random.sample(SERVICE_NAMES, count))
    ]

    SERVICE_CACHE[project_id] = services
    return services


# 工具实现
@mcp.tool(description="List all projects on your Aiven account.")
def list_projects() -> List[Dict[str, Any]]:
    """List all projects on your Aiven account."""
    return MOCK_PROJECTS


@mcp.tool(description="List all services in a specific Aiven project.")
def list_services(project_id: str) -> List[Dict[str, Any]]:
    """
    Args:
        project_id (str): id of your Aiven project
    """
    if not any(p['id'] == project_id for p in MOCK_PROJECTS):
        raise ValueError(f"Project with id '{project_id}' not found.")

    return generate_mock_services(project_id)


@mcp.tool(description="Get the detail of your service in a specific Aiven project.")
def get_service_details(project_id: str, service_name: str) -> Dict[str, Any]:
    """
    Args:
        project_id (str): id of your Aiven project
        service_name (str): name of the Aiven service
    """
    if not any(p['id'] == project_id for p in MOCK_PROJECTS):
        raise ValueError(f"Project with id '{project_id}' not found.")

    # 生成或获取缓存的服务列表
    services = generate_mock_services(project_id)

    # 查找服务
    service = next((s for s in services if s['name'] == service_name), None)
    if not service:
        raise ValueError(f"Service with name '{service_name}' not found in project '{project_id}'.")

    # 缓存详细信息以确保幂等性
    if 'connection_info' not in service:
        # 添加详细配置信息
        if service['service_type'] == 'pg':
            service['connection_info'] = {
                "host": f"{service_name}.aivencloud.com",
                "port": 12345,
                "database": "defaultdb",
                "username": "avnadmin",
                "password": "********",
                "uri": "postgres://avnadmin:********@pg-aiven.aivencloud.com:12345/defaultdb?sslmode=require"
            }
        elif service['service_type'] == 'kafka':
            service['connection_info'] = {
                "bootstrap_servers": [f"{service_name}-kafka.aivencloud.com:12345"],
                "schema_registry": f"https://{service_name}-sr.aivencloud.com:12346",
                "username": "avnadmin",
                "password": "********",
                "topics": ["users", "orders", "events"]
            }

    return service


if __name__ == "__main__":
    mcp.run()
