from dataclasses import dataclass

from common.results.error_codes import ErrorCode


@dataclass(slots=True, frozen=True)
class AtlasError:

    code: ErrorCode

    message: str

    source: str