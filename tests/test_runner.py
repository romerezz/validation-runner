import pytest
from src.models import TestStatus
from src.store import TestRunStore
from src.runner import create_test_run, run_test

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
    
