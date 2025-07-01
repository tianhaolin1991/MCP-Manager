#!/usr/bin/env python
# -*- coding: utf-8 -*-
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from bean.bean import ManagerServer, ManagerTool
from config.config import MODEL_NAME, API_KEY, BASE_URL
from eval.tool_manager.matcher import ToolMatcher, AnalyzeResult
from tool_manager_evaluate import ToolSelectionResult
from utils.file_util import read_jsonl_file, append

results = read_jsonl_file("../data/eval/tool_manager/task/manager_grid_search_results_pass@5_2steps.jsonl",
                          ToolSelectionResult)
BAD_CASES = [sr for sr in results if not sr.is_correct]
MANAGER_SERVER_DICT = {server.name: server for server in
                       read_jsonl_file("../data/mcp-manager/manager_servers.jsonl", ManagerServer)}
JUDGE_PROMPT = """Decide Which Tool Can Solve The Problem Below Better
# Problem
{problem}
# Tools
{tool_1}
{tool_2}
# Answer
Just output Id of the better tool
"""


def format_tool(id: int, tool: ManagerTool):
    return f"""{{
    \"id\": {id},
    \"name\": \"{tool.name}\",
    \"description\": \"{tool.description}\",
    \"parameters\": {tool.parameter}
}}"""


def to_markdown(index: int, ar: AnalyzeResult, chat_model: ChatOpenAI):
    markdown_output = f'# BAD CASE {index}\n'
    markdown_output += f"## TASK\n{ar.task}\n"
    markdown_output += f"## DETAILS\n"
    markdown_output += "| Item | GROUND TRUTH | SEARCH RESULT |\n| ---- | ------ | ------- |\n"
    markdown_output += f"| SERVER | {ar.target_tool.server} | {ar.matched_tool.server} |\n"
    markdown_output += f"| TOOL | {ar.target_tool.name} | {ar.matched_tool.name} |\n"
    markdown_output += f"| S_DESC | {ar.target_server_desc} | {ar.matched_server_desc} |\n"
    markdown_output += f"| T_DESC | {ar.target_tool.description} | {ar.matched_tool.description} |\n"
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
    if ar.target_score.server_rank == ar.matched_score.server_rank:
        server_score = 'EQUAL'
    elif ar.target_score.server_rank > ar.matched_score.server_rank:
        server_score = 'LOWER'
    else:
        server_score = 'HIGHER'
    #judge_res = chat_model.invoke([SystemMessage(
    #    content=JUDGE_PROMPT.format(problem=ar.task, tool_1=format_tool(1, ar.target_tool),
    #                                tool_2=format_tool(2, ar.matched_tool)))]).content
    judge_res = "1"
    print(f"judge_res{judge_res}")
    markdown_output += f"- SERVER_SCORE: {server_score} \n"
    markdown_output += f"- MATCH: NONE \n"
    markdown_output += f"- AI_JUDGE: {'GROUND TRUTH' if judge_res.lower() == '1' else 'SEARCH RESULT'}\n"
    markdown_output += f"- NOTE: NONE \n"
    return markdown_output


if __name__ == "__main__":
    tool_matcher = ToolMatcher()
    chat_model = ChatOpenAI(model=MODEL_NAME, api_key=API_KEY, base_url=BASE_URL)
    output = "analyze.md"
    visited = set()
    append(output, """# Analyze
- SERVER_SCORE: LOWER/HIGHER/EQUAL 使用二阶段检索是否副作用
- MATCH: Task和Ground Truth的匹配度 HIGHT/LOW
- AI_JUDGE: AI判断哪个工具更好
- NOTE: 备注\n""")
    for index, case in enumerate(BAD_CASES):
        server_name = case.target_server_name
        tool_name = case.target_tool_name
        id = f'{server_name}-{tool_name}'
        if id in visited:
            continue
        analyze_result = tool_matcher.analyze_two_steps(case.task, MANAGER_SERVER_DICT[server_name].tool(tool_name))
        analyze_result.target_server_desc = MANAGER_SERVER_DICT[server_name].description
        analyze_result.matched_server_desc = MANAGER_SERVER_DICT[analyze_result.matched_tool.server].description
        md = to_markdown(index, analyze_result, chat_model)
        append(output, md)
        visited.add(id)
