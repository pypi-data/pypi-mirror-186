"""
Expectation definition
"""
from typing import Any, Callable


class Expectation:
    """
    Expectation definition - should be used with the event helper functions
    """

    def __init__(self, event_field_name: str, comparison_function: Callable, comparison_value: Any):
        self.event_field_name = event_field_name
        self.comparison_function = comparison_function
        self.comparison_value = comparison_value

    def __repr__(self):
        return (
            f"field: '{self.event_field_name}',"
            f" operator: '{self.comparison_function.__name__}',"
            f" comparison value: '{self.comparison_value}'"
        )
