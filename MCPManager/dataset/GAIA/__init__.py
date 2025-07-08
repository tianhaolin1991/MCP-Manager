from benchmark import BenchmarkMeta, MCPBench
from utils.evaluation_utils import mcp_metric
from GAIA.gaia_program import GAIAPredict
from cons.constants import REACT_PROMPT

SYSTEM_PROMPT = """# Role
You are a helpful assistant. You are able to answer questions using different tools. """
def get_mcp_sample_benchmark():
    mcp_sample_baseline = GAIAPredict(
        max_steps=5,
        system_prompt=SYSTEM_PROMPT + REACT_PROMPT,
        task_name="gaia")
    
    return [
        BenchmarkMeta(
            MCPBench,
            [mcp_sample_baseline],
            mcp_metric,
            optimizers=[],
            name="MCP_GAIA"
        )
    ]

benchmark = get_mcp_sample_benchmark()