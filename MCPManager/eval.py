import argparse
import os
import pathlib
import sys
from pathlib import Path

import dspy

from analysis import read_evaluation_results
from benchmark.benchmark import BenchmarkMeta, EvaluateBench, EvaluationResult
from utils.file_util import read_jsonl_file
from benchmark.register_benchmark import register_all_benchmarks, registered_benchmarks


class CompareAnswerSignature(dspy.Signature):
    """
    Compare the answer to the ground truth answer.
    """

    answer = dspy.InputField(desc="The answer to a problem")
    ground_truth = dspy.InputField(desc="The ground truth answer to the same problem")
    is_correct = dspy.OutputField(
        desc="Whether the answer is correct, either True or False."
    )


class CompareAnswer(dspy.Module):
    def __init__(self):
        self.compare_answer = dspy.ChainOfThought(CompareAnswerSignature)

    def forward(self, ground_truth, answer):
        pred = self.compare_answer(answer=answer, ground_truth=ground_truth)
        return pred


def llm_as_judge_evaluate(gold, pred, extract_answer_fun=lambda x: x.answer):
    compare_answer = CompareAnswer()
    answer_raw = compare_answer(
        ground_truth=extract_answer_fun(gold), answer=extract_answer_fun(pred)
    ).is_correct
    if answer_raw.lower().startswith("true"):
        return True
    else:
        return False


#@contextmanager
#def suppress_output(suppress=True):
#    if suppress:
#        # Save the original streams
#        original_stderr = sys.stderr
#        original_stdout = sys.stdout

        # Redirect stderr and stdout to devnull
#        sys.stderr = open(os.devnull, "w")
#        sys.stdout = open(os.devnull, "w")

#    try:
#        yield
#    finally:
#        if suppress:
#            # Restore the original streams
#            sys.stderr.close()
#            sys.stdout.close()
#            sys.stderr = original_stderr
#            sys.stdout = original_stdout


def generate_evaluation_records(file_path):
    file_path = pathlib.Path(file_path)

    # if the records file already exists, do not overwrite it
    if (file_path / "evaluation_records.csv").exists():
        return

    # List all .txt files in the directory
    all_result_files = list(file_path.rglob("*.txt"))

    records = []

    # Process each file
    for file in all_result_files:
        # Split the filename to get benchmark, program, and optimizer
        file_name_parts = file.stem.split("_")
        if len(file_name_parts) >= 3:
            benchmark = file_name_parts[0]
            program = file_name_parts[1]
            optimizer = file_name_parts[2]
            records.append((benchmark, program, optimizer))
        else:
            raise ValueError(f"Invalid file name: {file.name}")

    with open(f"{file_path}/evaluation_records.csv", "w") as f:
        f.write("benchmark,program,optimizer\n")
        for record in records:
            f.write(",".join(record) + "\n")


def add_to_evaluation_records(file_path, evaluation_results: list[EvaluationResult]):
    file_path = pathlib.Path(file_path)

    with open(f"{file_path}/evaluation_records.csv", "a") as f:
        for evaluation_result in evaluation_results:
            f.write(
                f"{evaluation_result.benchmark},{evaluation_result.program},{evaluation_result.optimizer}\n"
            )


