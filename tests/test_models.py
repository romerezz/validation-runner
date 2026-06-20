from src.models import TestRun, TestStatus, validate_status_transition
import pytest

def test_pending_to_running_is_valid() -> None:
    validate_status_transition(TestStatus.PENDING, TestStatus.RUNNING)
    
def test_running_to_passed_is_valid() -> None:
    validate_status_transition(TestStatus.RUNNING, TestStatus.PASSED)

def test_running_to_failed_is_valid() -> None:
    validate_status_transition(TestStatus.RUNNING, TestStatus.FAILED)

def test_passed_to_running_is_invalid() -> None:
    with pytest.raises(RuntimeError):
        validate_status_transition(TestStatus.PASSED, TestStatus.RUNNING)

def test_failed_to_running_is_invalid() -> None:
    with pytest.raises(RuntimeError):
        validate_status_transition(TestStatus.FAILED, TestStatus.RUNNING)

def test_pending_to_cancelled_is_valid() -> None:
    validate_status_transition(TestStatus.PENDING, TestStatus.CANCELLED)

def test_cancelled_to_running_is_invalid() -> None:
        with pytest.raises(RuntimeError):
            validate_status_transition(TestStatus.CANCELLED, TestStatus.RUNNING)

def test_passed_run_is_finished() -> None:
    run = TestRun(id=1, name="login test", test_type="functional", status=TestStatus.PASSED)
    assert run.is_finished() is True

def test_failed_run_is_finished() -> None:
    run = TestRun(id=1, name="login test", test_type="functional", status=TestStatus.FAILED)
    assert run.is_finished() is True

def test_cancelled_run_is_finished() -> None:
    run = TestRun(id=1, name="login test", test_type="functional", status=TestStatus.CANCELLED)
    assert run.is_finished() is True

def test_pending_run_is_not_finished() -> None:
    run = TestRun(id=1, name="login test", test_type="functional", status=TestStatus.PENDING)
    assert run.is_finished() is False

def test_running_run_is_not_finished() -> None:
    run = TestRun(id=1, name="login test", test_type="functional", status=TestStatus.PENDING)
    assert run.is_finished() is False