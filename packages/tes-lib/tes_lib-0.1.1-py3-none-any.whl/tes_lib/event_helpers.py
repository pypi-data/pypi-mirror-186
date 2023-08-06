"""
A collection of helper functions for interacting with the test event store
"""
from typing import List, Dict, Any, Callable, Optional
import copy
import time
from multiprocessing import connection
import requests
import logging

from .defaults import (
    get_default_on_failure,
    get_default_request_timeout,
    get_default_poll_interval,
    get_default_maximum_poll_time,
    get_default_unexpected_event_maximum_poll_time,
    get_default_extended_event_debug_on_expectation_failure,
)
from .test_event import TestEvent
from .expectation import Expectation
from .errors import TesLibError, EventNotFoundError, UnexpectedEventFoundError, ExpectationError
from .library_settings import _TesLibInstance
from .messages import (
    GetAllEventsMessage,
    GetFullEventLogMessage,
    GetEventMessage,
    GetAllMatchingEventsMessage,
    RemoveExpectedEventMessage,
    ExpectEventMessage,
    ExpectEventExtendedDebugMessage,
    DeleteMatchingEventsMessage,
)
from .constants import EVENT_SOURCE_KEY, EVENT_TYPE_KEY, EVENT_ID_KEY, EVENT_STATE_KEY
from .constants import DEFAULT_IP, DEFAULT_PORT, NO_MATCHING_EVENT_FOUND


def wait_for_response(context: str, recv_connection: connection.Connection) -> Any:

    if recv_connection.poll(timeout=get_default_request_timeout()):
        result = recv_connection.recv()
    else:
        logging.warning(
            "No message received from event store, the request_timeout may need increasing"
            f" in the initialise call, context: {context}",
        )
        raise TesLibError(f"No response from event store, context: {context}")
    return result


def get_all_events() -> List[Dict]:
    """Get all events currently in the event store

    :return: A list of events
    """
    tes_lib = _TesLibInstance.get_instance()

    tes_lib.queue.put(GetAllEventsMessage())

    result = wait_for_response("get_all_events", tes_lib.parent_conn)

    return result


def _check_expectations(expectations: List[Expectation]):
    if expectations is None or len(expectations) < 1:
        raise ExpectationError(f"The provided expectation list of '{expectations}' is not valid")


def _event_matches_expectations(event: Dict, expectations: List[Expectation]) -> bool:
    for expectation in expectations:
        if expectation.event_field_name not in event:
            return False

        event_value = event[expectation.event_field_name]
        if not expectation.comparison_function(event_value, expectation.comparison_value):
            return False

    return True


def _log_event_store(
    events: List[Dict],
    order_by: str,
    order_by_default: Any,
    fields_to_log: Optional[List[str]],
    fields_to_exclude: Optional[List[str]],
    filters: Optional[List[Expectation]],
    required_fields: List[str],
):
    if fields_to_log and fields_to_exclude:
        logging.error(
            "fields_to_log and fields_to_exclude have been provided."
            " fields_to_exclude will be ignored"
        )

    # Filter events
    if filters:
        filtered_events = []

        for event in events:
            if _event_matches_expectations(event, filters):
                filtered_events.append(event)

        events = filtered_events

    # Order events
    if order_by != EVENT_ID_KEY:
        events = sorted(events, key=lambda x: (x.get(order_by, order_by_default), x[EVENT_ID_KEY]))
    else:
        events = sorted(events, key=lambda x: x[EVENT_ID_KEY])

    # Filter event fields
    if fields_to_log:
        for event in events:
            # Each event can have different fields so we have to do this every time
            keys_to_remove = [key for key in event.keys() if key not in fields_to_log]

            for field in required_fields:
                if field in keys_to_remove:
                    keys_to_remove.remove(field)

            for key in keys_to_remove:
                del event[key]

    elif fields_to_exclude:

        for field in required_fields:
            if field in fields_to_exclude:
                fields_to_exclude.remove(field)

        for event in events:
            for key in fields_to_exclude:
                if key in event.keys():
                    del event[key]

    logging.info("***** Logging Event Store *****")

    for event in events:
        event_id = event[EVENT_ID_KEY]
        del event[EVENT_ID_KEY]

        # Log the event fields first, helps when trying to find an expected event where the
        # expectations are not quite correct.
        ordered_fields = {}
        if EVENT_SOURCE_KEY in event:
            ordered_fields[EVENT_SOURCE_KEY] = event[EVENT_SOURCE_KEY]
            del event[EVENT_SOURCE_KEY]

        if EVENT_STATE_KEY in event:
            ordered_fields[EVENT_STATE_KEY] = event[EVENT_STATE_KEY]
            del event[EVENT_STATE_KEY]

        if EVENT_TYPE_KEY in event:
            ordered_fields[EVENT_TYPE_KEY] = event[EVENT_TYPE_KEY]
            del event[EVENT_TYPE_KEY]

        ordered_fields = dict(sorted(ordered_fields.items()))
        ordered_fields.update(dict(sorted(event.items())))

        logging.info(f"event_id: {event_id}, {ordered_fields}")

    logging.info("***** End Of Event Store *****")


