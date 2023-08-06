"""
Example backend module for the de-messaging framework.

Start this module by typing::

    python ExampleMessageConsumer.py -t your-custom-topic connect

in the terminal, or::

    python ExampleMessageConsumer.py --help

for further options.
"""
import datetime
from typing import Any, Callable, Dict, List, Union

import deprogressapi.tree
from deprogressapi import ProgressReport
from pydantic import BaseModel

import demessaging.types.xarray
from demessaging import BackendModule as _BackendModule
from demessaging import configure, main
from demessaging.config import ModuleConfig

NoneType = type(None)


__all__ = ["hello_world", "HelloWorld", "compute_sum", "report_progress_demo"]


class GreetResponse(BaseModel):

    message: str
    greetings: List[str]
    greeting_time: datetime.datetime


@configure(
    """
{
    "field_params": {
        "repeat": {
            "ge": 0
        }
    }
}
"""
)
def hello_world(
    message: str, repeat: int, greet_message: str
) -> GreetResponse:
    """
    Greet the hello world module.

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
    request = {
        "func_name": "hello_world",
        "message": message,
        "repeat": repeat,
        "greet_message": greet_message,
    }

    model = BackendModule.parse_obj(request)
    response = model.compute()

    return response.__root__  # type: ignore


class HelloWorld:
    """
    Greet the world from a class.

    Classes can define the methods that shall be used for the backend, and they
    define a constructor.
    """

    def __init__(self, message: str):
        """
        Parameters
        ----------
        message: str
            The hello message
        """
        self._request_base: Dict[str, Any] = {
            "class_name": "HelloWorld",
            "message": message,
        }

    @configure(
        """
    {
        "field_params": {
            "repeat": {
                "ge": 0
            }
        }
    }
    """
    )
    def repeat_message(self, repeat: int) -> List[str]:
        """
        Repeat the `message` multiple times.

        Parameters
        ----------
        repeat: int
            The number of times, `message` shall be repeated.
        """
        request = self._request_base.copy()
        request["function"] = {"func_name": "repeat_message", "repeat": repeat}

        model = BackendModule.parse_obj(request)
        response = model.compute()

        return response.__root__  # type: ignore


def compute_sum(
    da: demessaging.types.xarray.DataArray,
    reporter: deprogressapi.tree.ProgressReport = ProgressReport(
        report_id="root", step_message="Sum computation", steps=0, children=[]
    ),
) -> demessaging.types.xarray.DataArray:
    """
    Compute the sum over a data array.

    Parameters
    ----------
    da : DataArray
        The input data array

    Returns
    -------
    DataArray
        The sum of the data array
    """
    request = {"func_name": "compute_sum", "da": da, "reporter": reporter}

    model = BackendModule.parse_obj(request)
    response = model.compute()

    return response.__root__  # type: ignore


def report_progress_demo(
    reporter: Union[
        deprogressapi.tree.ProgressReport, NoneType
    ] = ProgressReport(
        report_id="root", step_message="Demo report", steps=0, children=[]
    )
) -> None:
    """
    Demo function for a progress report with the dasf-progress-api.
    """
    request = {"func_name": "report_progress_demo", "reporter": reporter}

    model = BackendModule.parse_obj(request)
    response = model.compute()

    return response.__root__  # type: ignore


backend_config = ModuleConfig.parse_raw(
    """
{
    "messaging_config": {
        "topic": "test-topic",
        "header": {},
        "max_workers": 4,
        "queue_size": 4,
        "max_payload_size": 512000,
        "websocket_url": "ws://127.0.0.1:8000/ws/",
        "producer_url": "",
        "consumer_url": ""
}
}
"""
)

_creator: Callable
if __name__ == "__main__":
    _creator = main
else:
    _creator = _BackendModule.create_model

BackendModule = _creator(
    __name__,
    config=backend_config,
    class_name="BackendModule",
    members=[hello_world, HelloWorld, compute_sum, report_progress_demo],
)
