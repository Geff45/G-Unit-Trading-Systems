from auth import Auth

from permissions import Permissions



auth = Auth()


print(
    auth.register(
        "G-Unit"
    )
)



print(
    auth.verify(
        "G-Unit"
    )
)



permissions = Permissions()


print(
    permissions.assign(
        "G-Unit",
        "admin"
    )
)



print(
    permissions.check(
        "G-Unit",
        "admin"
    )
)