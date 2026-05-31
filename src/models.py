from dataclasses import dataclass
from enum import Enum

class TestStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    PASSED = "PASSED"
    FAILED = "FAILED"

@dataclass
class TestRun:
    test_name: str
    status: TestStatus
    environment: str

    def is_finished(self) -> bool:
        return self.status in [TestStatus.PASSED, TestStatus.FAILED]