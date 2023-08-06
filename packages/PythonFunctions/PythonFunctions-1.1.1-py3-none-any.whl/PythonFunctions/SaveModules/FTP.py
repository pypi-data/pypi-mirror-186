import ftplib
import os

from . import template


class save(template.SaveTemplate):
    def __init__(self) -> None:
        self.ftp: ftplib.FTP = ftplib.FTP()

        super().__init__()

    def __Login(self, path):
        """Log in to the FTP server using the provided information

        Args:
            path (string): The path to connect to + the folder to go to.
        """
        info = path.split("/")
        path = ""

        for item in info[1:]:
            path += item + "/"

        server = info[0].split(":")
        port = 21

        if info[0].find(":") > -1:
            if server[1].isdigit():
                port = int(server[1])

        try:
            print(f"Attempting to connect to ftp://{server[0]}:{port}")
            self.ftp.connect(server[0], port)
            credentials = self.data.get("FTP")

            self.ftp.login(credentials.get("Name"), credentials.get("Password"))

            if len(info) > 1:
                try:
                    self.ftp.cwd(path)
                except ftplib.error_perm:
                    pass

        except ConnectionRefusedError:
            print(f"Server: {server[0]}, Port: {port}")
            print("Connection refused by target machine!")

        return path

    def WriteData(self, data: any, path: str, Encoding: bool = False) -> bool:
        print("Writing data...")
        path = self.__Login(path)
        print(f"Attempting to writing data to {path}")

        # Translate to binary for easier storage
        code = None
        if not isinstance(data, bytes):
            data = data.encode("utf-8")

        # write temp file
        with open(self.tempFile, "wb") as f:
            f.write(data)

        # store file on server
        with open(self.tempFile, "rb") as f:
            code = self.ftp.storbinary(f"STOR {path}", f)

        # remove data from local client
        if os.path.exists(self.tempFile):
            os.remove(self.tempFile)

        return code

    def ReadData(self, path: str, Encoding: bool = False) -> any:
        print("Reading data...")
        path = self.__Login(path)

        # get data from server
        with open(self.tempFile, "wb") as f:
            self.ftp.retrbinary(f"RETR {path}", f.write)

        with open(self.tempFile, "rb") as f:
            d = f.read()
            try:
                return d.decode("utf-8")
            except UnicodeDecodeError:
                return d

    def MakeFolders(self, path: str):
        print("Making folders...")
        path = self.__Login(path)
        print(f"Attempting to make: {path}")

        if len(path) > 0:
            directories = path.split("/")
            cPath = self.ftp.pwd()

            for item in directories:
                if item not in self.ftp.nlst() and item != "":
                    self.ftp.mkd(item)
                self.ftp.cwd(item)
            self.ftp.cwd(cPath)

        return path

    def DeleteFile(self, path: str):
        print("Deleting files...")
        path = self.__Login(path)

        return self.ftp.delete(f"{path}")

    def DeleteFolder(self, path: str):
        print("Deleting folders...")
        path = self.__Login(path)

        return self.ftp.rmd(path)


def load():
    return save()
