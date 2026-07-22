class EventError(Exception):
    """
    Base event exception.
    """


class DuplicateSubscription(EventError):
    """
    Handler already subscribed.
    """


class EventNotRegistered(EventError):
    """
    Unknown event.
    """


class HandlerFailed(EventError):
    """
    Handler execution failed.
    """