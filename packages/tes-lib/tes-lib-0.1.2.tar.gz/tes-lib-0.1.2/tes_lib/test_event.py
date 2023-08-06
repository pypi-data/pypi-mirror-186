"""Test Event class"""
import operator
from typing import List, Any
from .expectation import Expectation
from .constants import EVENT_TYPE_KEY, EVENT_SOURCE_KEY


class TestEvent:
    """Base Test Event class which contains the required fields

    This class is expected to be subclassed and then the subclass passed to the add_event function.

    All fields in the subclass should be able to be encoded in json
    """

    def __init__(self, event_source: str, event_type: Any):
        self.event_source = event_source
        self.event_type = event_type

    def get_expectations(self) -> List[Expectation]:
        """Get the default expectations

        :return: A list of expectations
        """
        return [
            Expectation(EVENT_SOURCE_KEY, operator.eq, self.event_source),
            Expectation(EVENT_TYPE_KEY, operator.eq, self.event_type),
        ]
