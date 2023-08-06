import pytest

PYTEST_BENCHMARK_PARAMS = {
    "min_time": 0.01,
    "max_time": 0.05,
    "min_rounds": 5,
    "warmup": True,
    "warmup_iterations": 1,
}


def get_pytest_benchmark(group: str):
    return pytest.mark.benchmark(group=group, **PYTEST_BENCHMARK_PARAMS)
