import json
from dataclasses import dataclass
from typing import List

from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_ollama import OllamaEmbeddings

from bean.bean import ManagerTool
from config.config import PROJECT_PATH, EMBEDDING_MODEL, OLLAMA_URL, DB_TYPE
from utils.file_util import from_dict


@dataclass
class ToolMatchResult:
    server: str
    tool: ManagerTool
    score: float


class ToolMatcher:
    def __init__(self):
        self.embedding_model = OllamaEmbeddings(
            base_url=OLLAMA_URL,
            model=EMBEDDING_MODEL
        )
        if DB_TYPE == 'chroma':
            self.server_retriever = Chroma(collection_name='server', persist_directory=f'{PROJECT_PATH}//chroma',
                                           embedding_function=self.embedding_model,
                                           collection_metadata={"hnsw:space": "cosine"})
            self.tool_retriever = Chroma(collection_name='tool', persist_directory=f'{PROJECT_PATH}//chroma',
                                         embedding_function=self.embedding_model,
                                         collection_metadata={"hnsw:space": "cosine"})
        else:
            self.server_retriever = FAISS.load_local(f'{PROJECT_PATH}//{DB_TYPE}//server',
                                                     embeddings=self.embedding_model,
                                                     distance_strategy=DistanceStrategy.COSINE,
                                                     allow_dangerous_deserialization=True)
            self.tool_retriever = FAISS.load_local(f'{PROJECT_PATH}//{DB_TYPE}//tool', embeddings=self.embedding_model,
                                                   distance_strategy=DistanceStrategy.COSINE,
                                                   allow_dangerous_deserialization=True)

    def load_data(self, data_path: str) -> None:
        """
        Load the tool data

        Args:
            data_path: The path to the JSON file containing the tool embeddings
        """
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                self.servers_data = json.load(f)
            print(f"Loaded {len(self.servers_data)} servers from {data_path}")
        except Exception as e:
            raise ValueError(f"Error loading tool data: {e}")

    def match(self, task, pass_at_k: int = 1, two_steps:bool = True) -> List[ToolMatchResult]:
        # 准备匹配结果
        # server_docs = self.server_retriever.similarity_search_with_score(mcp_server.server, filter={'domain': mcp_server.domain}, k=5)
        if two_steps:
            server_docs = self.server_retriever.similarity_search_with_relevance_scores(task, k=100)
        else:
            server_docs = []
        # 使用ToolMatcher进行分层匹配
        # 第一阶段：匹配服务器
        server_scores = []
        for rank, (server_doc, server_score) in enumerate(server_docs):
            server_scores.append({
                "name": server_doc.metadata['name'],
                "score": server_score,
                "rank": rank + 1,
            })

        matched_servers = {server['name']: server for server in server_scores}

        tool_docs = self.tool_retriever.similarity_search_with_relevance_scores(task, k=100)
        tool_scores = []
        for tool_rank, (tool_doc, tool_score) in enumerate(tool_docs):
            tool = from_dict(ManagerTool, json.loads(tool_doc.metadata["info"]))
            # 最终得分结合服务器得分和工具得分
            # 使用与matcher.py相同的得分计算方式
            if two_steps and (tool.server not in matched_servers):
                continue
            if two_steps:
                server_rank = matched_servers[tool.server]['rank'] if two_steps else 1
                final_rank = 1 / server_rank + 1 / (tool_rank + 1)
            else:
                server_rank = 1
                final_rank = 1 / (tool_rank + 1)
            tool_scores.append({
                "server": tool.server,
                "server_rank": server_rank,
                "tool": tool,
                "tool_rank": tool_rank,
                "final_rank": final_rank
            })

        # 按最终得分降序排序
        tool_scores.sort(key=lambda x: x["final_rank"], reverse=True)

        # 取前1个工具（与matcher.py中的top_tools保持一致）
        matched_tools = tool_scores[:pass_at_k]
        return [ToolMatchResult(server=matched_tool['server'], tool=matched_tool['tool'],
                               score=matched_tool['final_rank']) for matched_tool in matched_tools]
