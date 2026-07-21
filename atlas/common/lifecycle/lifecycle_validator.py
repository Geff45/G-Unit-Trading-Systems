"""
Lifecycle transition validation for Atlas services.
"""

from common.lifecycle.lifecycle_state import LifecycleState


_ALLOWED_TRANSITIONS = {

    LifecycleState.CREATED: {
        LifecycleState.INITIALIZING
    },

    LifecycleState.INITIALIZING: {
        LifecycleState.INITIALIZED,
        LifecycleState.FAILED
    },

    LifecycleState.INITIALIZED: {
        LifecycleState.CONFIGURING,
        LifecycleState.SHUTTING_DOWN
    },

    LifecycleState.CONFIGURING: {
        LifecycleState.READY,
        LifecycleState.FAILED
    },

    LifecycleState.READY: {
        LifecycleState.STARTING,
        LifecycleState.SHUTTING_DOWN
    },

    LifecycleState.STARTING: {
        LifecycleState.RUNNING,
        LifecycleState.FAILED
    },

    LifecycleState.RUNNING: {
        LifecycleState.PAUSING,
        LifecycleState.STOPPING,
        LifecycleState.FAILED
    },

    LifecycleState.PAUSING: {
        LifecycleState.PAUSED
    },

    LifecycleState.PAUSED: {
        LifecycleState.RESUMING,
        LifecycleState.STOPPING
    },

    LifecycleState.RESUMING: {
        LifecycleState.RUNNING
    },

    LifecycleState.STOPPING: {
        LifecycleState.STOPPED
    },

    LifecycleState.STOPPED: {
        LifecycleState.STARTING,
        LifecycleState.SHUTTING_DOWN
    },

    LifecycleState.SHUTTING_DOWN: {
        LifecycleState.SHUTDOWN
    },

    LifecycleState.FAILED: {
        LifecycleState.SHUTTING_DOWN,
        LifecycleState.STOPPING
    },

    LifecycleState.SHUTDOWN: set(),

    LifecycleState.UNKNOWN: {
        LifecycleState.CREATED
    },
}


def is_valid_transition(
    current: LifecycleState,
    target: LifecycleState,
) -> bool:
    """
    Check whether a lifecycle transition is legal.
    """

    return target in _ALLOWED_TRANSITIONS.get(current, set())