def log_full_event_store(
    order_by: str = EVENT_ID_KEY,
    order_by_default: Any = None,
    fields_to_log: Optional[List[str]] = None,
    fields_to_exclude: Optional[List[str]] = None,
    filters: Optional[List[Expectation]] = None,
):
    """See log_event_store for param details

    The root logger needs to be configured at info level or below or the events will not be
    displayed

    This function is the same as log_event_store except that it will also contain events that
    have been deleted or removed from the store due to being expected.
    """
    tes_lib = _TesLibInstance.get_instance()

    tes_lib.queue.put(GetFullEventLogMessage())

    events = wait_for_response("log_full_event_store", tes_lib.parent_conn)

    _log_event_store(
        events,
        order_by,
        order_by_default,
        fields_to_log,
        fields_to_exclude,
        filters,
        [EVENT_ID_KEY, EVENT_STATE_KEY],
    )


def log_event_store(
    order_by: str = EVENT_ID_KEY,
    order_by_default: Any = None,
    fields_to_log: Optional[List[str]] = None,
    fields_to_exclude: Optional[List[str]] = None,
    filters: Optional[List[Expectation]] = None,
):
    """Log the current contents of the event store

    The root logger needs to be configured at info level or below or the events will not be
    displayed

    :param order_by: The field events should be ordered by
    :param order_by_default: The value to use when ordering for events that don't have the order_by
                             field
    :param fields_to_log: Event fields to log, all others will be excluded - incompatible with
                          fields_to_exclude. If not provided all fields will be logged. The
                          event_id field will be included even if not specified in the fields_to_log
    :param fields_to_exclude: Fields to exclude, all others will be logged - incompatible with
                              fields_to_log. If not provided all fields will be logged. The
                              event_id field cannot be excluded.
    :param filters: Only log the events that meet the given expectations. If not provided all
                    events will be logged
    :return: None
    """
    events = get_all_events()

    _log_event_store(
        events,
        order_by,
        order_by_default,
        fields_to_log,
        fields_to_exclude,
        filters,
        [EVENT_ID_KEY],
    )


