"""Test backend module

This module exists just for test purposes
"""
import os
import uuid
from typing import ClassVar, List, Literal, Optional, cast

from deprogressapi import PrintReport

from demessaging import config, main

__all__ = ["report_test"]


topic = os.getenv("TEST_TOPIC", "test_topic_" + uuid.uuid4().urn[9:])


config.registry.hard_code(f"topic = '{topic}'")


@config.registry.register_type
class TestReport(PrintReport):
    """Just a test reporter class to see the messaging works."""

    _reports: ClassVar[List[PrintReport]] = []

    report_type: Literal["_test_report_" + topic] = "_test_report_" + topic  # type: ignore

    def show_print(self):
        self._reports.append(self)


def report_test(
    reporter: Optional[TestReport] = TestReport(report_id="test_report"),
) -> TestReport:
    """Test function for using a report via the pulsar.

    Parameters
    ----------
    testreport : Optional[TestReport]
        A reporter object for the test
    """
    reporter = cast(TestReport, TestReport.from_arg(reporter))
    reporter.print("Test report")
    reporter.error("Error report")
    reporter.complete()
    return reporter


if __name__ == "__main__":
    main(messaging_config=dict(topic=topic))
