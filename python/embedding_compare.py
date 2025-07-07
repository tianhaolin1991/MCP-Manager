import os
from dataclasses import dataclass
from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document

from bean.bean import ManagerServer
from build_index import CachedEmbeddings
from config.config import PROJECT_PATH, DB_TYPE
from tool_manager_evaluate import run_grid_search, ToolSelectionResult
from utils.file_util import read_jsonl_file, dataclass_to_json, append_jsonl_file

models = ['bge-m3:567m']
names = ['embedding_bge_m3']
embedding_path = f'{PROJECT_PATH}//data//embedding'


@dataclass
class EmbeddingSearchResult:
    embedding_model: str
    score: float
    rank: float
    hit: bool


@dataclass
class EmbeddingCompareResult:
    server: str
    tool: str
    res: List[EmbeddingSearchResult]


def chroma_build_index(embedding_cache, chroma_persist, mcp_servers):
    embedding_function = CachedEmbeddings(cache_file=embedding_cache)
    tool_docs = []
    for server in mcp_servers:
        for tool in server.tools:
            tool_docs.append(
                Document(page_content=tool.description, metadata={'name': tool.name, "server": server.name,
                                                                  "info": dataclass_to_json(tool)}))
    Chroma.from_documents(tool_docs, collection_name='tool', embedding=embedding_function,
                          persist_directory=chroma_persist,
                          collection_metadata={"hnsw:space": "cosine"})


def main(type: str,two_steps:bool,pass_at_k=5):
    compare_output_dir = f'{PROJECT_PATH}//data//eval//embedding_compare'
    server_path = f"{PROJECT_PATH}//data//mcp-manager//manager_server_with_task_hard.jsonl"
    mcp_servers = read_jsonl_file(server_path, ManagerServer)
    for i, embedding_model in enumerate(models):
        chroma_persist = f'{PROJECT_PATH}//{DB_TYPE}'
        embedding_cache = f'{embedding_path}//{names[i]}.jsnol'
        if not os.path.exists(chroma_persist):
            chroma_build_index(embedding_cache, chroma_persist, mcp_servers)
        output_path = f"{compare_output_dir}//{type}//{names[i]}_results.jsonl"
        run_grid_search(
            data_path=server_path,
            output_path=output_path,
            pass_at_k=pass_at_k,
            num_position_ratios=2656,  # 位置等分数量
            num_sample_sizes=2656,  # 样本大小数量
            request_interval=1.0,  # 请求间隔2秒
            use_cache=True,
            two_steps=two_steps,
            embedding_model=models[i],
            persist_directory=chroma_persist,
            last_grid_only=True,
        )
    final_result_dict = {}
    for i, name in enumerate(names):
        srs = read_jsonl_file(
            f"{compare_output_dir}//{type}//{name}_results.jsonl",
            ToolSelectionResult)
        for sr in srs:
            name = f'{sr.target_server.name}-{sr.target_tool.name}'
            cr = final_result_dict.get(name, EmbeddingCompareResult(server=sr.target_server.name,
                                                                    tool=sr.target_tool.name, res=[]))
            if sr.is_correct:
                cr.res.append(EmbeddingSearchResult(embedding_model=models[i], rank=sr.pass_at_k,
                                                    score=sr.match_result.score, hit=True))
            else:
                cr.res.append(EmbeddingSearchResult(embedding_model=models[i], rank=-1, score=-1, hit=False))
            final_result_dict[name] = cr
    for key, value in final_result_dict.items():
        append_jsonl_file(f'{compare_output_dir}//{type}//compare_result.jsonl', value)
    crs = read_jsonl_file(f'{compare_output_dir}//{type}//compare_result.jsonl', EmbeddingCompareResult)
    mis_match = {embedding_model: 0 for embedding_model in models}
    total = len(crs)
    rank_total = {embedding_model: 0 for embedding_model in models}
    score_total = {embedding_model: 0 for embedding_model in models}
    for cr in crs:
        for res in cr.res:
            model = res.embedding_model
            rank = res.rank
            score = res.score
            hit = res.hit
            if hit:
                rank_total[model] += rank
                score_total[model] += score
            else:
                mis_match[model] += 1
    for model in models:
        cunt = total - mis_match[model]
        average_rank = rank_total[model] / cunt
        average_score = score_total[model] / cunt
        print(f"model-{model}, avg_rank-{average_rank}, avg_score-{average_score}, mismatch:{mis_match[model]}")


if __name__ == "__main__":
    main(type="2steps", two_steps=True, pass_at_k=1)
    main(type="1step", two_steps=False, pass_at_k=1)
