import random, os, json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, List, Type

import dspy

import benchmark.optimizers as MCPRadar_optimizers
from config_utils import read_jsonl
from mcp_program import MCPPredict
from process.llm import LLMCallRecord
from cons.constants import *

dataset_size = {"full": None, "lite": 500, "tiny": 200, "test": 2}


class Benchmark(ABC):
    def __init__(self, dataset_mode="lite"):
        # dataset for training and validation
        self.dataset = None
        # dataset for the actual benchmarking
        self.test_set = None
        self.train_set = None
        self.dev_set = None
        self.val_set = None

        self.init_dataset()
        assert self.dataset is not None, "Dataset not initialized"
        assert self.test_set is not None, "Test set not initialized"
        self.max_testset_size = dataset_size[dataset_mode]

        self.test_set = self.trim_dataset(self.test_set, self.max_testset_size)

        # TODO: FIXME: "test" option is for debugging purposes only, should be removed for final release
        if dataset_mode == "test":
            self.dataset = self.trim_dataset(self.dataset, 60)
            self.create_splits()
            self.test_set = self.trim_dataset(self.test_set, 50)

        if not self.train_set or not self.dev_set or not self.val_set:
            self.create_splits()

        self.train_set = self.trim_dataset(self.train_set, 150)
        self.dev_set = self.trim_dataset(self.dev_set, 300)
        self.val_set = self.trim_dataset(self.val_set, 300)

        assert self.train_set is not None, "Train set not initialized"
        assert self.dev_set is not None, "Dev set not initialized"
        assert self.val_set is not None, "Val set not initialized"

    @abstractmethod
    def init_dataset(self) -> None:
        """
        Initializes the dataset for the benchmark, and sets it to self.dataset.
        Each element in the dataset should be an instance of dspy.Example.
        """
        return

    def trim_dataset(self, dataset, size: int) -> None:
        if size is None or size >= len(dataset):
            return dataset
        rng = random.Random()
        rng.seed(1)
        return rng.sample(dataset, size)

    def create_splits(self) -> None:
        """
        Creates the splits for the dataset (not including test).
        Upon completion, self.train_set, self.dev_set, and self.val_set should be set.
        """

        total_len = len(self.dataset)
        self.dev_set = self.dataset[: int(0.4 * total_len)]
        self.val_set = self.dataset[int(0.4 * total_len) : int(0.8 * total_len)]
        self.train_set = self.dataset[int(0.8 * total_len) :]

    def get_dataset(self):
        return self.dataset

    def get_train_set(self):
        return self.train_set

    def get_dev_set(self):
        return self.dev_set

    def get_test_set(self):
        return self.test_set


class MCPBench(Benchmark):
    def __init__(self, dataset_mode="lite", dataset_path=None):
        self.dataset_path = dataset_path
        super().__init__(dataset_mode=dataset_mode)

    def init_dataset(self):
        self.dataset = []
        self.test_set = []
        test_raw_data = read_jsonl(self.dataset_path)
        
        for test_data in test_raw_data:
            self.test_set.append(
                dspy.Example(
                    id=test_data["unique_id"],
                    question=test_data["Prompt"],
                    answer=test_data["Answer"],
                ).with_inputs("id", "question", "answer", "config")
            )




@dataclass
class EvaluationResult:
    benchmark: str
    program: str

    score: float
    cost: float
    input_tokens: int
    output_tokens: int

    outputs_raw_data: List|None = None

    # optimizer: str = None
    # optimized_program: dspy.Module = None
    # optimizer_input_tokens: int = None
    # optimizer_output_tokens: int = None
    # optimizer_cost: float = None

    # optimizer_program_scores: list[float] = None


@dataclass
class BenchmarkMeta:
    benchmark: Type[Benchmark]
    program: List[MCPPredict]
    metric: Callable
    dataset_mode: str = "lite"

    optimizers: List[MCPRadar_optimizers.OptimizerConfig] = field(
        default_factory=lambda: MCPRadar_optimizers.DEFAULT_OPTIMIZERS
    )

    # BenchmarkMeta.num_threads has higher priority than run time argument of num_threads
    # use this as an upper bound for the number of threads to use
    num_threads: int = None
    name: str = None


def setup_lm(dspy_config=None):
    lm: dspy.LM = dspy_config.get("lm", dspy.settings.lm)
    assert lm is not None, "dspy language model not set"

    lm = lm.copy()
    assert len(lm.history) == 0, "language model history not empty"
    return lm


# def calculate_stats(lm: dspy.LM) -> tuple[float, int, int]:
#     cost = 0
#     input_tokens = 0
#     output_tokens = 0
#     for i, trace in enumerate(lm.history):
#         cost += trace.get("cost", None) or 0
#         input_tokens += trace.get("usage", 0).get("prompt_tokens", 0)
#         output_tokens += trace.get("usage", 0).get("completion_tokens", 0)

#     return cost, input_tokens, output_tokens

