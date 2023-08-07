import os


class SaveTemplate:
    def __init__(self) -> None:
        self.parent = os.path.dirname(os.path.dirname(__file__))
        self.tempFile = f"{self.parent}/PyFuncSave/temp.temp"
        self.data = {}

    def credentials(self, data):
        self.data = data

    def WriteData(self, data: any, path: str, Encoding: bool = False) -> bool:
        """Save data to a file by writing it

        Args:
            data (any): The data to save
            path (str): The path to save to
            Encoding (bool, optional): To save in binary. Defaults to False.

        Raises:
            NotImplementedError: This hasn't been made for this file system yet

        Returns:
            bool: Did the save succseed?
        """
        raise NotImplementedError(
            "The file system you are trying to use does not have support for `WriteData`"
        )

    def ReadData(self, path: str, Encoding: bool = False) -> any:
        """Read data from a file and returns it

        Args:
            path (str): The path to read from
            Encoding (bool, optional): To load in binary. Defaults to False.

        Raises:
            NotImplementedError: This hasn't been made for this file system yet

        Returns:
            any: The data to return
        """
        raise NotImplementedError(
            "The file system you are trying to use does not have support for `ReadData`"
        )

    def MakeFolders(self, path: str):
        """Make folders to save a file in.
        Automatically happens if folders do not exists already

        Args:
            path (str): The path of folders

        Raises:
            NotImplementedError: This hasn't been made for this file system yet
        """
        raise NotImplementedError(
            "The file system you are trying to use does not have support for `MakeFolders`"
        )

    def DeleteFile(self, path: str):
        """Delete a file.

        Args:
            path (str): The file to delete

        Raises:
            NotImplementedError: This hasn't been made for this file system yet
        """
        raise NotImplementedError(
            "The file system you are trying to use does not have support for `DeleteFile`"
        )

    def DeleteFolder(self, path: str):
        """Delete a folder (or multiple if it's a sub folder)

        Args:
            path (str): The folder to delete

        Raises:
            NotImplementedError: This hasn't been made for this file system yet
        """
        raise NotImplementedError(
            "The file system you are trying to use does not have support for `DeleteFolder`"
        )


def load():
    return SaveTemplate()
