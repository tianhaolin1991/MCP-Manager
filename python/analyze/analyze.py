#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bean.bean import ManagerServer
from eval.tool_manager.matcher import ToolMatcher, AnalyzeResult
from tool_manager_evaluate import ToolSelectionResult
from utils.file_util import read_jsonl_file, append

results = read_jsonl_file("../data/eval/tool_manager/task/manager_grid_search_results_pass@5_2steps.jsonl", ToolSelectionResult)
BAD_CASES = [sr for sr in results if not sr.is_correct]
MANAGER_SERVER_DICT = {server.name: server for server in
                       read_jsonl_file("../data/mcp-manager/manager_servers.jsonl", ManagerServer)}

def to_markdown(index:int, ar:AnalyzeResult):
    markdown_output = f'# BAD CASE {index}\n'
    markdown_output += f"## TASK\n{ar.task}\n"
    markdown_output += f"## DETAILS\n"
    markdown_output += "| Item | TARGET | MATCHED |\n| ---- | ------ | ------- |\n"
    markdown_output += f"| SERVER | {ar.target_tool.server} | {ar.matched_tool.server} |\n"
    markdown_output += f"| TOOL | {ar.target_tool.name} | {ar.matched_tool.name} |\n"
    markdown_output += f"| DESC | {ar.target_tool.description} | {ar.matched_tool.description} |\n"
    target_params = [f"{k}: {v}" for k, v in ar.target_tool.parameter.items()]
    matched_params = [f"{k}: {v}" for k, v in ar.matched_tool.parameter.items()]
    markdown_output += f"| PARAMETERS | {'<br>'.join(target_params)} | {'<br>'.join(matched_params)} |\n"
    target_scores = f"{ar.target_score.server_score:.3f}/{ar.target_score.tool_score:.3f}/{ar.target_score.final_score:.3f}"
    matched_scores = f"{ar.matched_score.server_score:.3f}/{ar.matched_score.tool_score:.3f}/{ar.matched_score.final_score:.3f}"
    markdown_output += f"| SCORES(SERVER/TOOL/FINAL) | {target_scores} | {matched_scores} |\n"
    target_ranks = f"{ar.target_score.server_rank}/{ar.target_score.tool_rank}/{ar.target_score.final_rank}"
    matched_ranks = f"{ar.matched_score.server_rank}/{ar.matched_score.tool_rank}/{ar.matched_score.final_rank}"
    markdown_output += f"| RANKS(SERVER/TOOL/FINAL) | {target_ranks} | {matched_ranks} |\n"
    markdown_output += "## ANALYSIS\n"
    return markdown_output
    
    
if __name__ == "__main__":
    tool_matcher = ToolMatcher()
    output = "analyze.md"
    visited=set()
    for index, case in enumerate(BAD_CASES):
        server_name = case.target_server_name
        tool_name = case.target_tool_name
        id = f'{server_name}-{tool_name}'
        if id in visited:
            continue
        best_match_server = case.matched_server
        best_match_tool = case.matched_tool
        analyze_result = tool_matcher.analyze_two_steps(case.task, MANAGER_SERVER_DICT[server_name].tool(tool_name))
        md = to_markdown(index, analyze_result)
        append(output, md)
        visited.add(id)