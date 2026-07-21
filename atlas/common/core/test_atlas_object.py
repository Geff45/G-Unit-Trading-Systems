from common.core.atlas_object import AtlasObject

from common.identity.identity_types import IdentityType

from common.lifecycle.lifecycle_state import LifecycleState


runtime = AtlasObject(

    "Runtime",

    IdentityType.SERVICE

)

print(runtime.info())

runtime.lifecycle.transition_to(
    LifecycleState.INITIALIZING
)

runtime.lifecycle.transition_to(
    LifecycleState.INITIALIZED
)

print(runtime.info())