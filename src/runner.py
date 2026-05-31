from src.models import TestRun, TestStatus

def create_test_run(test_name: str, environment: str) -> TestRun:
    return TestRun(test_name, TestStatus.PENDING, environment)


def health_check():
    return "ok"