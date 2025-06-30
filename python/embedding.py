from langchain_ollama import OllamaEmbeddings

from bean.bean import ManagerServer,ManagerServerEmbeddings
from utils.file_util import read_jsonl_file, append_jsonl_file


def main():
    embedding_model = OllamaEmbeddings(
        base_url="http://119.3.125.66:11434",  # Ollama服务地址
        #model="dengcao/Qwen3-Embedding-4B:Q5_K_M"
        model="bge-m3:567m"
    )
    servers = read_jsonl_file('data/mcp-manager/manager_servers.jsonl', ManagerServer)
    for server in servers:
        server_desc = embedding_model.embed_query(server.description)
        tool_descs = []
        for tool in server.tools:
            tool_desc = embedding_model.embed_query(tool.description)
            tool_descs.append(tool_desc)
        append_jsonl_file('data/mcp-manager/embedding.jsonl', ManagerServerEmbeddings(name=server.name, server=server_desc, tools=tool_descs))

if __name__ == "__main__":
    main()