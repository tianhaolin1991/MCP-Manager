import json
from dataclasses import dataclass

import numpy as np
import re
import time
from typing import List, Dict, Any, Tuple, Optional
import openai
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from bean.bean import ManagerTool
from config.config import PROJECT_PATH
from utils.file_util import from_dict


@dataclass
class ToolMatchResult:
    server: str
    tool: ManagerTool
    score: float


class ToolMatcher:
    def __init__(self, embedding_model: str = "bge-m3:567m"):
        """
        Setup the tool matcher

        Args:
            embedding_model: The name of the embedding model
            top_servers: The number of servers in the first stage
            top_tools: The number of tools to return
        """
        self.embedding_model = OllamaEmbeddings(
            base_url="http://119.3.125.66:11434",  # Ollama服务地址
            model=embedding_model
        )
        self.server_retriever = Chroma(collection_name='server', persist_directory=f'{PROJECT_PATH}//chroma',
                                       embedding_function=self.embedding_model)
        self.tool_retriever = Chroma(collection_name='tool', persist_directory=f'{PROJECT_PATH}//chroma',
                                     embedding_function=self.embedding_model)

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

    def match(self, mcp_server) -> ToolMatchResult:
        # 准备匹配结果
        # server_docs = self.server_retriever.similarity_search_with_score(mcp_server.server, filter={'domain': mcp_server.domain}, k=5)
        server_docs = self.server_retriever.similarity_search_with_score(mcp_server.server, k=20)
        # 使用ToolMatcher进行分层匹配
        # 第一阶段：匹配服务器
        server_scores = []
        for server_doc, server_score in server_docs:
            server_scores.append({
                "name": server_doc.metadata['name'],
                "score": 1 / (1 + server_score),
            })

        # 按相似度降序排序
        server_scores.sort(key=lambda x: x["score"], reverse=True)

        matched_servers = server_scores

        tool_scores = []
        for server_info in matched_servers:
            server_name = server_info["name"]
            server_score = server_info["score"]
            tool_docs = self.tool_retriever.similarity_search_with_score(mcp_server.server,
                                                                         filter={'server': server_name}, k=5)
            for tool_doc, tool_score in tool_docs:
                tool = from_dict(ManagerTool, json.loads(tool_doc.metadata["info"]))
                tool_score = 1 / (1 + tool_score)
                # 最终得分结合服务器得分和工具得分
                # 使用与matcher.py相同的得分计算方式
                final_score = (server_score * tool_score) * max(server_score, tool_score)
                tool_scores.append({
                    "server_name": server_name,
                    "server_score": server_score,
                    "tool": tool,
                    "tool_score": tool_score,
                    "final_score": final_score
                })

        # 按最终得分降序排序
        tool_scores.sort(key=lambda x: x["final_score"], reverse=True)

        # 取前1个工具（与matcher.py中的top_tools保持一致）
        matched_tool = tool_scores[0]
        return ToolMatchResult(server=matched_tool['server_name'], tool=matched_tool['tool'],
                               score=matched_tool['final_score'])
