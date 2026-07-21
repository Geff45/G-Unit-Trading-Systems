from common.identity.identity import Identity

from common.identity.identity_registry import IdentityRegistry

from common.identity.identity_types import IdentityType


registry = IdentityRegistry()

runtime = Identity.create(

    "Runtime",

    IdentityType.SERVICE

)

kernel = Identity.create(

    "Kernel",

    IdentityType.KERNEL

)

registry.register(runtime)

registry.register(kernel)

print(registry.count())

for item in registry.all():

    print(item)