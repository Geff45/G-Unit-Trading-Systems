from common.results.result import Result
from common.results.error import AtlasError
from common.results.error_codes import ErrorCode


good = Result.ok("Atlas Ready")

bad = Result.fail(

    AtlasError(

        ErrorCode.STARTUP_ERROR,

        "Kernel failed",

        "Kernel"

    )

)

print(good)

print()

print(bad)