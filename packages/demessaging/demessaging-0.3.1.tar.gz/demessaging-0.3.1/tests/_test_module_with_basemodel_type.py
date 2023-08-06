"""Test backend module

This module exists just for test purposes
"""
import os
import uuid
from typing import List

from pydantic import BaseModel

from demessaging import config, main

__all__ = ["func_basic", "TestClass"]


topic = os.getenv("TEST_TOPIC", "test_topic_" + uuid.uuid4().urn[9:])


@config.registry.register_type
class TestBaseModelType(BaseModel):
    """Just a test type to see if it appeads in the generated API module."""

    data: int


def func_basic(a: List[TestBaseModelType]) -> int:
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
    return a[0].data


class TestClass:
    """A class to test custom basemodel types."""

    def __init__(self, a: List[TestBaseModelType]):
        """
        Parameters
        ----------
        a: List[TestBaseModelType]
            One data object
        """
        self.a = a

    def test_func(self, b: TestBaseModelType) -> int:
        """A test method

        Parameters
        ----------
        b : TestBaseModelType
            Some more data

        Returns
        -------
        int
            the sum of both
        """
        adata = self.a[0].data
        return adata + b.data


if __name__ == "__main__":
    main(messaging_config=dict(topic=topic))
