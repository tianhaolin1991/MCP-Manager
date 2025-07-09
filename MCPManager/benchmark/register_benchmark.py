from benchmark.benchmark import BenchmarkMeta

registered_benchmarks = []

def check_benchmark(benchmark):
    try:
        assert hasattr(benchmark, "benchmark")
    except AssertionError:
        return False
    return True


def register_benchmark(module: str):
    if module == 'GAIA':
        from MCPRadar.GAIA import benchmark
        registered_benchmarks.append(benchmark)
    elif module == 'Coding':
        from MCPRadar.Coding import benchmark
        registered_benchmarks.append(benchmark)
    elif module == 'MATH':
        from MCPRadar.MATH import benchmark
        registered_benchmarks.append(benchmark)
    else:
        raise ValueError(f'Unknown benchmark module {module}')

def register_all_benchmarks(benchmarks):
    for benchmark in benchmarks:
        register_benchmark(benchmark)
    return registered_benchmarks
