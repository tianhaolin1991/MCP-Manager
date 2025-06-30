import json
from dataclasses import dataclass

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

    def match(self, task) -> ToolMatchResult:
        # 准备匹配结果
        # server_docs = self.server_retriever.similarity_search_with_score(mcp_server.server, filter={'domain': mcp_server.domain}, k=5)
        server_docs = self.server_retriever.similarity_search_with_relevance_scores(task, k=100)
        # 使用ToolMatcher进行分层匹配
        # 第一阶段：匹配服务器
        server_scores = []
        for server_doc, server_score in server_docs:
            server_scores.append({
                "name": server_doc.metadata['name'],
                "score": server_score,
            })

        # 按相似度降序排序
        server_scores.sort(key=lambda x: x["score"], reverse=True)
        matched_servers = {server['name']:server['score'] for server in server_scores}

        tool_docs = self.tool_retriever.similarity_search_with_relevance_scores(task, k=100)
        tool_scores = []
        for tool_doc, tool_score in tool_docs:
            tool = from_dict(ManagerTool, json.loads(tool_doc.metadata["info"]))
            # 最终得分结合服务器得分和工具得分
            # 使用与matcher.py相同的得分计算方式
            if tool.server not in matched_servers:
                continue
            server_score = matched_servers[tool.server]
            final_score = (server_score * tool_score) * max(server_score, tool_score)
            tool_scores.append({
                "server": tool.server,
                "server_score": server_score,
                "tool": tool,
                "tool_score": tool_score,
                "final_score": final_score
            })

        # 按最终得分降序排序
        tool_scores.sort(key=lambda x: x["final_score"], reverse=True)

        # 取前1个工具（与matcher.py中的top_tools保持一致）
        matched_tool = tool_scores[0]
        return ToolMatchResult(server=matched_tool['server'], tool=matched_tool['tool'],
                               score=matched_tool['final_score'])
