from langchain_community.vectorstores import FAISS, DistanceStrategy
from langchain_core.embeddings import Embeddings
from bean.bean import ManagerServer, ManagerServerEmbeddings
from config.config import PROJECT_PATH, DB_TYPE, EMBEDDING_CACHE_FILE
from utils.file_util import read_jsonl_file, dataclass_to_json
from langchain_chroma import Chroma
from langchain_core.documents import Document

ALL_MANAGER_SERVERS = read_jsonl_file('data/mcp-manager/manager_servers_old.jsonl', ManagerServer)


class CachedEmbeddings(Embeddings):
    def __init__(self, cache_file = EMBEDDING_CACHE_FILE):
        servers = ALL_MANAGER_SERVERS
        embeddings = read_jsonl_file(cache_file, ManagerServerEmbeddings)
        name_to_embeddings = {embedding.name: embedding for embedding in embeddings}
        self.embedding_dict = {}
        for server in servers:
            server_embedding = name_to_embeddings[server.name]
            # self.embedding_dict[server.description] = server_embedding.server
            tool_embeddings = server_embedding.tools
            for i, tool in enumerate(server.tools):
                tool_embedding = tool_embeddings[i]
                self.embedding_dict[tool.description] = tool_embedding

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [self.embedding_dict[text] for text in texts]

    def embed_query(self, text: str) -> list[float]:
        pass

    async def aembed_documents(self, texts: list[str]) -> list[list[float]]:
        pass

    async def aembed_query(self, text: str) -> list[float]:
        pass


def main():
    mcp_servers = ALL_MANAGER_SERVERS
    embedding_function = CachedEmbeddings()
    server_docs = []
    tool_docs = []
    for server in mcp_servers:
        doc = Document(page_content=server.description,
                       metadata={'name': server.name, 'domains': ",".join([domain.name for domain in server.domains])})
        server_docs.append(doc)
        for tool in server.tools:
            tool_docs.append(Document(page_content=tool.description, metadata={'name': tool.name, "server": server.name,
                                                                               "info": dataclass_to_json(tool)}))
    if DB_TYPE == "chroma":
        Chroma.from_documents(server_docs, collection_name='server', embedding=embedding_function,
                              persist_directory=f'{PROJECT_PATH}//{DB_TYPE}',
                              collection_metadata={"hnsw:space": "cosine"})
        Chroma.from_documents(tool_docs, collection_name='tool', embedding=embedding_function,
                              persist_directory=f'{PROJECT_PATH}//{DB_TYPE}',
                              collection_metadata={"hnsw:space": "cosine"})
    else:
        server_rdb = FAISS.from_documents(server_docs, embedding=embedding_function,
                                          distance_strategy=DistanceStrategy.COSINE)
        server_rdb.save_local(f'{PROJECT_PATH}//{DB_TYPE}//server')
        tool_rdb = FAISS.from_documents(tool_docs, embedding=embedding_function,
                                        distance_strategy=DistanceStrategy.COSINE)
        tool_rdb.save_local(f'{PROJECT_PATH}//{DB_TYPE}//tool')


if __name__ == "__main__":
    main()