def expect_event(
    expectations: List[Expectation],
    maximum_poll_time: float = 0,
    poll_interval: float = 0,
    on_failure: Optional[Callable] = None,
    extended_event_debug_on_expectation_failure: Optional[bool] = None,
    partial_filter_fields: Optional[List[str]] = None,
) -> Dict:
    """Expect an event - finds the first event that matches all the given expectations in the
    event store. This event is then removed from the event store and returned.

    :param expectations: The list of expectations the event must meet
    :param maximum_poll_time: The amount of time to wait for the event to be found, if not
      provided the default will be used
    :param poll_interval: The time between polling for the event, if not provided the default
      will be used
    :param on_failure: The function to call when we fail to find the expected event, if not
      provided the default will be used
    :param extended_event_debug_on_expectation_failure: Use the less performant but more detailed
      debugging of why no matching event was found in the event store
    :param partial_filter_fields: The names of fields used to perform a partial filter before
      performing a full match, these fields should have expectations for them in the
      `expectations` param or they will not take effect. By default if left blank `event_type`
      and `event_source` will be used if expectations for them are present.
    :return: The found event
    :raises EventNotFoundError: The expected event was not found
    """
    _check_expectations(expectations)

    if maximum_poll_time <= 0:
        maximum_poll_time = get_default_maximum_poll_time()

    if poll_interval <= 0:
        poll_interval = get_default_poll_interval()

    end_time = time.time() + maximum_poll_time
    tes_lib = _TesLibInstance.get_instance()

    if extended_event_debug_on_expectation_failure is None:
        extended_event_debug_on_expectation_failure = (
            get_default_extended_event_debug_on_expectation_failure()
        )

    extended_event_debug_info = []
    returned_event: Any = NO_MATCHING_EVENT_FOUND

    while returned_event is NO_MATCHING_EVENT_FOUND:
        if extended_event_debug_on_expectation_failure:
            tes_lib.queue.put(ExpectEventExtendedDebugMessage(expectations, partial_filter_fields))

            result = wait_for_response("expect_event_extended_debug", tes_lib.parent_conn)
            returned_event = result[0]
            extended_event_debug_info = result[1]
        else:
            tes_lib.queue.put(ExpectEventMessage(expectations))

            returned_event = wait_for_response("expect_event", tes_lib.parent_conn)

        # Note this check is here rather than in the while condition to make sure we always try to
        # query the event store at least once, even if the maximum_poll_time has been set to 0
        if time.time() > end_time:
            break

        if returned_event is NO_MATCHING_EVENT_FOUND:
            time.sleep(poll_interval)

    # Call the on failure if we didn't find the event
    if returned_event == NO_MATCHING_EVENT_FOUND:
        if extended_event_debug_on_expectation_failure:
            if len(extended_event_debug_info) > 0:
                # Order events
                extended_event_debug_info = sorted(
                    extended_event_debug_info, key=lambda x: x["event"][EVENT_ID_KEY]
                )

                logging.info("***** Logging Extended Expectation Failure Debug *****")

                for event_failure_details in extended_event_debug_info:
                    event = event_failure_details["event"]
                    event_id = event[EVENT_ID_KEY]
                    del event[EVENT_ID_KEY]

                    # Log the event fields first, helps when trying to find an expected event
                    # where the expectations are not quite correct.
                    ordered_fields = {}
                    if EVENT_SOURCE_KEY in event:
                        ordered_fields[EVENT_SOURCE_KEY] = event[EVENT_SOURCE_KEY]
                        del event[EVENT_SOURCE_KEY]

                    if EVENT_STATE_KEY in event:
                        ordered_fields[EVENT_STATE_KEY] = event[EVENT_STATE_KEY]
                        del event[EVENT_STATE_KEY]

                    if EVENT_TYPE_KEY in event:
                        ordered_fields[EVENT_TYPE_KEY] = event[EVENT_TYPE_KEY]
                        del event[EVENT_TYPE_KEY]

                    ordered_fields = dict(sorted(ordered_fields.items()))
                    ordered_fields.update(dict(sorted(event.items())))

                    logging.info(f"event_id: {event_id}, {ordered_fields}")

                    # Log the failed expectations
                    for expectation_failure in event_failure_details["expectation_failures"]:
                        logging.info("    {}".format(expectation_failure))

                logging.info("***** End Of Extended Expectation Failure Debug *****")

        if on_failure is None:
            on_failure = get_default_on_failure()

        on_failure()
        raise EventNotFoundError(
            f"Failed to find an event matching the following expectations: {expectations}"
        )

    # Remove the event if we have found it
    tes_lib.queue.put(RemoveExpectedEventMessage(returned_event))
    return returned_event


def dont_expect_event(
    expectations: List[Expectation], maximum_poll_time: float = 0, poll_interval: float = 0
):
    """Don't expect any events in the event store matching the given expectations

    :param expectations: The list of expectations to match against
    :param maximum_poll_time: The amount of time to wait without seeing the event, if
      not provided the default will be used
    :param poll_interval: The time between polling for the event, if not provided the default
                          will be used
    :return: None
    :raises UnexpectedEventFoundError: An unexpected event was found that matches the given
            expectations
    """
    _check_expectations(expectations)
    returned_event = NO_MATCHING_EVENT_FOUND

    if maximum_poll_time <= 0:
        maximum_poll_time = get_default_unexpected_event_maximum_poll_time()

    if poll_interval <= 0:
        poll_interval = get_default_poll_interval()

    end_time = time.time() + maximum_poll_time
    tes_lib = _TesLibInstance.get_instance()

    while returned_event is NO_MATCHING_EVENT_FOUND and time.time() < end_time:
        tes_lib.queue.put(ExpectEventMessage(expectations))

        returned_event = wait_for_response("expect_event", tes_lib.parent_conn)

        if returned_event is NO_MATCHING_EVENT_FOUND:
            time.sleep(poll_interval)

    if returned_event != NO_MATCHING_EVENT_FOUND:
        raise UnexpectedEventFoundError(
            f"An unexpected event {returned_event} was found"
            f" matching the following expectations {expectations}"
        )


