import os
import shutil

from . import template


class Save(template.SaveTemplate):
    def WriteData(self, data: any, path: str, Encoding: bool = False) -> bool:
        if Encoding:
            with open(path, "wb") as f:
                return f.write(data) == len(data)

        with open(path, "w", encoding="utf-8") as f:
            return f.write(data) == len(data)

    def ReadData(self, path: str, Encoding: bool = False) -> any:
        if Encoding:
            with open(path, "rb") as f:
                return f.read()

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def MakeFolders(self, path: str):
        if not os.path.exists(path):
            os.makedirs(path)

    def DeleteFile(self, path: str):
        if os.path.exists(path):
            os.remove(path)

    def DeleteFolder(self, path: str):
        if os.path.exists(path):
            shutil.rmtree(path)


def load():
    return Save()
