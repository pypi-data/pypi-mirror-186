import os
import typing


class Clean:
    """Cleans up the path and removes unnessecary files"""

    def GetData(self, path: str) -> typing.List:
        """Returns the files stored in a given path

        Args:
            path (str): The path of files

        Returns:
            typing.List: The list found for that path
        """
        # If list, just use that instead
        if isinstance(path, typing.List):
            return path

        if path is None:
            return []

        try:
            return os.listdir(path)
        except FileNotFoundError:
            return []

    def RemoveHidden(self, data: typing.List[str]) -> typing.List[str]:
        """Removes files and folders that start with `.` or `__`

        Args:
            data (typing.List[str]): The original file list

        Returns:
            typing.List[str]: The new list without hidden files
        """

        newData = []
        for folder in data:
            if not folder.startswith(".") and not folder.startswith("__"):
                newData.append(folder)

        return newData

    def RemoveReserved(
        self, data: typing.List[str], reserved: typing.List[str]
    ) -> typing.List[str]:
        """Remove any files that are resereved for other purposes
        Which the user didn't include, or are just generic system files.

        Args:
            data (typing.List[str]): The data for that path
            reserved (typing.List[str]): The resereved file list

        Returns:
            typing.List[str]: The new list with the removed files
        """

        # Convert to array if string
        if isinstance(reserved, str):
            reserved = [reserved]

        # Checks if there are actually stuff to remove
        if len(reserved) == 0:
            return data

        newData = []
        for file in data:
            # Reserved check
            if file in reserved:
                continue

            # ends with reserved *
            endswithForbidden = False
            for item in reserved:
                if item.startswith("*"):
                    if file.endswith(item[1:]):
                        endswithForbidden = True

            if endswithForbidden:
                continue

            newData.append(file)
        return newData

    def clean(self, path: str, reserved: typing.List[str] = None) -> typing.List[str]:
        """Returns the finished product of cleaning up the path

        Args:
            path (str): The path to get the files from
            reserved (typing.List[str], optional): The list of data to not include in the final list

        Returns:
            typing.List[str]: The final data list
        """
        if reserved is None:
            reserved = []

        if isinstance(reserved, str):
            reserved = [reserved]

        # Get data
        data = self.GetData(path)
        # Earily return
        if len(data) == 0:
            return data

        # Remove hidden
        data = self.RemoveHidden(data)

        if len(data) == 0:
            return data

        # Remove reserved files
        reserved.append("Desktop.ini")  # windows non hidden
        reserved.append("$RECYCLE.BIN")  # windows non hidden

        data = self.RemoveReserved(data, reserved)
        return data
