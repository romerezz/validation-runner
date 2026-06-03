from dataclasses import dataclass
from enum import Enum

class TestStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    PASSED = "PASSED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

@dataclass
class TestRun:
    id: int
    name: str
    test_type: str
    status: TestStatus = TestStatus.PENDING

    def is_finished(self) -> bool:
        return self.status in [TestStatus.PASSED, TestStatus.FAILED]
    
allowed_transitions = {
    TestStatus.PENDING: [TestStatus.RUNNING, TestStatus.CANCELLED],
    TestStatus.RUNNING: [TestStatus.PASSED, TestStatus.FAILED],
    TestStatus.PASSED: [],
    TestStatus.FAILED: [],
    TestStatus.CANCELLED: []
}

def validate_status_transition(current_status: TestStatus, next_status: TestStatus) -> None:
    if next_status not in allowed_transitions[current_status]:
        raise RuntimeError(
            f"Invalid status transition: {current_status.value} -> {next_status.value}"
        )