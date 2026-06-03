import pytest
from src.models import TestStatus, TestRun
from src.store import TestRunStore
from src.runner import create_test_run, run_test, cancel_test

def test_run_passes() -> None:
    store = TestRunStore()
    test_run = create_test_run("login test", "functional", store)

    result = run_test(test_run.id, True, store)

    assert result.status == TestStatus.PASSED

def test_run_finished_cannot_run_again() -> None:
    store = TestRunStore()
    test_run = create_test_run("login test", "functional", store)

    run_test(test_run.id, True, store)

    with pytest.raises(RuntimeError):
        run_test(test_run.id, True, store)
    
def test_cancel_pending_test_run() -> None:
    store = TestRunStore()
    test_run = create_test_run("login test", "functional", store)
    cancelled_test_run = cancel_test(test_run.id, store)

    assert cancelled_test_run.status == TestStatus.CANCELLED

def test_cannot_cancel_passed_test_run() -> None:
    store = TestRunStore()
    test_run = create_test_run("login test", "functional", store)
    run_test(test_run.id, True, store)

    with pytest.raises(RuntimeError):
        cancel_test(test_run.id, store)
    