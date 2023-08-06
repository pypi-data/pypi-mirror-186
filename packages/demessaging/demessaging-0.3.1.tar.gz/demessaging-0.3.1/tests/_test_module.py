"""Test backend module

This module exists just for test purposes
"""
import uuid
from typing import List

from conftest import ArbitraryTestModel, ArbitraryType

from demessaging import main

__all__ = [
    "Class",
    "func_arbitrary_model",
    "func_basic",
    "func_arbitrary_type",
]


topic = "test_topic_" + uuid.uuid4().urn[9:]


class Class:
    """A test class."""

    def __init__(self, a: int, b: int = 1):
        """
        Parameters
        ----------
        a : int
            first integer
        b : int, optional
            second integer, by default 1
        """
        self.a = a
        self.b = b

    @staticmethod
    def sum(a: int, b: int) -> int:
        """
        Parameters
        ----------
        a : int
            first integer
        b : int, optional
            second integer, by default 1

        Returns
        -------
        int
            The sum of `a` and `b`
        """
        return a + b

    def _this_should_not_be_included(self, a: int) -> int:
        """This method should not be included because it stats with _

        Parameters
        ----------
        a: int
            Some dummy int
        """
        return a

    def add2a(self, c: int) -> int:
        """Add a number to `a`.

        Parameters
        ----------
        c : int
            The number to add

        Returns
        -------
        int
            a + c
        """
        return self.a + c

    def add2b(self, c: int) -> int:
        """Add a number to `b`

        Parameters
        ----------
        c : int
            The number to add

        Returns
        -------
        int
            b + c
        """
        return self.b + c


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


def func_arbitrary_type(a: ArbitraryType) -> ArbitraryType:
    """Test function for arbitrary types.

    Parameters
    ----------
    a: ArbitraryType
        Some arbitrary thing

    Returns
    -------
    ArbitraryType
        The same as `a`
    """
    return a


def func_arbitrary_model(a: ArbitraryTestModel) -> ArbitraryTestModel:
    """Test function for arbitrary models.

    Parameters
    ----------
    a: ArbitraryTestModel
        Some arbitrary thing

    Returns
    -------
    ArbitraryTestModel
        The same as `a`
    """
    return a


def _private_func():
    """This should not be included."""
    pass


if __name__ == "__main__":
    main(messaging_config=dict(topic=topic))
