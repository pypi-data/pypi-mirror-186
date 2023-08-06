# Module update checker, based off the github file
import json
import os

canReadGlobal = True
try:
    import requests
except ModuleNotFoundError:
    print("Requests is not installed. Can not check for a new PythonFunction update!")
    canReadGlobal = False


def LocalSettings():
    """Check if muted

    Returns:
        bool: Muted or not
    """
    path = os.getcwd() + "/PyFuncSet.json"
    if os.path.exists(path):
        data = {}
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return not data.get("Mute")

    return True


def ReadLocal():
    """Get the module version

    Returns:
        str: Module version
    """
    return "1.1.5"


def ReadGlobal():
    """Get the version on the server"""
    url = "https://raw.githubusercontent.com/FunAndHelpfulDragon/python-Functions/main/Version.txt"
    r = requests.get(url, timeout=60)
    if r.text != ReadLocal():
        print("Notice: A newer version of PythonFunctions is alvalible.")


if canReadGlobal and LocalSettings():
    ReadGlobal()
