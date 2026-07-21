from registry import CLI

from commands.base import Command



build = Command(
    "build"
)


deploy = Command(
    "deploy"
)



print(
    CLI.register(build)
)


print(
    CLI.register(deploy)
)



print(
    CLI.list()
)



print(
    build.execute()
)