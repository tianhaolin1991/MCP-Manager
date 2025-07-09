from benchmark.benchmark import BenchmarkMeta, MCPBench

from MCPRadar.GAIA.gaia_program import GAIAPredict
from cons.constants import REACT_PROMPT
from process.evaluator import Evaluator

SYSTEM_PROMPT = """# Role
You are a helpful assistant. You are able to answer questions using different tools. """
def get_mcp_sample_benchmark():
    mcp_sample_baseline = GAIAPredict(
        max_steps=20,
        prompt_template=SYSTEM_PROMPT + REACT_PROMPT,
        task_name="gaia")
    
    return BenchmarkMeta(
            MCPBench,
            [mcp_sample_baseline],
            Evaluator.mcp_metric,
            optimizers=[],
            name="MCP_GAIA"
        )

benchmark = get_mcp_sample_benchmark()