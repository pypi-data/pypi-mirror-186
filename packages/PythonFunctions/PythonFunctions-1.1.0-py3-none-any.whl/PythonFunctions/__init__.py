# Module update checker, based off the github file
import os


canReadGlobal = True
try:
    import requests
except ModuleNotFoundError:
    print("Requests is not installed. Can not check for a new PythonFunction update!")
    canReadGlobal = False


def ReadLocal():
    localVersion = ""
    path = os.path.abspath(os.path.dirname(__file__))
    with open(f"{path}/Version.txt", "r", encoding="utf-8") as f:
        localVersion = f.read()
    return localVersion


def ReadGlobal():
    url = "https://raw.githubusercontent.com/FunAndHelpfulDragon/python-Functions/main/Version.txt"
    r = requests.get(
        url, timeout=60)
    if r != ReadLocal():
        print("Notice: A newer version of PythonFunctions is alvalible.")


if canReadGlobal:
    ReadGlobal()
