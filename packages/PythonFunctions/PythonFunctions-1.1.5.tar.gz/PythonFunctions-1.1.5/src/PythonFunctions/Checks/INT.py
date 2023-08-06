"""Checks if a value is within a certain range
"""


def check(value, Message, ID, **info) -> int:
    """Checks if a value is within a certain range

    Args:
        value (_type_): The value to check
        Message (_type_): Message obj
        ID (_type_): IsDigit obj

    Returns:
        _type_: Either the value, or nothing
    """
    higherRange = info.get("higher")
    lowerRange = info.get("lower")

    # is digit check
    if ID.IsDigit(value):

        value = float(value)
        if lowerRange is not None:
            if value < lowerRange:
                Message.clear(
                    f"Out of range. Too low! (Lowest Value: {lowerRange})",
                    timeS=1,
                    colour=["red"],
                )
                return None

        if higherRange is not None:
            if value > higherRange:
                Message.clear(
                    f"Out of range. Too high! (Highest Value: {higherRange})",
                    timeS=1,
                    colour=["red"],
                )
                return None
        return int(value)

    Message.clear("Invalid input! Not a `real` number", timeS=1, colour="light red")
    return None
