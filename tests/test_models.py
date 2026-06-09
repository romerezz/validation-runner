from src.models import TestStatus, validate_status_transition
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
