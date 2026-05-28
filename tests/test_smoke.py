from src.runner import health_check


def test_health_check():
    assert health_check() == "ok"