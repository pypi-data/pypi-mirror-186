"""Defaults that can be optionally overridden"""
from typing import Callable


# This exists only to shut mypy up
def _on_failure():
    pass


class Defaults:
    ON_FAILURE = _on_failure
    REQUEST_TIMEOUT = 0.0
    POLL_INTERVAL = 0.0
    MAXIMUM_POLL_TIME = 0.0
    UNEXPECTED_EVENT_MAXIMUM_POLL_TIME = 0.0
    EXTENDED_EVENT_DEBUG_ON_EXPECTATION_FAILURE = True


def setup_library_defaults(
    on_failure: Callable,
    request_timeout: float,
    poll_interval: float,
    maximum_poll_time: float,
    unexpected_event_maximum_poll_time: float,
    extended_event_debug_on_expectation_failure: bool,
):
    Defaults.ON_FAILURE = on_failure
    Defaults.REQUEST_TIMEOUT = request_timeout
    Defaults.POLL_INTERVAL = poll_interval
    Defaults.MAXIMUM_POLL_TIME = maximum_poll_time
    Defaults.UNEXPECTED_EVENT_MAXIMUM_POLL_TIME = unexpected_event_maximum_poll_time
    Defaults.EXTENDED_EVENT_DEBUG_ON_EXPECTATION_FAILURE = (
        extended_event_debug_on_expectation_failure
    )


def get_default_on_failure() -> Callable:
    return Defaults.ON_FAILURE


def get_default_poll_interval() -> float:
    return Defaults.POLL_INTERVAL


def get_default_request_timeout() -> float:
    return Defaults.REQUEST_TIMEOUT


def get_default_maximum_poll_time() -> float:
    return Defaults.MAXIMUM_POLL_TIME


def get_default_unexpected_event_maximum_poll_time() -> float:
    return Defaults.UNEXPECTED_EVENT_MAXIMUM_POLL_TIME


def get_default_extended_event_debug_on_expectation_failure() -> bool:
    return Defaults.EXTENDED_EVENT_DEBUG_ON_EXPECTATION_FAILURE
