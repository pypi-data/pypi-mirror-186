"""Test backend module

This module exists just for test purposes
"""
import uuid

import xarray as xr  # noqa: F401

from demessaging import main
from demessaging.types.xarray import DataArray

__all__ = ["compute_sum"]


topic = "test_topic_" + uuid.uuid4().urn[9:]


def compute_sum(da: DataArray) -> DataArray:
    """Compute the sum over a data array.

    Parameters
    ----------
    da : DataArray
        The input data array

    Returns
    -------
    DataArray
        The sum of the data array
    """
    return da.sum()


if __name__ == "__main__":
    main(messaging_config=dict(topic=topic))
