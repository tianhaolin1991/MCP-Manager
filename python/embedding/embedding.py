from langchain_ollama import OllamaEmbeddings

from bean.bean import ManagerServer, ManagerServerEmbeddings
from config.config import OLLAMA_URL, EMBEDDING_MODEL, EMBEDDING_CACHE_FILE, PROJECT_PATH
from utils.file_util import read_jsonl_file, append_jsonl_file


def main():
    models = ['bge-m3:567m']
    file_names = ['embedding_bge_m3']
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
            meta_data = server.meta_data
            server_descs = {}
            for domain in meta_data.domains:
                server_descs[domain] = embedding_model.embed_query(domain)
            if meta_data.product_or_platform:
                server_descs[meta_data.product_or_platform] = embedding_model.embed_query(meta_data.product_or_platform)
            for func in meta_data.functionalities:
                server_descs[func] = embedding_model.embed_query(func)
            tool_descs = {}
            for tool in server.tools:
                tool_desc = embedding_model.embed_query(tool.description)
                tool_descs[tool.description] = tool_desc
            append_jsonl_file(f"{PROJECT_PATH}//data//embedding//{file_names[i]}",
                              ManagerServerEmbeddings(name=server.name, server=server_descs, tools=tool_descs))
            print(f"EMBEDDING {i}-{j},{server.name} len({len(server_descs)})")


if __name__ == "__main__":
    main()
