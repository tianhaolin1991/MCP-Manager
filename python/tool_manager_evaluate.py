#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from dataclasses import dataclass

from langchain_core.output_parsers import PydanticOutputParser
from openai import BaseModel
from pydantic import Field
from tenacity import retry, stop_after_attempt, wait_fixed

from bean.bean import Domain, ManagerServer, ManagerTool
from eval.tool_manager.matcher import ToolMatcher
from eval.tool_manager.sampler import ToolSampler
from eval.utils import generate_grid_search_params
from utils.file_util import read_jsonl_file, dataclass_to_json, append_jsonl_file

DOMAINS = [dataclass_to_json(domain) for domain in read_jsonl_file("./data/domain/domain.jsonl", Domain)]

MANAGER_SERVER_DICT = {server.name: server for server in
                       read_jsonl_file("data/mcp-manager/manager_servers.jsonl", ManagerServer)}


class MCPServer(BaseModel):
    domain: str = Field(description="待获取的mcp server所属的领域")
    server: str = Field(description="待获取的mcp server的描述")
    tool: str = Field(description="待获取的工具能力描述")


@dataclass
class ToolSelectionResult:
    pass_at_k: int
    elapsed_time: float
    task:str
    is_correct: bool
    target_server_name: str
    target_tool_name: str
    target_server_description: str
    target_tool_description: str
    matched_server: str
    matched_tool: str
    sample_size: int
    position_index: int
    selection_method: str


parser = PydanticOutputParser(pydantic_object=MCPServer)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
def test_llm_retrieval(
        target_server: ManagerServer,
        target_tool: ManagerTool,
        pass_at_k: int,
        sample_size: int = 20,
        position_index: int = 0,
        use_random_selection: bool = False,
        two_steps:bool = True
) -> ToolSelectionResult:
    """

    Args:
        sampled_data: 采样的数据
        target_server: 目标服务器信息
        target_tool: 目标工具信息
        sample_size: 采样工具数量
        position_index: 目标工具的位置索引
        use_random_selection: 是否使用随机选择
        model_name: 模型名称

    Returns:
        (测试结果, None)
    """
    # 设置结果文件名的后缀
    if use_random_selection:
        selection_method = "random"
    else:
        selection_method = f"position_index_{position_index}"

    # 获取目标服务器和工具描述

    # 开始计时
    start_time = time.time()

    # 结束计时
    end_time = time.time()
    elapsed_time = end_time - start_time

    # 初始化工具匹配器
    matcher = ToolMatcher()

    match_results = matcher.match(target_tool.task, pass_at_k = pass_at_k, two_steps = two_steps)
    # 检查是否匹配到了目标工具
    for match_result in match_results:
        is_correct = (
                match_result.server == target_server.name and
                match_result.tool.name == target_tool.name
        )
        if is_correct:
            # 构建最终结果
            return ToolSelectionResult(pass_at_k=pass_at_k, elapsed_time=elapsed_time, #response=response.content.strip(),
                                       task = target_tool.task,
                                       target_server_name=target_server.name,
                                       target_server_description=target_server.description,
                                       target_tool_name=target_tool.name, target_tool_description=target_tool.description,
                                       matched_server=match_result.server, matched_tool=match_result.tool.name,
                                       sample_size=sample_size, position_index=position_index,
                                       selection_method=selection_method, is_correct=is_correct)
    return ToolSelectionResult(pass_at_k=pass_at_k, elapsed_time=elapsed_time,  # response=response.content.strip(),
                               task=target_tool.task,
                               target_server_name=target_server.name,
                               target_server_description=target_server.description,
                               target_tool_name=target_tool.name, target_tool_description=target_tool.description,
                               matched_server=match_results[0].server, matched_tool=match_results[0].tool.name,
                               sample_size=sample_size, position_index=position_index,
                               selection_method=selection_method, is_correct=False)

def covert_to_manager(zero_server, zero_tool):
    server = MANAGER_SERVER_DICT[zero_server.name]
    for tool in server.tools:
        if tool.name == zero_tool.name:
            return server, tool
    return None, None


