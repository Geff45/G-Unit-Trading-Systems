from kernel.logging.log_entry import LogEntry
from kernel.logging.log_level import LogLevel


class AtlasLogger:

    def __init__(self):

        self._entries = []

    def log(self, level, source, message):

        self._entries.append(

            LogEntry(

                level=level,

                source=source,

                message=message,

            )

        )

    def info(self, source, message):

        self.log(LogLevel.INFO, source, message)

    def warning(self, source, message):

        self.log(LogLevel.WARNING, source, message)

    def error(self, source, message):

        self.log(LogLevel.ERROR, source, message)

    def entries(self):

        return self._entries