"""
Returns True ("y") or False ("n")

Arguments:
----------
None
"""


def check(value, Message, _, **__):
    """
    If value == `y` then return True
    if value == `n` then return False
    else return None
    """
    value = value.strip()

    if len(value) == 0:
        return Message.clear("Invalid input! Nothing there")

    return True if value[0] == "y" else False if value[0] == "n" else None
