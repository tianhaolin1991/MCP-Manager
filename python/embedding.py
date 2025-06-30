from langchain_ollama import OllamaEmbeddings

from bean.bean import ManagerServer,ManagerServerEmbeddings
from config.config import OLLAMA_URL, EMBEDDING_MODEL
from utils.file_util import read_jsonl_file, append_jsonl_file


def main():
    embedding_model = OllamaEmbeddings(
        base_url=OLLAMA_URL,  # Ollama服务地址
        model=EMBEDDING_MODEL
    )
    servers = read_jsonl_file('data/mcp-manager/manager_servers.jsonl', ManagerServer)
    for server in servers:
        server_desc = embedding_model.embed_query(server.description)
        tool_descs = []
        for tool in server.tools:
            tool_desc = embedding_model.embed_query(tool.description)
            tool_descs.append(tool_desc)
        append_jsonl_file('data/mcp-manager/embedding_qwen3_0.6b.jsonl', ManagerServerEmbeddings(name=server.name, server=server_desc, tools=tool_descs))

if __name__ == "__main__":
    main()