"""Board generation and display

Functions:
- CreateBoard
- DisplayBoard
"""

import typing

from .Colours import c


def CreateBoard(
    x_len: int, y_len: int, *, value: str = "-"
) -> typing.List[typing.List]:
    """Create a 2D array that is like a board

    Args:
        x (int): The width
        y (int): the height
        value (str, optional): What to fill in the board with. Defaults to '-'.

    Returns:
        typing.List[typing.List]: The array result
    """
    board = []
    for _ in range(y_len):  # Y size (height)
        x_Grid = []
        for _ in range(x_len):  # X size (width)
            x_Grid.append(value)
        board.append(x_Grid)
    return board


def DisplayBoard(
    board: typing.List[typing.List], *, colourInfo: typing.DefaultDict = None
):
    """Displays the inputted board

    Args:
        board (typing.List[typing.List]): The board (2D array) to show
        colourInfo (dict, optional): The colour info of the grid. Defaults to {}.
    """
    for y_Index in board:
        for x_Index in y_Index:
            if colourInfo is not None:
                print(f"{c(colourInfo.get(x_Index))}{x_Index}{c()}", end="")
            else:
                print(x_Index, end="")
        print()


if __name__ == "__main__":
    brd = CreateBoard(3, 3, value="+")
    DisplayBoard(brd, colourInfo={"+": "y"})
