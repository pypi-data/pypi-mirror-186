"""
This file contains the message definitions for messages passed to the event store process via
the request multiprocessing queue
"""


class _BaseMessage:
    def __init__(self, message_type):
        self.message_type = message_type


class ShutdownMessage(_BaseMessage):
    TYPE = "SHUTDOWN"

    def __init__(self):
        super().__init__(ShutdownMessage.TYPE)


class ResetMessage(_BaseMessage):
    TYPE = "RESET"

    def __init__(self):
        super().__init__(ResetMessage.TYPE)


class GetAllEventsMessage(_BaseMessage):
    TYPE = "GET_ALL"

    def __init__(self):
        super().__init__(GetAllEventsMessage.TYPE)


class GetFullEventLogMessage(_BaseMessage):
    TYPE = "GET_FULL"

    def __init__(self):
        super().__init__(GetFullEventLogMessage.TYPE)


class GetEventMessage(_BaseMessage):
    TYPE = "GET_EVENT"

    def __init__(self, expectations):
        super().__init__(GetEventMessage.TYPE)
        self.expectations = expectations


class GetAllMatchingEventsMessage(_BaseMessage):
    TYPE = "GET_MATCHING"

    def __init__(self, expectations):
        super().__init__(GetAllMatchingEventsMessage.TYPE)
        self.expectations = expectations


class AddEventMessage(_BaseMessage):
    TYPE = "ADD"

    def __init__(self, event_fields):
        super().__init__(AddEventMessage.TYPE)
        self.event_fields = event_fields


class ExpectEventMessage(_BaseMessage):
    TYPE = "EXPECT"

    def __init__(self, expectations):
        super().__init__(ExpectEventMessage.TYPE)
        self.expectations = expectations


class ExpectEventExtendedDebugMessage(_BaseMessage):
    TYPE = "EXPECT_EXTENDED_DEBUG"

    def __init__(self, expectations, partial_filter_fields=None):
        super().__init__(ExpectEventExtendedDebugMessage.TYPE)
        self.expectations = expectations
        self.partial_filter_fields = partial_filter_fields


class RemoveExpectedEventMessage(_BaseMessage):
    TYPE = "REMOVE_EXPECTED"

    def __init__(self, event):
        super().__init__(RemoveExpectedEventMessage.TYPE)
        self.event = event


class DeleteMatchingEventsMessage(_BaseMessage):
    TYPE = "DELETE_MATCHING"

    def __init__(self, expectations):
        super().__init__(DeleteMatchingEventsMessage.TYPE)
        self.expectations = expectations
