from benchmark.benchmark import BenchmarkMeta, MCPBench
from process.evaluator import Evaluator
from .coding_program import CodingPredict
from cons.constants import REACT_PROMPT

SYSTEM_PROMPT = """# Role
You are a helpful assistant. You are able to answer questions using different tools. """
def get_mcp_sample_benchmark():
    mcp_sample_baseline = CodingPredict(
        max_steps=5,
        prompt_template=(REACT_PROMPT + SYSTEM_PROMPT).strip(),
        task_name="gaia")
    
    return BenchmarkMeta(
            MCPBench,
            [mcp_sample_baseline],
            Evaluator.mcp_metric,
            optimizers=[],
            name="MCP_GAIA"
        )


benchmark = get_mcp_sample_benchmark()