def read_evaluation_records(file_path):
    file_path = pathlib.Path(file_path)
    records = []

    # create the records file if it does not exist
    if not (file_path / "evaluation_records.csv").exists():
        # create empty records file without header
        with open(f"{file_path}/evaluation_records.csv", "w") as f:
            f.write("")
    with open(f"{file_path}/evaluation_records.csv", "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            records.append(tuple(line.strip().split(",")))

    return records


def evaluate(
    benchmark_meta: BenchmarkMeta,
    lm,
    file_path,
    num_threads=8,
    dataset_mode=None,
    dataset_path=None,
    api_key=None,
    api_base=None,
):
    """
    benchmark_meta: BenchmarkMeta object to evaluate
    lm: Language model to use, should be an instance of dspy.LM
    missing_mode: only evaluate experiments without a result file
    """
    dataset_mode = dataset_mode or benchmark_meta.dataset_mode
    benchmark = benchmark_meta.benchmark(dataset_mode=dataset_mode, dataset_path=dataset_path)
    # Canonicalize optimizers to (optimizer, compile_kwargs) tuples
    benchmark_name = benchmark_meta.name or benchmark.__class__.__name__

    num_threads = benchmark_meta.num_threads or num_threads
    print(f"Evaluating {benchmark_name}")
    print(f"num_threads: {num_threads}")
    print(f"Test set size: {len(benchmark.test_set)}")


    Path(file_path).mkdir(parents=True, exist_ok=True)

    evaluation_records = read_evaluation_records(file_path)

    # create a stats file for each experiment
    stats_file = os.path.join(file_path, f"{benchmark_name}.stat")
    with open(stats_file, "w") as f:
        f.write(
            f"benchmark: {benchmark_name}\n"
            f"lm: {lm}\n"
            f"test_set_size: {len(benchmark.test_set)}\n"
        )

    for program in benchmark_meta.program:
        program_name = getattr(program, "_name", program.__class__.__name__)
        setattr(program, "mcp_config", global_config)
        # if missing_mode:
            # Only run missing experiments
            # for optimizer in benchmark_meta.optimizers:
            #     if (benchmark_name, program_name, optimizer.name) in evaluation_records:
            #         optimizers.remove(optimizer)
            # if (benchmark_name, program_name, "None") in evaluation_records:
            #     evaluate_baseline_flag = False

        print(f"Program: {program_name}")

        evaluate_bench = EvaluateBench(
            benchmark=benchmark,
            program=program,
            metric=benchmark_meta.metric,
            lm=lm,
            benchmark_name=benchmark_meta.name,
            num_threads=num_threads,
            api_key=api_key if api_key else os.getenv("OPENAI_API_KEY", ""),
            api_base=api_base if api_base else os.getenv("OPENAI_API_BASE", ""),
        )
        evaluate_bench.evaluate()
        evaluation_result = evaluate_bench.results
        file_name = f"{evaluation_result.benchmark}_{evaluation_result.program}"
        with open(os.path.join(file_path, f"{file_name}.txt"), "w") as f:
            f.write(f"score,cost,input_tokens,output_tokens\n")
            f.write(
                f"{evaluation_result.score},{evaluation_result.cost},{evaluation_result.input_tokens},"
                f"{evaluation_result.output_tokens}\n"
            )


def evaluate_all(
    benchmarks,
    lm,
    file_path,
    num_threads=8,
    suppress_dspy_output=False,
    dataset_mode=None,
    dataset_path=None,
    missing_mode=False,
    api_key=None,
    api_base=None,
):
    # 只有当benchmarks是字符串列表时才进行注册
    if benchmarks and isinstance(benchmarks[0], str):
        benchmarks = register_all_benchmarks(benchmarks)
    if missing_mode:
        generate_evaluation_records(file_path)
    for benchmark_meta in benchmarks:
        evaluate(
            benchmark_meta,
            lm,
            file_path,
            num_threads,
            dataset_mode,
            dataset_path,
            api_key=api_key,
            api_base=api_base,
        )

    df = read_evaluation_results(file_path)
    df.to_csv(f"{file_path}/evaluation_results.csv", index=False)
    df["model"] = lm

    # generate evaluation records
    generate_evaluation_records(file_path)

global_config=None
def main():
    
    parser = argparse.ArgumentParser(description="MCPRadar benchmark evaluation")
    parser.add_argument("--benchmark", type=str, required=True, help="Benchmark to evaluate")
    parser.add_argument("--lm", type=str, required=True, help="Language model to use")
    parser.add_argument("--lm_api_key", type=str, help="API key for language model")
    parser.add_argument(
        "--lm_api_base", type=str, help="API base for language model"
    )
    parser.add_argument(
        "--dataset_mode", type=str, help="Dataset mode (train, val, test)"
    )
    parser.add_argument(
        "--dataset_path", type=str, help="Dataset path"
    )
    parser.add_argument(
        "--num_threads", type=int, default=8, help="Number of threads to use"
    )
    parser.add_argument(
        "--file_path", type=str, default="evaluation", help="File path for evaluation results"
    )
    parser.add_argument(
        "--suppress_dspy_output",
        action="store_true",
        help="Suppress dspy output",
    )
    parser.add_argument(
        "--missing_mode",
        action="store_true",
        help="Only run missing experiments (skip experiments that already have results)",
    )
    parser.add_argument(
        "--config",
        type=str,
        default='ddgo.json',
        help="Configuration file for the benchmark",
    )
    
    args = parser.parse_args()

    global_config= read_json(args.config)
    # 处理benchmark参数
    benchmark_path = args.benchmark
    if not benchmark_path.startswith(""):
        benchmark_path = f"{benchmark_path}"
    
    # 注册所有基准测试
    register_all_benchmarks([benchmark_path])

    benchmarks = [benchmark for benchmark in registered_benchmarks]
    if not benchmarks:
        print(f"No benchmark registered with name {args.benchmark}")
        sys.exit(1)

    evaluate_all(
        benchmarks,
        args.lm,
        args.file_path,
        num_threads=args.num_threads,
        suppress_dspy_output=args.suppress_dspy_output,
        dataset_mode=args.dataset_mode,
        dataset_path=args.dataset_path,
        missing_mode=args.missing_mode,
        api_key=args.lm_api_key,
        api_base=args.lm_api_base,
    )

if __name__ == "__main__":
    main()