def run_grid_search(
        data_path: str,
        output_dir: str,
        pass_at_k: int,
        num_position_ratios: int = 20,
        num_sample_sizes: int = 50,
        request_interval: float = 5.0,
        use_cache: bool = True,
        two_steps:bool = True
) -> None:
    """
    运行网格搜索测试

    Args:
        data_path: 数据文件路径
        output_dir: 输出目录路径
        num_position_ratios: 位置等分，实际上会多一个
        num_sample_sizes: 样本大小的数量
        request_interval: 请求间隔时间（秒）
    """
    # 生成网格搜索参数
    grid_points_list = generate_grid_search_params(num_position_ratios, num_sample_sizes)

    os.makedirs(output_dir, exist_ok=True)
    # 初始化结果列表
    all_results = []
    # 结果文件路径
    results_file = os.path.join(output_dir, f"manager_grid_search_results_pass@{pass_at_k}_${'2steps' if two_steps else '1step'}.json")
    if use_cache:
        results = read_jsonl_file(results_file, ToolSelectionResult)
        all_results.extend(results)
        # TODO--缓存
    else:
        if os.path.exists(results_file):
            os.remove(results_file)

    sampler = ToolSampler(data_path, seed=42)

    # 缓存已经采样的数据
    sampled_data_cache = {}

    for (position_index, sample_size) in grid_points_list:
        print(f"\n=== 处理样本: {position_index} / {sample_size} ===")

        # 采样工具（或从缓存获取）
        if sample_size not in sampled_data_cache:
            sampled_data = sampler.sample_tools(sample_size)
            sampled_data_cache[sample_size] = sampled_data
        else:
            sampled_data = sampled_data_cache[sample_size]

        # 选择目标工具
        manager_server, manager_tool = sampler.select_target_tool(sampled_data, position_index)
        # 测试大模型的工具检索能力
        selection_result = test_llm_retrieval(
            target_server=manager_server,
            target_tool=manager_tool,
            sample_size=sample_size,
            position_index=position_index,
            use_random_selection=False,
            pass_at_k= pass_at_k,
            two_steps = two_steps
        )

        # 添加到结果列表
        all_results.append(selection_result)
        append_jsonl_file(results_file, selection_result)

        # 打印结果
        print(f"  结果: {'✓' if selection_result.is_correct else '✗'} "
              f"耗时: {selection_result.elapsed_time:.2f}秒")
        print(f"  目标服务器: {selection_result.target_server_name}, 目标工具: {selection_result.target_tool_name}")
        print(f"  匹配的服务器: {selection_result.matched_server}, 匹配的工具: {selection_result.matched_tool}")
        print(f"  : {selection_result.task}")

        # 等待一段时间，避免请求过于频繁
        if position_index != len(grid_points_list) - 1 or sample_size != len(grid_points_list) - 1:
            print(f"  等待 {request_interval} 秒...")
            time.sleep(request_interval)

    print(f"\n=== 网格搜索完成 ===")
    print(f"总共测试了 {len(all_results)} 个配置")
    print(f"结果已保存到: {results_file}")

    # 计算正确率
    correct_count = sum(1 for result in all_results if result.is_correct)
    accuracy = correct_count / len(all_results) if all_results else 0
    print(f"总体正确率: {accuracy:.2%}")


if __name__ == "__main__":
    # 默认数据路径
    data_path = "data/mcp-manager/manager_server_with_task.jsonl"
    output_dir = "data/eval/tool_manager/task"
    for i in range(1,6):
        # 运行网格搜索
        run_grid_search(
            data_path=data_path,
            output_dir=output_dir,
            pass_at_k=i,
            num_position_ratios=20,  # 位置等分数量
            num_sample_sizes=50,  # 样本大小数量
            request_interval=1.0,  # 请求间隔2秒
            use_cache=False
        )
    for i in range(1,6):
        # 运行网格搜索
        run_grid_search(
            data_path=data_path,
            output_dir=output_dir,
            pass_at_k=i,
            num_position_ratios=20,  # 位置等分数量
            num_sample_sizes=50,  # 样本大小数量
            request_interval=1.0,  # 请求间隔2秒
            use_cache=False,
            two_steps=False
        )