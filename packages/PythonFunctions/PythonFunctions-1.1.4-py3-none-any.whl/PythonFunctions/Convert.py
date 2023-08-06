import dataclasses
import typing

from .Message import Message


# Converts the input to a valid location (a1 -> [0,0])
@dataclasses.dataclass
class LocationConvert:
    """Convert a letter and a number, to a position array

    Args:
        value (str): The position to translate
    """

    def __init__(self):
        self.letters: str = ""
        self.y: str = ""

    # Thanks to Guy_732
    # changes letter to number based in the alphabet
    def _decode(self, s: str) -> int:
        s = s.lower()
        ref = ord("a") - 1
        v = 0
        exp = 1
        for c in reversed(s):
            v += (ord(c) - ref) * exp
            exp *= 26

        return v

    def Convert(self, value: str) -> typing.Tuple:
        """Main convert function

        Args:
            value: (str)

        Returns:
            Tuple: The cooridnate position
        """
        if len(value) >= 2:
            # lower input
            value = value.lower().strip()

            # splits the input into numbers and letters
            for v in value:
                if v.isdigit():
                    self.y += v
                else:
                    self.letters += v

            # Checks if there is at least 1 character that is not a letter
            if self.letters == value:
                Message().clear(
                    "Must be at least two digits, a letter (x) and a number (y)",
                    timeS=1,
                    colour=["orange"],
                )  # noqa
                return None, None

            # convert letters into numbers
            return self._decode(self.letters) - 1, (int(self.y) - 1)

        # Not enough characters
        Message().clear(
            "Must be at least two digits, a letter (x) and a number (y)",
            timeS=1,
            colour=["orange"],
        )  # noqa
        return None, None
