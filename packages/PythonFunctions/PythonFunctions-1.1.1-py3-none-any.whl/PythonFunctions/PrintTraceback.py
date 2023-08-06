import os
import traceback


def PrintTraceback():
    # Mainly for pytest, but skip over the '-' if failed
    try:
        dash = "-" * os.get_terminal_size().columns
    except OSError:
        dash = ""

    print(f"\033[41m{dash}")
    traceback.print_exc()
    print(f"{dash}\033[0m")


if __name__ == "__main__":
    PrintTraceback()
