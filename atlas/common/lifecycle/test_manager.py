from common.lifecycle.lifecycle_manager import LifecycleManager
from common.lifecycle.lifecycle_state import LifecycleState


manager = LifecycleManager()

print(manager.current())

manager.transition_to(
    LifecycleState.INITIALIZING
)

manager.transition_to(
    LifecycleState.INITIALIZED
)

manager.transition_to(
    LifecycleState.CONFIGURING
)

manager.transition_to(
    LifecycleState.READY
)

print(manager.current())

print(manager.previous())

print()

print("History")

for timestamp, state in manager.history:

    print(

        timestamp,

        state.name
    )