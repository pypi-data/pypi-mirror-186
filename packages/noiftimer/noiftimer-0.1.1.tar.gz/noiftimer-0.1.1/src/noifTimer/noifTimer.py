from datetime import datetime


class Timer:
    """Simple timer class that tracks total elapsed time
    and average time between calls to 'start' and 'stop'."""

    def __init__(self, averagingWindowLength: int = 10, subsecondFormat: bool = False):
        """:param averagingWindowLength: Number of start/stop cycles
        to calculate the average elapsed time with.\n
        :param subsecondFormat: If True, formatTime() will
        include milliseconds and microseconds with its return string."""
        self.startTime = datetime.now()
        self.stopTime = datetime.now()
        self.averageElapsedTime = 0
        self.history = []
        self.elapsedTime = 0
        self.averagingWindowLength = averagingWindowLength
        self.subsecondFormat = subsecondFormat
        self.started = False

    def start(self):
        """Start timer."""
        self.startTime = datetime.now()
        self.started = True

    def stop(self):
        """Stop timer.

        Calculates elapsed time and average elapsed time."""
        self.stopTime = datetime.now()
        self.started = False
        self.elapsedTime = (self.stopTime - self.startTime).total_seconds()
        self._saveElapsedTime()
        self.averageElapsedTime = sum(self.history) / (len(self.history))

    def _saveElapsedTime(self):
        """Saves current elapsed time to the history buffer
        in a FIFO manner."""
        if len(self.history) >= self.averagingWindowLength:
            self.history.pop(0)
        self.history.append(self.elapsedTime)

    def checkTime(self, format: bool = True) -> float | str:
        """Returns current elapsed without stopping the timer.

        :param format: If True, elapsed time is returned as a string.
        If False, elapsed time is returned as a float."""
        self.elapsedTime = (datetime.now() - self.startTime).total_seconds()
        return self.formatTime(self.elapsedTime) if format else self.elapsedTime

    def _getTimeUnit(
        self, numSeconds: float, secondsPerUnit: float, unitSuffix: str
    ) -> tuple[float, str]:
        """Determines the number of units in a given number of seconds
        by integer division.

        Returns a tuple containing the remaining number of seconds after division
        as well as the number of units as a string with 'unitSuffix' appended to the string.

        e.g. _getTimeUnit(124, 60, 'm') will return (4, '2m')"""
        numUnits = int(numSeconds / secondsPerUnit)
        if numUnits > 0:
            remainder = numSeconds - (numUnits * secondsPerUnit)
            return (remainder, f"{numUnits}{unitSuffix}")
        else:
            return (numSeconds, "")

    def formatTime(self, numSeconds: float) -> str:
        """Returns numSeconds as a string with units."""
        microsecond = 0.000001
        millisecond = 0.001
        second = 1
        secondsPerMinute = 60
        secondsPerHour = secondsPerMinute * 60
        secondsPerDay = secondsPerHour * 24
        secondsPerWeek = secondsPerDay * 7
        secondsPerMonth = secondsPerWeek * 4
        secondsPerYear = secondsPerMonth * 12
        timeUnits = [
            (secondsPerYear, "y"),
            (secondsPerMonth, "mn"),
            (secondsPerWeek, "w"),
            (secondsPerDay, "d"),
            (secondsPerHour, "h"),
            (secondsPerMinute, "m"),
            (second, "s"),
            (millisecond, "ms"),
            (microsecond, "us"),
        ]
        if not self.subsecondFormat:
            timeUnits = timeUnits[:-2]
        timeString = ""
        for timeUnit in timeUnits:
            numSeconds, unitString = self._getTimeUnit(
                numSeconds, timeUnit[0], timeUnit[1]
            )
            if unitString != "":
                timeString += f"{unitString} "
        return timeString

    def getStats(self, format: bool = True) -> str:
        """Returns string for elapsed time and average elapsed time."""
        if format:
            return f"elapsed time: {self.formatTime(self.elapsedTime)}\naverage elapsed time: {self.formatTime(self.averageElapsedTime)}"
        else:
            return f"elapsed time: {self.elapsedTime}s\naverage elapsed time: {self.averageElapsedTime}s"
