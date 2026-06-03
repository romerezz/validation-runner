from src.models import TestRun, TestStatus, validate_status_transition
from src.store import TestRunStore

def health_check():
    return "ok"

def create_test_run(name: str, test_type: str, store: TestRunStore) -> TestRun:
    return store.add_test_run(name, test_type)

def run_test(test_run_id: int, passed: bool, store: TestRunStore) -> TestRun:
    test_run = store.get_test_run(test_run_id)

    validate_status_transition(test_run.status, TestStatus.RUNNING)
    test_run.status = TestStatus.RUNNING

    if passed:
        validate_status_transition(test_run.status, TestStatus.PASSED)
        test_run.status = TestStatus.PASSED
    else:
        validate_status_transition(test_run.status, TestStatus.FAILED)
        test_run.status = TestStatus.FAILED

    return test_run

def cancel_test(test_run_id: int, store: TestRunStore) -> TestRun:
    test_run = store.get_test_run(test_run_id)

    validate_status_transition(test_run.status, TestStatus.CANCELLED)
    test_run.status = TestStatus.CANCELLED

    return test_run