def get_event(
    expectations: List[Expectation],
    maximum_poll_time: float = 0,
    poll_interval: float = 0,
    on_failure: Optional[Callable] = None,
) -> Dict:
    """Get an event - finds the first event that matches all the given expectations in the
    event store.

    :param expectations: The list of expectations the event must meet
    :param maximum_poll_time: The amount of time to wait for the event to be found, if not
      provided the default will be used
    :param poll_interval: The time between polling for the event, if not provided the default
      will be used
    :param on_failure: The function to call when we fail to find the event, if not provided the
      default will be used
    :return: The found event
    :raises EventNotFoundError: The event was not found
    """
    _check_expectations(expectations)
    returned_event: Any = NO_MATCHING_EVENT_FOUND

    if maximum_poll_time <= 0:
        maximum_poll_time = get_default_maximum_poll_time()

    if poll_interval <= 0:
        poll_interval = get_default_poll_interval()

    end_time = time.time() + maximum_poll_time
    tes_lib = _TesLibInstance.get_instance()

    while returned_event is NO_MATCHING_EVENT_FOUND and time.time() < end_time:
        tes_lib.queue.put(GetEventMessage(expectations))

        returned_event = wait_for_response("get_event", tes_lib.parent_conn)

        if returned_event is NO_MATCHING_EVENT_FOUND:
            time.sleep(poll_interval)

    if returned_event == NO_MATCHING_EVENT_FOUND:
        if on_failure is None:
            on_failure = get_default_on_failure()

        on_failure()
        raise EventNotFoundError(
            f"Failed to find an event matching the following expectations: {expectations}"
        )

    return returned_event


def get_all_matching_events(expectations: List[Expectation]) -> List[Dict]:
    """Get all events from the store that match the given expectations

    :param expectations: The list of expectations the event must meet
    :param timeout: The amount of time to wait for the matching events to be returned
    :param poll_interval: The time between polling for the event
    :return: A list of the events found
    """
    _check_expectations(expectations)
    tes_lib = _TesLibInstance.get_instance()
    tes_lib.queue.put(GetAllMatchingEventsMessage(expectations))

    events = wait_for_response("get_all_matching_events", tes_lib.parent_conn)

    return events


def delete_all_matching_events(expectations: List[Expectation]) -> int:
    """Delete all events from the store that match the given expectations

    :param expectations: The list of expectations the event must meet
    :param timeout: The amount of time to wait for the matching events to be deleted
    :param poll_interval: The time between polling for the event
    :return: The number of events deleted
    """
    _check_expectations(expectations)
    tes_lib = _TesLibInstance.get_instance()
    tes_lib.queue.put(DeleteMatchingEventsMessage(expectations))

    num_events_removed = wait_for_response(
        "delete_all_matching_events",
        tes_lib.parent_conn,
    )

    return int(num_events_removed)


def add_raw_event(
    event_source: str,
    event_type: Any,
    additional_event_params: Dict,
    ip_address: str = DEFAULT_IP,
    port: int = DEFAULT_PORT,
):
    """Add an event to the event store by fields rather than via a TestEvent

    This is a helper function which will make a POST request to the add event webserver

    :param event_source: The name of the event source
    :param event_type: The event type
    :param additional_event_params: A json compatible dictionary of field_name to field_value
                                    Note a copy of this dictionary will be taken
    :param ip_address: The ip address of the add event webserver
    :param port: The port of the add event webserver
    :return: None
    :raises TesLibError: An error occurred adding the event to the event store
    """
    url = f"http://{ip_address}:{port}/add"

    event_params = copy.deepcopy(additional_event_params)
    event_params[EVENT_SOURCE_KEY] = event_source
    event_params[EVENT_TYPE_KEY] = event_type

    response = requests.post(url=url, json=event_params)
    # Works fine pylint just doesn't understand what's going on
    # pylint: disable=no-member
    if response.status_code != requests.codes.ok:
        raise TesLibError(f"Failed to add event to the store: {response.text}")


def add_event(test_event: TestEvent, ip_address: str = DEFAULT_IP, port: int = DEFAULT_PORT):
    """Add an event to the event store

    This is a helper function which will make a POST request to the add event webserver

    :param test_event: A TestEvent instance
    :param ip_address: The ip address of the add event webserver
    :param port: The port of the add event webserver
    :return: None
    :raises TesLibError: An error occurred adding the event to the event store
    """
    url = f"http://{ip_address}:{port}/add"

    event_params = vars(test_event)

    response = requests.post(url=url, json=event_params)
    # Works fine pylint just doesn't understand what's going on
    # pylint: disable=no-member
    if response.status_code != requests.codes.ok:
        raise TesLibError(f"Failed to add event to the store: {response.text}")
