from datetime import datetime

class LoggerClass(object):
    def __init__(self, logfile=None):
        self._logger = None
        self._logfile = None

        # open logger handler
        if logfile:
            self._logfile = logfile
            self._logger = open(logfile, "a")
            print(f"Logger {self._logfile} opened")

    def __new__(cls, logfile=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggerClass, cls).__new__(cls)
        return cls.instance

    def __del__(self):
        # closing handler if needed
        if self._logger:
            self._logger.close()
            print(f"Logger {self._logfile} closed")

    def __str__(self):
        if self._logger:
            return f"handler is open"
        return "handler is closed"


    def _now(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    def info(self, msg):
        if self._logger:
            self._logger.write(f"{self._now()} info: {msg}\n")

    def debug(self, msg):
        if self._logger:
            self._logger.write(f"{self._now()} debug: {msg}\n")


if __name__ == "__main__":
    # a = 1.31
    # b = 1.31
    # if hex(id(a)) == hex(id(b)):
    #     print(f"Same: {hex(id(a))} vs. {hex(id(b))}")
    # else:
    #     print(f"Not Same: {hex(id(a))} vs. {hex(id(b))}")

    log = LoggerClass("logger-test")
    log.info("Hello World!")
