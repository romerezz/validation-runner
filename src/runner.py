from src.models import TestRun, TestStatus
from src.store import TestRunStore

def create_test_run(name: str, test_type: str, store: TestRunStore) -> TestRun:
    return store.add_test_run(name, test_type)

def run_test(test_run_id: int, passed: bool, store: TestRunStore) -> TestRun:
    test_run = store.get_test_run(test_run_id)

    if test_run.is_finished():
        raise RuntimeError("Test cannot be executed again.")

    test_run.status = TestStatus.RUNNING

    if passed:
        test_run.status = TestStatus.PASSED
    else:
        test_run.status = TestStatus.FAILED

    return test_run

def health_check():
    return "ok"