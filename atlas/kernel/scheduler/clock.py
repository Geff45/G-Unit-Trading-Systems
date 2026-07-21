from datetime import datetime, UTC


class AtlasClock:

    def now(self):
        return datetime.now(UTC)