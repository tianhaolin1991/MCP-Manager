from langchain_ollama import OllamaEmbeddings

from bean.bean import ManagerServer, ManagerServerEmbeddings
from config.config import OLLAMA_URL, EMBEDDING_MODEL, EMBEDDING_CACHE_FILE, PROJECT_PATH
from utils.file_util import read_jsonl_file, append_jsonl_file


def main():
    models = ['dengcao/Qwen3-Embedding-4B:Q5_K_M', 'dengcao/Qwen3-Embedding-0.6B:F16', 'bge-m3:567m']
    file_names = ['embedding_qwen3_4b', 'embedding_qwen3_0.6b', 'embedding_bge_m3']
    servers = read_jsonl_file(f'{PROJECT_PATH}/data/mcp-manager/manager_servers.jsonl', ManagerServer)
    for i in range(len(models)):
        embedding_model = OllamaEmbeddings(
            base_url=OLLAMA_URL,  # Ollama服务地址
            model=models[i]
        )
        cached_list = read_jsonl_file(f"{PROJECT_PATH}//data//embedding//{file_names[i]}", ManagerServerEmbeddings)
        print(f"c length: {len(cached_list)}")
        for j, server in enumerate(servers):
            if j < len(cached_list):
                continue
            server_desc = embedding_model.embed_query(server.description)
            tool_descs = []
            for tool in server.tools:
                tool_desc = embedding_model.embed_query(tool.description)
                tool_descs.append(tool_desc)
            append_jsonl_file(f"{PROJECT_PATH}//data//embedding//{file_names[i]}",
                              ManagerServerEmbeddings(name=server.name, server=server_desc, tools=tool_descs))
            print(f"EMBEDDING {i}-{j},{server.name} len({len(server_desc)})")


if __name__ == "__main__":
    main()
