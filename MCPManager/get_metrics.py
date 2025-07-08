import json
import re
import os
import argparse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openai as oai


with open('configs\mcp_config_math.json', 'r', encoding='utf-8') as file:
    math_mcps = json.load(file)['mcp_pool']
math_toollist = []
for item in math_mcps:
    math_toollist += item['tools']
math_toollist = str(math_toollist)

with open('configs\mcp_config_gaia.json', 'r', encoding='utf-8') as file:
    gaia_mcps = json.load(file)['mcp_pool']
gaia_toollist = []
for item in gaia_mcps:
    gaia_toollist += item['tools']
gaia_toollist = str(gaia_toollist)

with open('configs\mcp_config_code.json', 'r', encoding='utf-8') as file:
    code_mcps = json.load(file)['mcp_pool']
code_toollist = []
for item in code_mcps:
    code_toollist += item['tools']
code_toollist = str(code_toollist)



SYSTEM_PROMPT = """
You are an assistant who is good at calling on tools. The following tools are currently available:{mcptools}.

Given the following question, answer with the tool call stack, indicate whether the answer error is related to the tool call, and if so give the location of the first tool call that went wrong (the location of the occurrence divided by the total number of occurrences, e.g., if the second of the three calls went wrong, it would be (2-1)/3=0.33, or 1.0 if it is not related), and indicate the percentage of tool calls that went wrong. The return format is:
"fail_by_tool": bool,
"first_wrong_tool_call": float,
"total_wrong_tool_calls": float,
"""

def build_message(toollist,content):
    message=[
      {
        "role": "system",
        "content": [
          {
            "type": "text",
            "text": SYSTEM_PROMPT.format(mcptools=toollist)
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "{content}".format(content=content)
          }
        ]
      },
    ]
    return message

client = oai.OpenAI(
  base_url=[YOUR_URL],
  api_key=[YOUR_KEY],
)


def get_metrics(data, toollist):
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_total_tokens = 0
    count = 0
    # Process tool usage
    tool_usage_count = 0
    tool_usage_success_count = 0
    tool_call_details = []
    wrong_tool_ratio = 0
    wrong_tool_depth = 0

    pattern = r'"first_wrong_tool_call":\s*(\d+\.?\d*).*?"total_wrong_tool_calls":\s*(\d+\.?\d*)'
    for item in data:
        if 'token_usage' in item:
            token_usage = item['token_usage']
            total_prompt_tokens += token_usage.get('prompt_tokens', 0)
            total_completion_tokens += token_usage.get('completion_tokens', 0)
            total_total_tokens += token_usage.get('total_tokens', 0)
            count += 1
        if 'tool_usage' in item and item['tool_usage'] and 'tool_calls' in item['tool_usage']:
            tool_calls = item['tool_usage']['tool_calls']
            if tool_calls:
                tool_usage_count += 1
                if item.get('success', True):
                    tool_usage_success_count += 1
                    wrong_tool_depth += 1
                else:
                    print(item)
                    completion = client.chat.completions.create(
                        model="anthropic/claude-3.7-sonnet",
                        messages=build_message(toollist, item),
                    )
                    print(completion.choices[0].message.content)
                    match = re.search(pattern, completion.choices[0].message.content, re.DOTALL)
                    if match:
                        wrong_tool_depth += float(match.group(1))
                        wrong_tool_ratio += float(match.group(2))
                    else:
                        print("Can't found matched item")
                    
                # tool_call_details.append({
                #     'unique_id': item.get('unique_id', 'N/A'),
                #     'question': item.get('question', 'N/A'),
                #     'ground_truth': item.get('ground_truth', 'N/A'),
                #     'prediction': item.get('prediction', 'N/A'),
                #     'success': item.get('success', None),
                #     'tool_calls': tool_calls
                # })        
    if count > 0:
        avg_prompt_tokens = total_prompt_tokens / count
        avg_completion_tokens = total_completion_tokens / count
        avg_total_tokens = total_total_tokens / count
        
        print(f"Problem number: {count}")
        print(f"Avg prompt_tokens: {avg_prompt_tokens:.2f}")
        print(f"Avg completion_tokens: {avg_completion_tokens:.2f}")
        print(f"Avg total_tokens: {avg_total_tokens:.2f}")
        RA = tool_usage_success_count / tool_usage_count if tool_usage_count > 0 else 0
        TFTD = wrong_tool_depth / tool_usage_count if tool_usage_count > 0 else 0    # Task Fault Tolerance Depth
        DTSR = (1 - wrong_tool_ratio / tool_usage_count) if tool_usage_count > 0 else 0    # Dialogue Turn Success Rate
        print(f"\nThere are {tool_usage_count} problems in the dataset that used tools.")
        print(f"Accuracy rate of problems using tools: {RA:.2%}" if tool_usage_count > 0 else "没有使用工具的问题")
        print(f"TFTD : {TFTD:.2f}")
        print(f"DTSR: {DTSR:.2f}")
    else:
        print("No valid problem found.")
    
    return avg_total_tokens, RA, TFTD, DTSR
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate metrics from a JSON file.")
    parser.add_argument("file_path", type=str, help="Path to the JSON results file.")
    parser.add_argument("--toollist_type", type=str, choices=["math", "gaia", "code"], default="gaia",
                        help="Type of toollist to use (math, gaia, or code). Default is gaia.")
    
    args = parser.parse_args()

    # 根据选择的toollist_type设置toollist
    if args.toollist_type == "math":
        selected_toollist = math_toollist
    elif args.toollist_type == "gaia":
        selected_toollist = gaia_toollist
    elif args.toollist_type == "code":
        selected_toollist = code_toollist
    else:
        # 默认情况，或者可以抛出错误
        selected_toollist = gaia_toollist 

    with open(args.file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        metrics = get_metrics(data, selected_toollist)
    print(metrics)