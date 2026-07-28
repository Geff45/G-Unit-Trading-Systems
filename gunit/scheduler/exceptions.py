"""
Scheduler exceptions.
"""


class SchedulerError(Exception):
    """
    Base scheduler exception.
    """


class DuplicateJobError(SchedulerError):
    """
    Raised when a job is registered twice.
    """


class JobNotFoundError(SchedulerError):
    """
    Raised when a job cannot be found.
    """