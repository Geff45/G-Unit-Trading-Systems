from sdk_manager import SDK

from version import version



print(
    version()
)



print(
    SDK.register(
        "Deployment"
    )
)


print(
    SDK.register(
        "Trading-System"
    )
)


print(
    SDK.info()
)