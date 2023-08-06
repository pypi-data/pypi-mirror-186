"""
Add event webserver - this webserver accepts POST requests of events which, if they are valid,
will be added to the event store
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import multiprocessing
from typing import Any
from .messages import AddEventMessage
from .constants import EVENT_TYPE_KEY, EVENT_SOURCE_KEY

_EVENT_QUEUE = None


class _AddEventWebServer(BaseHTTPRequestHandler):
    def _set_bad_request_headers(self, error_msg: str):
        """Set the headers on the response for a 400 bad request

        :param error_msg: The error message to return
        :return: None
        """
        self.send_response(400)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(str.encode(error_msg))

    def _set_not_found_headers(self):
        """Set the headers on the response for a 404 not found

        :return: None
        """
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _set_okay_headers(self):
        """Set the headers on the response for a 200 okay

        :return: None
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Handle a GET request

        This function is used to provide an easy way to check if the webserver is up and running

        :return: None
        """
        if self.path == "/ready":
            self._set_okay_headers()
            self.wfile.write(b"Ready")
        else:
            self._set_not_found_headers()

    def do_POST(self):
        """Handle a POST request

        :return: None
        """
        if self.path == "/add":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            try:
                event_data = json.loads(post_data)
            except json.JSONDecodeError as exc:
                self._set_bad_request_headers(f"Failed to decode message as json: {exc}")
            else:
                if EVENT_TYPE_KEY not in event_data:
                    self._set_bad_request_headers(f"{EVENT_TYPE_KEY} key not in message")
                elif EVENT_SOURCE_KEY not in event_data:
                    self._set_bad_request_headers(f"{EVENT_SOURCE_KEY} key not in message")
                else:
                    _EVENT_QUEUE.put(AddEventMessage(event_data))
                    self._set_okay_headers()
        else:
            self._set_not_found_headers()

    def log_message(self, format: str, *args: Any) -> None:
        # Override the logging to stop it spamming the test output, it's not useful anyway,
        # for example:
        #   127.0.0.1 - - [24/Jul/2022 09:21:54] "POST /add HTTP/1.1" 200 -
        pass


def run_webserver(queue: multiprocessing.Queue, ip_address: str, port: int):
    """Run the add event webserver - note this function call will block as it calls serve_forever

    :param queue: A multiprocessing queue for putting event requests onto
    :param ip_address: The ip_address to listen on
    :param port: The port the webserver should listen on
    :return: None
    """
    global _EVENT_QUEUE
    _EVENT_QUEUE = queue
    server_address = (ip_address, port)
    httpd = HTTPServer(server_address, _AddEventWebServer)
    httpd.serve_forever()