def calculate_stats(manager: List[LLMCallRecord]) -> tuple[float, float, float]:
    input_tokens = sum(usage["prompt_tokens"] for trace in manager for usage in trace.lm_usages)
    output_tokens = sum(usage["completion_tokens"] for trace in manager for usage in trace.lm_usages)
    
    avg_input = input_tokens // len(manager)
    avg_output = output_tokens // len(manager)
    
    return 0, avg_input, avg_output



class EvaluateBench(ABC):
    def __init__(
        self,
        benchmark: Benchmark,
        program: MCPPredict,
        metric: Callable,
        lm: str,
        benchmark_name: str = None,
        num_threads: int = 1,
        api_key: str = None,
        api_base: str = None,
    ):
        self.benchmark = benchmark
        self.program = program
        self.lm = lm
        self.program.setup_lm(lm, api_key=api_key, api_base=api_base)
        self.metric = metric
        self.num_threads = num_threads
        self.devset = benchmark.get_test_set()
        self.program_name = getattr(
            self.program, "_name", self.program.__class__.__name__
        )
        self.benchmark_name = benchmark_name or self.benchmark.__class__.__name__
        self.results: list[EvaluationResult] = []

    def get_empty_results(self):
        return EvaluationResult(
            benchmark=self.benchmark_name,
            program=self.program_name,
            score=0,
            cost=0,
            input_tokens=0,
            output_tokens=0,
        )

    def save_predictions_to_json(self, datasets, predictions, output_path):
        """
        Save predictions and their metadata to a JSON file.
        
        Args:
            predictions: List of prediction results
            output_path: Path to save the JSON file
        """
        results = []
        
        for i, pred in enumerate(predictions):
            example = datasets[i] if datasets is not None else None
            # Extract basic information
            result = {
                "unique_id": example.id if hasattr(example, 'id') else None,
                "question": pred.question if hasattr(pred, 'question') else None,
                "ground_truth": pred.ground_truth if hasattr(pred, 'ground_truth') else None,
                "prediction": pred.answer if hasattr(pred, 'answer') else None,
                "success": pred.success if hasattr(pred, 'success') else None,
            }
            
            # Extract tool usage information
            tool_usage = {}
            if hasattr(pred, 'process_report') and pred.process_report:
                # Extract information about tool calls
                tool_calls = []
                
                # Get all tool calls from the conversation trace
                if hasattr(pred, 'trace'):
                    for message in pred.trace:
                        if message.get(ROLE) == constants.TOOL and message.get(constants.TOOL_CALLS):
                            for tool_call in message.get(constants.TOOL_CALLS):
                                if tool_call.get("type") == "function":
                                    function_info = tool_call.get("function", {})
                                    tool_calls.append({
                                        "name": function_info.get("name"),
                                        "arguments": function_info.get("arguments")
                                    })
                
                # Count tools by type
                tool_count = len(tool_calls)
                tool_names = [call["name"] for call in tool_calls]
                
                tool_usage = {
                    "tool_calls": tool_calls,
                    "total_tool_count": tool_count,
                    "tool_names": tool_names
                }
            
            result["tool_usage"] = tool_usage
            
            # Extract model usage statistics
            if hasattr(pred, 'process_report') and pred.process_report:
                if hasattr(pred.process_report, 'lm_usages'):
                    try:
                        result["token_usage"] = {
                            "prompt_tokens": sum(usage.get('prompt_tokens', 0) for usage in pred.process_report.lm_usages),
                            "completion_tokens": sum(usage.get('completion_tokens', 0) for usage in pred.process_report.lm_usages),
                            "total_tokens": sum((usage.get('prompt_tokens', 0) + usage.get('completion_tokens', 0)) 
                                            for usage in pred.process_report.lm_usages)
                        }
                    except Exception as e:
                        print(f"Warning: Could not extract token usage: {e}")
                        result["token_usage"]={
                            "prompt_tokens": 0,
                            "completion_tokens": 0,
                            "total_tokens": 0
                        }
            
            results.append(result)
        
        # Save to JSON file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"Saved {len(results)} predictions to {output_path}")
        return results

    def evaluate_baseline(self) -> EvaluationResult:
        score, info = self.program.evaluate(self.devset, self.metric)
        result = self.get_empty_results()
        datasets, outputs, _ = zip(*info)
        managers = [one.process_report for one in outputs if hasattr(one, 'process_report')]

        result.score = score   
        result.outputs_raw_data = outputs
        if not managers:
            result.cost = 0
            result.input_tokens = 0
            result.output_tokens = 0
        else:
            result.cost, result.input_tokens, result.output_tokens = calculate_stats(managers)
        
        # Save raw predictions to JSON
        output_dir = os.path.join("results", self.benchmark_name)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{self.program_name}_{self.lm}_predictions.json")
        self.save_predictions_to_json(datasets, outputs, output_path)
        
        return result

    def evaluate(self) -> EvaluationResult:
        result = self.evaluate_baseline()
        self.results = result
        return result
