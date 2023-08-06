"""Test backend module

This module exists just for test purposes
"""
import uuid
from typing import List

from demessaging import config, main

__all__ = ["func_basic"]


topic = "test_topic_" + uuid.uuid4().urn[9:]


@config.registry.register_type
class MyType:
    """Just a test type to see if it appeads in the generated API module."""

    def __init__(self, a: int) -> None:
        self.a = a

    def add2a(self, b: int) -> int:
        return self.a + b


def func_basic(a: int) -> List[int]:
    """A test function.

    With some docu.

    Parameters
    ----------
    a: integer
        An integer

    Returns
    -------
    list of int
        A list of integers
    """
    return [a]


if __name__ == "__main__":
    main(messaging_config=dict(topic=topic))
