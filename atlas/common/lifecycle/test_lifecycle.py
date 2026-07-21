from common.lifecycle.lifecycle_state import LifecycleState
from common.lifecycle.lifecycle_validator import is_valid_transition


tests = [

    (
        LifecycleState.CREATED,
        LifecycleState.INITIALIZING
    ),

    (
        LifecycleState.RUNNING,
        LifecycleState.PAUSING
    ),

    (
        LifecycleState.RUNNING,
        LifecycleState.CREATED
    ),

    (
        LifecycleState.PAUSED,
        LifecycleState.RESUMING
    ),

]


for current, target in tests:

    print(
        current.name,
        "->",
        target.name,
        "=",
        is_valid_transition(current, target)
    )