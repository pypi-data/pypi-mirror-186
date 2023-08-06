import os

from snok.main import foo


def test_timezone() -> None:
    assert foo() == "foo"
    assert os.environ["TZ"] == "UTC"
