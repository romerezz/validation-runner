import pytest
from src.models import TestStatus, TestRun
from src.store import TestRunStore
from src.runner import create_test_run, run_test, cancel_test
from src.errors import ValidationError

@pytest.fixture
def store() -> TestRunStore:
    return TestRunStore()

def test_run_passes(store: TestRunStore) -> None:
    test_run = create_test_run("login test", "smoke", store)

    result = run_test(test_run.id, True, store)

    assert result.status == TestStatus.PASSED

def test_run_finished_cannot_run_again(store: TestRunStore) -> None:
    run = create_test_run("login test", "smoke", store)

    run_test(run.id, True, store)

    with pytest.raises(RuntimeError):
        run_test(run.id, True, store)
    
def test_cancel_pending_test_run(store: TestRunStore) -> None:
    test_run = create_test_run("login test", "smoke", store)
    cancelled_test_run = cancel_test(test_run.id, store)

    assert cancelled_test_run.status == TestStatus.CANCELLED

def test_cannot_cancel_passed_test_run(store: TestRunStore) -> None:
    test_run = create_test_run("login test", "smoke", store)
    run_test(test_run.id, True, store)

    with pytest.raises(RuntimeError):
        cancel_test(test_run.id, store)

def test_get_test_run_returns_created_test_run(store: TestRunStore) -> None:
    test_run = create_test_run("memory test", "smoke", store)
    
    assert test_run == store.get_test_run(test_run.id)

def test_get_missing_test_run_raises_error(store: TestRunStore) -> None:
    with pytest.raises(KeyError):
        store.get_test_run(999)

def test_run_missing_test_run_raises_error(store: TestRunStore) -> None:
    with pytest.raises(KeyError):
        run_test(999, True, store)

def test_create_test_run_rejects_invalid_test_type(store) -> None:
    with pytest.raises(ValidationError):
        create_test_run("login test", "banana", store)