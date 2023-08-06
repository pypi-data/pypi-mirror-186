"""
The library settings and state
"""
import time
from multiprocessing import Queue, Pipe, Process
from typing import Callable
import requests
import logging

from .defaults import setup_library_defaults
from .errors import TesLibError
from .test_event_store import event_store_run_loop
from .add_event_web_server import run_webserver
from .messages import ShutdownMessage, ResetMessage
from .constants import DEFAULT_PORT, DEFAULT_IP


class _TesLib:
    def __init__(self):
        self.queue = Queue()
        self.parent_conn, self.child_conn = Pipe()

        self.ip_address = DEFAULT_IP
        self.port = DEFAULT_PORT

        self.event_store_process = None
        self.webserver_process = None

        self._initialised = False

    @staticmethod
    def wait_for_webserver(ip_address: str, port: int):
        """Wait for the webserver to be up and ready

        :param ip_address: The ip_address the webserver is listening
        :param port: The port the webserver is listening on
        :return: None
        """
        timeout = 5
        url = f"http://{ip_address}:{port}/ready"
        for _ in range(timeout):
            try:
                response = requests.get(url=url)
                # Works fine pylint just doesn't understand what's going on
                # pylint: disable=no-member
                if response.status_code == requests.codes.ok:
                    return
            except requests.exceptions.ConnectionError:
                # Webserver may not be ready to listen yet - this is what we're trying to check
                # so is expected behaviour
                pass

            time.sleep(1)

        raise RuntimeError(
            "Failed to initialise library - no response from add event webserver before timeout"
        )

    def _initialise(self, ip_address: str, port: int):
        """Initialise the library

        :param ip_address: The ip_address the webserver should  listen on
        :param port: The port the webserver should listen on
        :return: None
        """
        if self._initialised:
            return

        self.ip_address = ip_address
        self.port = port

        self.event_store_process = Process(
            target=event_store_run_loop, args=(self.queue, self.child_conn)
        )
        self.event_store_process.start()
        self.webserver_process = Process(target=run_webserver, args=(self.queue, ip_address, port))
        self.webserver_process.start()

        self.wait_for_webserver(ip_address, port)

        self._initialised = True

    def initialise(
        self,
        ip_address: str,
        port: int,
        on_failure: Callable,
        request_timeout: float,
        poll_interval: float,
        maximum_poll_time: float,
        unexpected_event_maximum_poll_time: float,
        extended_event_debug_on_expectation_failure: bool,
    ):
        """Initialise the library

        :param ip_address: The ip_address the webserver should  listen on
        :param port: The port the webserver should listen on
        :param on_failure: The default function to be called when an expectation failure occurs
        :param request_timeout: The maximum amount of time to wait for a response from the event
          store
        :param poll_interval: How often to poll when repeatedly checking the event store
        :param maximum_poll_time: The maximum amount of time to keep polling the event store
          when repeatedly checking
        :param unexpected_event_maximum_poll_time: The maximum amount of time to keep polling
          the event store when repeatedly checking an event has not occurred
        :param extended_event_debug_on_expectation_failure: Should more information about why
          events didn't match be displayed on expectation failure
        :return: None
        """
        if self._initialised:
            return

        setup_library_defaults(
            on_failure,
            poll_interval,
            request_timeout,
            maximum_poll_time,
            unexpected_event_maximum_poll_time,
            extended_event_debug_on_expectation_failure,
        )

        self._initialise(ip_address, port)

    def reset(self, timeout=5):
        """Reset the event store ready for the next test run

        :param timeout: The amount of time to give the event store to reset
        :return: None
        """
        if not self._initialised:
            return

        self.queue.put(ResetMessage())

        # pylint: disable=cyclic-import,import-outside-toplevel
        from .event_helpers import wait_for_response

        try:
            _ = wait_for_response("Reset test event store", self.parent_conn)
        except TesLibError:
            # If we don't get a response reset the library
            logging.error("No response from event store on reset - restarting processes")

            self.cleanup()
            self._initialise(self.ip_address, self.port)

    def cleanup(self):
        """Cleanup the library

        :return: None
        """
        if not self._initialised:
            return

        self.queue.put(ShutdownMessage())
        self.event_store_process.join(timeout=3)
        self.webserver_process.terminate()
        self.webserver_process.join(timeout=3)

        self._initialised = False


class _TesLibInstance:

    INSTANCE = None

    @staticmethod
    def get_instance():
        """Get an instance of the TesLib class

        :return: TesLib instance
        """
        if _TesLibInstance.INSTANCE is None:
            _TesLibInstance.INSTANCE = _TesLib()
        return _TesLibInstance.INSTANCE
