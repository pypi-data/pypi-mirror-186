"""
tes-lib

A library to enable asynchronous event based testing of complex systems.
"""
from typing import Callable

from .constants import (
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_MAXIMUM_POLL_TIME,
    DEFAULT_UNEXPECTED_EVENT_MAXIMUM_POLL_TIME,
    DEFAULT_EXTENDED_EVENT_DEBUG,
)
from .library_settings import _TesLibInstance
from .expectation import Expectation
from .event_helpers import (
    expect_event,
    add_event,
    add_raw_event,
    get_event,
    get_all_events,
    delete_all_matching_events,
    get_all_matching_events,
    log_event_store,
    log_full_event_store,
    dont_expect_event,
)
from .errors import TesLibError, EventNotFoundError, UnexpectedEventFoundError
from .test_event import TestEvent
from .constants import DEFAULT_PORT, DEFAULT_IP

# Note: These functions are here to allow them to use defaults from the event helpers such as
# log_event_store. If they were in the library_settings module that module would want to
# import event_helpers which imports library_settings creating a circular import loop


def initialise(
    ip_address: str = DEFAULT_IP,
    port: int = DEFAULT_PORT,
    on_failure: Callable = log_event_store,
    request_timeout: float = DEFAULT_REQUEST_TIMEOUT,
    poll_interval: float = DEFAULT_POLL_INTERVAL,
    maximum_poll_time: float = DEFAULT_MAXIMUM_POLL_TIME,
    unexpected_event_maximum_poll_time: float = DEFAULT_UNEXPECTED_EVENT_MAXIMUM_POLL_TIME,
    extended_event_debug_on_expectation_failure: bool = DEFAULT_EXTENDED_EVENT_DEBUG,
):
    """Initialise the library - this will start the event store and webserver processes. Each call
    of initialise should be paired with a call to cleanup.

    Calling this function multiple times without calling cleanup between will have no effect

    :param ip_address: The IP address to be used by the add event webserver
    :param port: The port to be used by the add event webserver
    :param on_failure: The default function to be called when an expectation failure occurs
    :param request_timeout: The maximum amount of time to wait for a response from the event store,
      see the performance section of the docs for guidance on setting this value
    :param poll_interval: How often to poll when repeatedly checking the event store
    :param maximum_poll_time: The maximum amount of time to keep polling the event store when
      repeatedly checking
    :param unexpected_event_maximum_poll_time: The maximum amount of time to keep polling the event
      store when repeatedly checking an event has not occurred
    :param extended_event_debug_on_expectation_failure: Should more information about why events
      didn't match be displayed on expectation failure
    :return: None
    """
    _TesLibInstance.get_instance().initialise(
        ip_address,
        port,
        on_failure,
        poll_interval,
        request_timeout,
        maximum_poll_time,
        unexpected_event_maximum_poll_time,
        extended_event_debug_on_expectation_failure,
    )


def reset_event_store():
    """Reset the test event store removing all event. This function will call cleanup followed by
    initialise if it fails to reset the event store.

    Calling this function without first calling initialise will have no effect

    :return: None
    """
    _TesLibInstance.get_instance().reset()


def cleanup():
    """Cleanup the library - this will stop the event store and webserver processes

    Calling this function multiple times without calling initialise between will have no effect

    :return: None
    """
    _TesLibInstance.get_instance().cleanup()


__all__ = [
    "initialise",
    "cleanup",
    "reset_event_store",
    "Expectation",
    "add_event",
    "add_raw_event",
    "delete_all_matching_events",
    "dont_expect_event",
    "expect_event",
    "get_event",
    "get_all_events",
    "get_all_matching_events",
    "log_event_store",
    "log_full_event_store",
    "EventNotFoundError",
    "TesLibError",
    "UnexpectedEventFoundError",
    "TestEvent",
]
