from os import get_terminal_size
from time import sleep
from typing import Any

from noifTimer import Timer


def clear():
    """Erase the current line from the terminal."""
    print(" " * (get_terminal_size().columns - 1), flush=True, end="\r")


def printInPlace(string: str, animate: bool = False, animateRefresh: float = 0.01):
    """Calls to printInPlace will overwrite
    the previous line of text in the terminal
    with the 'string' param.

    :param animate: Will cause the string
    to be printed to the terminal
    one character at a time.

    :param animateRefresh: Number of seconds
    between the addition of characters
    when 'animate' is True."""
    clear()
    string = str(string)
    width = get_terminal_size().columns
    string = string[: width - 2]
    if animate:
        for i in range(len(string)):
            print(f"{string[:i+1]}", flush=True, end=" \r")
            sleep(animateRefresh)
    else:
        print(string, flush=True, end="\r")


def ticker(info: list[str]):
    """Prints info to terminal with
    top and bottom padding so that repeated
    calls print info without showing previous
    outputs from ticker calls.

    Similar visually to printInPlace,
    but for multiple lines."""
    width = get_terminal_size().columns
    info = [str(line)[: width - 1] for line in info]
    height = get_terminal_size().lines - len(info)
    print("\n" * (height * 2), end="")
    print(*info, sep="\n", end="")
    print("\n" * (int((height) / 2)), end="")


class ProgBar:
    """Self incrementing, dynamically sized progress bar.

    Includes a Timer object from loopTimer that starts timing
    on the first call to display and stops timing once
    self.counter >= self.total.
    It can be easily added to the progress bar display by calling
    Timer's checkTime function and passing the value to the 'prefix' or 'suffix'
    param of self.display():

    bar = ProgBar(total=someTotal)
    bar.display(prefix=f"Run time: {bar.timer.checkTime()}")"""

    def __init__(
        self,
        total: float,
        fillCh: str = "_",
        unfillCh: str = "/",
        widthRatio: float = 0.75,
        newLineAfterCompletion: bool = True,
        clearAfterCompletion: bool = False,
    ):
        """:param total: The number of calls to reach 100% completion.

        :param fillCh: The character used to represent the completed part of the bar.

        :param unfillCh: The character used to represent the uncompleted part of the bar.

        :param widthRatio: The width of the progress bar relative to the width of the terminal window.

        :param newLineAfterCompletion: Make a call to print() once self.counter >= self.total.

        :param clearAfterCompletion: Make a call to printBuddies.clear() once self.counter >= self.total.

        Note: if newLineAfterCompletion and clearAfterCompletion are both True, the line will be cleared
        then a call to print() will be made."""
        self.total = total
        self.fillCh = fillCh[0]
        self.unfillCh = unfillCh[0]
        self.widthRatio = widthRatio
        self.newLineAfterCompletion = newLineAfterCompletion
        self.clearAfterCompletion = clearAfterCompletion
        self.timer = Timer(subsecondFormat=True)
        self.reset()

    def reset(self):
        self.counter = 0
        self.percent = ""
        self.prefix = ""
        self.suffix = ""
        self.filled = ""
        self.unfilled = ""
        self.bar = ""

    def getPercent(self) -> str:
        """Returns the percentage complete to two decimal places
        as a string without the %."""
        percent = str(round(100.0 * self.counter / self.total, 2))
        if len(percent.split(".")[1]) == 1:
            percent = percent + "0"
        if len(percent.split(".")[0]) == 1:
            percent = "0" + percent
        return percent

    def _prepareBar(self):
        self.terminalWidth = get_terminal_size().columns - 1
        barLength = int(self.terminalWidth * self.widthRatio)
        progress = int(barLength * self.counter / self.total)
        self.filled = self.fillCh * progress
        self.unfilled = self.unfillCh * (barLength - progress)
        self.percent = self.getPercent()
        self.bar = self._getBar()

    def _trimBar(self):
        originalRatio = self.widthRatio
        while len(self.bar) > self.terminalWidth and self.widthRatio > 0:
            self.widthRatio -= 0.01
            self._prepareBar()
        self.widthRatio = originalRatio

    def _getBar(self):
        return f"{self.prefix} [{self.filled}{self.unfilled}]-{self.percent}% {self.suffix}"

    def display(
        self,
        prefix: str = "",
        suffix: str = "",
        counterOverride: float = None,
        totalOverride: float = None,
        returnObject: Any = None,
    ) -> Any:
        """Writes the progress bar to the terminal.

        :param prefix: String affixed to the front of the progress bar.

        :param suffix: String appended to the end of the progress bar.

        :param counterOverride: When an externally incremented completion counter is needed.

        :param totalOverride: When an externally controlled bar total is needed.

        :param returnObject: An object to be returned by display().

        Allows display() to be called within a comprehension:

        e.g.

        progBar = ProgBar(9)

        myList = [progBar.display(returnObject=i) for i in range(10)]"""
        if not self.timer.started:
            self.timer.start()
        if counterOverride:
            self.counter = counterOverride
        if totalOverride:
            self.total = totalOverride
        # Don't wanna divide by 0 there, pal
        while self.total <= 0:
            self.total += 1
        self.prefix = prefix
        self.suffix = suffix
        self._prepareBar()
        self._trimBar()
        pad = " " * (self.terminalWidth - len(self.bar))
        width = get_terminal_size().columns
        print(f"{self.bar}{pad}"[: width - 2], flush=True, end="\r")
        if self.counter >= self.total:
            self.timer.stop()
            if self.clearAfterCompletion:
                clear()
            if self.newLineAfterCompletion:
                print()
        self.counter += 1
        return returnObject
