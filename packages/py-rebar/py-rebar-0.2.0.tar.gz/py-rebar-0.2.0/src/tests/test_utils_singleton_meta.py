"""Unit tests for utils/singleton_meta.py."""
from pyrebar.utils import SingletonMeta


class TestClass(metaclass=SingletonMeta):
    """Test singleton class."""

    value: str = "foo"


def test_singleton():
    """Unit test for the SingletonMeta metaclass."""
    a = TestClass()
    b = TestClass()

    assert a.value == b.value
    assert a == b

    a.value = "bar"
    assert "bar" == b.value
