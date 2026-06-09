from src.models import TestRun, TestStatus

class TestRunStore:
    def __init__(self) -> None:
        self._test_runs: dict[int, TestRun] = {}
        self._next_id: int = 1

    def add_test_run(self, name: str, test_type: str) -> TestRun:
        test_run = TestRun(self._next_id, name, test_type)
        self._test_runs[test_run.id] = test_run
        self._next_id += 1
        return test_run

    def get_test_run(self, test_run_id: int) -> TestRun:
        return self._test_runs[test_run_id]

