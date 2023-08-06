import datetime
import inspect
import os

from .Colours import c


def main(
    name: str,
    twitter: str = None,
    youtube: str = None,
    github: str = None,
    *,
    colour: str = "",
):
    """
    Prints off a watermark / header style thing on call.

    Args:
        name (str): The username
        twitter (str, optional): Twitter link
        youtube (str, optional): Youtube link
        github (str, optional); Github link
    """
    fileName: str = ""

    for frame in inspect.stack()[1:]:
        if frame.filename[0] != "<":
            fileName = os.path.basename(frame.filename)[:-3]
            break

    twitURL = "https://twitter.com/DragMine149"
    youURL = "https://youtube.com/channel/UCOnORrEI4GhYtivLQJpOoJQ"
    gitURL = "https://github.com/dragmine149"

    # Prints off my watermark
    line = "-" * os.get_terminal_size().columns

    # Gets data
    data = ""
    if twitter is not None:
        data += f"\u001b]8;;{twitter}\u001b\\Twitter\u001b]8;;\u001b\\, "
    if youtube is not None:
        data += f"\u001b]8;;{youtube}\u001b\\Youtube\u001b]8;;\u001b\\, "
    if github is not None:
        data += f"\u001b]8;;{github}\u001b\\Github\u001b]8;;\u001b\\"

    # If data is null
    if data == "":
        data = "Nothing linked"

    mydata = ""
    mydata += f"\u001b]8;;{twitURL}\u001b\\Twitter\u001b]8;;\u001b\\, "
    mydata += f"\u001b]8;;{youURL}\u001b\\Youtube\u001b]8;;\u001b\\, "
    mydata += f"\u001b]8;;{gitURL}\u001b\\Github\u001b]8;;\u001b\\"

    # Gets time
    ctime = datetime.datetime.now()

    print("\x1b[2J\x1b[H", end="")
    print(
        f"""{c(colour)}{line}{c()}
{fileName} made by {name} ({data}).
Contains Functions.py made by dragmine149 ({mydata}).
Activation Time: {ctime.hour}:{ctime.minute}:{ctime.second}
{c(colour)}{line}{c()}"""
    )


if __name__ == "__main__":
    main("drag")
