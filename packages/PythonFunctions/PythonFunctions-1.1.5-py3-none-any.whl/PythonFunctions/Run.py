"""
Run.py

Mainipulate time, in a module.
Basic functions, but just stored elsewhere
"""

import time

start = time.time()
markers = []


def Mark() -> int:
    """Add a new marker

    Returns:
        int: The marker number
    """
    markers.append(time.time())
    return len(markers)


def GetMarkTime(i: int) -> float:
    """Return the time at the mark

    Args:
        i (int): The mark index

    Returns:
        float: The time
    """
    return markers[i]


def CompareIndex(a: int, b: int) -> float:
    """Compare the time differences between 2 points in the marker index

    Args:
        a (int): The first marker index
        b (int): The second marker index

    Returns:
        float: The time difference
    """
    return markers[b] - markers[a]


def End() -> float:
    """Returns the time since the program started

    Returns:
        float: The time difference
    """
    return time.time() - start
