from dataclasses import dataclass
from enum import Enum

class TestStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    PASSED = "PASSED"
    FAILED = "FAILED"

@dataclass
class TestRun:
    id: int
    name: str
    test_type: str
    status: TestStatus = TestStatus.PENDING

    def is_finished(self) -> bool:
        return self.status in [TestStatus.PASSED, TestStatus.FAILED]