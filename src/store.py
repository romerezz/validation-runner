from src.models import TestRun

test_runs: list[TestRun] = []

def save_test_run(test_run: TestRun) -> None:
    test_runs.append(test_run)

def get_test_runs() -> list[TestRun]:
    return test_runs   