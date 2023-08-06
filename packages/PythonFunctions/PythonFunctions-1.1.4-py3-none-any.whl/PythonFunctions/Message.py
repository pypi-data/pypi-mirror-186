import os
import time
import typing

from .Colours import Print


class Message:
    """Another way to handle console clearing"""

    @staticmethod
    def __messageSort(
        *,
        timeS: int = 0,
        message: str = None,
        clear: bool = False,
        colour: typing.List = None,
        delete: bool = False
    ):
        # checks for timeS is string instead of time
        if isinstance(timeS, str):
            Print(
                "Automatically fixed error! `timeS` was string instead of number!",
                "light red",
            )  # noqa E501
            time.sleep(2)  # force wait
            message = timeS
            timeS = 2  # default time, 2 seconds for message

        # Prints the message
        if message:
            Print(message, colour)

        # Waits X seconds
        time.sleep(timeS)

        # If clearing console data
        if clear:
            # Check if we don't care about previous data
            if delete:
                return os.system("cls" if os.name == "nt" else "clear")
            return print("\x1b[2J\x1b[H", end="")
        return None

    @staticmethod
    def clear(
        message: str = "",
        *,
        timeS: int = 0,
        colour: typing.List = [None, None],
        delete: bool = False
    ):
        """Clears the console with some options

        Args:
            message (str, optional): The message to show. Defaults to None.
            timeS (int, optional): Time to wait after showing the message. Defaults to 0.
            colour (typing.List, optional): The colour of the message. Defaults to [None, None].
            delete (bool, optional): Whever to delete the console log afterwards. Defaults to False.
        """
        Message.__messageSort(
            timeS=timeS, message=message, colour=colour, clear=True, delete=delete
        )

    @staticmethod
    def warn(
        message: str = None, *, timeS: int = 0, colour: typing.List = [None, None]
    ):
        """Not as bad as clear, but still shows as many options

        Args:
            message (str, optional): The message to show. Defaults to None.
            timeS (int, optional): The time to wait before carring on. Defaults to 0.
            colour (typing.List, optional): The colour of the message. Defaults to [None, None].
        """
        Message.__messageSort(timeS=timeS, message=message, colour=colour)
