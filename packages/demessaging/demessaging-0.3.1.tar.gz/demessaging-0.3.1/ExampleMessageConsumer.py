"""Example backend module for the de-messaging framework.

Start this module by typing::

    python ExampleMessageConsumer.py -t your-custom-topic connect

in the terminal, or::

    python ExampleMessageConsumer.py --help

for further options.
"""
import datetime
from typing import List, Optional

# this import is (unfortunately) necessary to resolve the deprogressapi.tree in
# the generated client stub
import deprogressapi.tree  # noqa: F401
from deprogressapi import ProgressReport
from pydantic import BaseModel, validate_arguments

from demessaging import configure, main, registry
from demessaging.types.xarray import DataArray

__all__ = ["hello_world", "HelloWorld", "compute_sum", "report_progress_demo"]


@registry.register_type
class GreetResponse(BaseModel):

    message: str
    greetings: List[str]
    greeting_time: datetime.datetime


# You can configure different validations for the parameters.
# Here, we know that `repeat` must at least be 0, so we set this as a field
# parameter (see
# https://pydantic-docs.helpmanual.io/usage/schema/#field-customisation)
# for available validators
@configure(field_params={"repeat": {"ge": 0}})
def hello_world(
    message: str, repeat: int, greet_message: str
) -> GreetResponse:
    """Greet the hello world module.

    Parameters
    ----------
    message: str
        Message that will be part of the greet response
    repeat: int
        Number of repetitions of the greet message
    greet_message: str
        Message string that will be mirror back to the requesting node

    Returns
    -------
    GreetResponse
        Hello world greet response object
    """
    greetings: List[str] = [greet_message] * repeat
    return GreetResponse(
        message=message,
        greetings=greetings,
        greeting_time=datetime.datetime.now(),
    )


# You can also use generic python classes as input/output for your model. In
# this case, we use xarrays DataArray. Note that you then have to define a
# special `validate` method. See :class:`demessaging.types.xarray.DataArray`
# for instance.
@validate_arguments
def compute_sum(
    da: DataArray,
    reporter: ProgressReport = ProgressReport(step_message="Sum computation"),
) -> DataArray:
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
    import time

    with reporter:
        for i in range(10):
            with reporter.create_subreport(step_message=f"Report {i}"):
                time.sleep(1)
        ret = da.sum()
    return ret


def report_progress_demo(
    reporter: Optional[ProgressReport] = ProgressReport(
        step_message="Demo report"
    ),
) -> None:
    """Demo function for a progress report with the dasf-progress-api."""
    import time

    reporter = ProgressReport.from_arg(reporter)

    num_steps = 10
    reporter.steps = num_steps

    with reporter:
        for i in range(num_steps):
            with reporter.create_subreport(step_message=f"Sub report {i}"):
                time.sleep(1)
    return


# You can configure how the individual class in the backend module shall be
# interpreted with the `configure` function. See
# :class:`demessaging.config.ClassConfig` for available parameters
@configure(methods=["repeat_message"])
class HelloWorld:
    """Greet the world from a class.

    Classes can define the methods that shall be used for the backend, and they
    define a constructor."""

    def __init__(self, message: str):
        """
        Parameters
        ----------
        message: str
            The hello message
        """
        self.message = message

    @configure(field_params={"repeat": {"ge": 0}})
    def repeat_message(self, repeat: int) -> List[str]:
        """Repeat the `message` multiple times.

        Parameters
        ----------
        repeat: int
            The number of times, `message` shall be repeated.
        """
        return [self.message] * repeat


if __name__ == "__main__":
    main(
        messaging_config=dict(topic="mytesttopic", max_workers=4, queue_size=4)
    )
