import importlib

from . import template


class save(template.SaveTemplate):
    def __init__(self) -> None:
        super().__init__()
        self.moduleClass = None

    def getFileSystem(self):
        file = None

        while file is None:
            file = input("Please enter path to file: ")
            try:
                module = importlib.import_module(
                    file.replace("/", ".").replace("\\", ".")
                )
                self.moduleClass = module.load()
            except ModuleNotFoundError:
                file = None
                print("Not a valid file")

    def WriteData(self, data: any, path: str, Encoding: bool = False) -> bool:
        if self.moduleClass is None:
            self.getFileSystem()

        return self.moduleClass.WriteData(data, path, Encoding)

    def ReadData(self, path: str, Encoding: bool = False) -> any:
        if self.moduleClass is None:
            self.getFileSystem()

        return self.moduleClass.ReadData(path, Encoding)

    def DeleteFile(self, path: str):
        if self.moduleClass is None:
            self.getFileSystem()

        return self.moduleClass.DeleteFile(path)

    def DeleteFolder(self, path: str):
        if self.moduleClass is None:
            self.getFileSystem()

        return self.moduleClass.DeleteFolder(path)

    def MakeFolders(self, path: str):
        if self.moduleClass is None:
            self.getFileSystem()

        return self.moduleClass.MakeFolders(path)


def load():
    return save()
