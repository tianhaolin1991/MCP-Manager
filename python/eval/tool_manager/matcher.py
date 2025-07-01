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


@dataclass
class Score:
    server_score: float
    server_rank: int
    tool_score: float
    tool_rank: int
    final_score: float
    final_rank: int


@dataclass
class AnalyzeResult:
    task: str
    target_tool: ManagerTool
    target_score: Score
    matched_tool: ManagerTool
    matched_score: Score


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

    def match(self, task, pass_at_k: int = 5, two_steps: bool = True) -> List[ToolMatchResult]:
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
                server_score = matched_servers[tool.server]['score']
                final_score = (server_score * tool_score) * max(server_score, tool_score)
                server_rank = matched_servers[tool.server]['rank']
            else:
                server_score = 0.0
                final_score = tool_score
                server_rank = 0
            tool_scores.append({
                "server": tool.server,
                "server_score": server_score,
                "tool": tool,
                "tool_score": tool_score,
                "final_score": final_score,
                "server_rank": server_rank,
                "tool_rank": tool_rank + 1
            })

        # 按最终得分降序排序
        tool_scores.sort(key=lambda x: x["final_score"], reverse=True)

        # 取前1个工具（与matcher.py中的top_tools保持一致）
        matched_tools = tool_scores[:pass_at_k]
        return [ToolMatchResult(server=matched_tool['server'], tool=matched_tool['tool'],
                                score=matched_tool['final_score']) for matched_tool in matched_tools]

    def analyze_two_steps(self, task: str, target: ManagerTool) -> AnalyzeResult:
        # 准备匹配结果
        # server_docs = self.server_retriever.similarity_search_with_score(mcp_server.server, filter={'domain': mcp_server.domain}, k=5)
        server_docs = self.server_retriever.similarity_search_with_relevance_scores(task, k=1000)
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
        tool_docs = self.tool_retriever.similarity_search_with_relevance_scores(task, k=1000)
        tool_scores = []
        for tool_rank, (tool_doc, tool_score) in enumerate(tool_docs):
            tool = from_dict(ManagerTool, json.loads(tool_doc.metadata["info"]))
            if (tool.server not in matched_servers):
                continue
            server_score = matched_servers[tool.server]['score']
            final_score = (server_score * tool_score) * max(server_score, tool_score)
            tool_scores.append({
                "server": tool.server,
                "server_score": server_score,
                "tool": tool,
                "tool_score": tool_score,
                "final_score": final_score,
                "server_rank": matched_servers[tool.server]['rank'],
                "tool_rank": tool_rank + 1,
            })

        # 按最终得分降序排序
        tool_scores.sort(key=lambda x: x["final_score"], reverse=True)
        target_final_rank = -1
        for final_rank, final_score in enumerate(tool_scores):
            if final_score["server"] == target.server and final_score["tool"].name == target.name:
                target_final_rank = final_rank + 1
                break
        if target_final_rank == -1:
            target_score = Score(server_score=0.0, tool_score=0.0,
                                 final_score=0.0,
                                 server_rank=-1, tool_rank=-1,
                                 final_rank=-1)
        else:
            target_result = tool_scores[target_final_rank - 1]
            target_score = Score(server_score=target_result["server_score"], tool_score=target_result["tool_score"],
                                 final_score=target_result['final_score'],
                                 server_rank=target_result['server_rank'], tool_rank=target_result['tool_rank'],
                                 final_rank=target_final_rank)
        matched_result = tool_scores[0]
        matched_score = Score(server_score=matched_result["server_score"], tool_score=matched_result["tool_score"],
                              final_score=matched_result['final_score'],
                              server_rank=matched_result['server_rank'], tool_rank=matched_result['tool_rank'],
                              final_rank=1)
        return AnalyzeResult(task=task, target_tool=target, matched_tool=tool_scores[0]['tool'],
                             target_score=target_score, matched_score=matched_score)
