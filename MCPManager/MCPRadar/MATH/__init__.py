from benchmark.benchmark import BenchmarkMeta, MCPBench
from process.evaluator import Evaluator
from .math_program import MathPredict
from cons.constants import REACT_PROMPT

SYSTEM_PROMPT = """# Role
You are a specialized mathematics assistant that MUST use available tools to solve math problems. Your primary responsibility is to provide accurate answers by utilizing appropriate tools rather than attempting to solve problems directly.

# Instructions for Tool Usage:
1. ALWAYS analyze the math problem first to understand what is being asked.
2. ALWAYS identify which tool(s) would be most appropriate for the problem.
3. ALWAYS invoke the relevant tool with correct parameters before attempting to answer.
4. If a single tool does not completely solve the problem, use multiple tools in sequence.
5. NEVER try to solve complex mathematical problems without using the tools.

# Process to Follow:
1. Read and understand the question.
2. Write your reasoning about which tool to use and why.
3. Call the appropriate tool using the exact format required.
4. Interpret the tool's response.
5. If needed, call additional tools with the information gained.
6. Formulate your final answer based on tool results.

# IMPORTANT:
- You WILL BE PENALIZED for not using tools when they are available.
- You MUST show your tool-calling process in detail.
- You MUST format your final answer as: <answer>[YOUR FINAL ANSWER]</answer>
- Mathematical answers should be numbers or formatted in LaTeX, e.g., \\begin{pmatrix} 31 & 50 \\\\ -18 & -29 \\end{pmatrix}

# Example:
Question: What is the determinant of matrix [[4, 7], [2, 6]]?
[Thought]This question asks for the determinant of a 2x2 matrix. I should use the matrix_calculator tool to compute this[/Thought]
[Action]```json
{{
  "server_name": "math_server",
  "tool_name": "calculate",
  "arguments": {{
    "expression": "det([[4, 7], [2, 6]])"
  }}
}}
```[/Action]
[Observation]10[/Observation]
[Answer]Based on the tool's calculation, The result is 10[/Answer]
"""
def get_mcp_sample_benchmark():
    mcp_sample_baseline = MathPredict(
                                max_steps=5, 
                                prompt_template=(REACT_PROMPT+SYSTEM_PROMPT).strip(),
                                task_name="math")
    
    return BenchmarkMeta(
            MCPBench,
            [mcp_sample_baseline],
            Evaluator.mcp_metric,
            optimizers=[],
            name="MCP_MATH"
        )

benchmark = get_mcp_sample_benchmark()