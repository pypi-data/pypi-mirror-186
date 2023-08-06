import io
import os
import sys

from . import template

disabled = False

try:
    from google.auth.exceptions import RefreshError
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
except ModuleNotFoundError:
    disabled = True
    # pylint:disable=C0301
    print(
        "NOTE: google drive api is NOT INSTALLED. As so, communicating with google drive api is DISABLED!!"
    )
    # pylint:enable=C0301


class save(template.SaveTemplate):
    def __init__(self) -> None:
        super().__init__()
        self.SCOPES = ["https://www.googleapis.com/auth/drive"]
        self.service = None
        self.pageSize = 0

    def credentials(self, data):
        self.pageSize = data.get("gPage")
        super().credentials(data)
        self.service = self.__LoadGoogle()

    def __LoadGoogle(self):
        if disabled:
            return False

        path = self.data.get("SettingsSave")
        path = os.path.dirname(path)
        Tpath = path + "/gToken.json"
        Cpath = path + "/gCred.json"

        if not os.path.exists(Cpath):
            sys.exit(f"Please make sure the file: {Cpath} exists!")

        try:
            creds = None
            if os.path.exists(Tpath):
                creds = Credentials.from_authorized_user_file(Tpath, self.SCOPES)

            # If there are no (valid) credentials available, let the user login
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(Cpath, self.SCOPES)
                    creds = flow.run_local_server(port=0)

                # Save the credentials for the next run
                with open(Tpath, "w", encoding="utf-8") as token:
                    token.write(creds.to_json())

            print("Drive API loaded!")
            return build("drive", "v3", credentials=creds)
        except KeyboardInterrupt:
            sys.exit("Bad drive... Please restart the program and try again.")
        except RefreshError:
            if os.path.exists(Tpath):
                os.system(f"rm {Tpath}")

                # Check if files are actually there and not missing due to folder creation.
                if not os.path.exists(Cpath):
                    sys.exit(f"{Cpath} has not been found!")
            return self.__LoadGoogle()

    def __ListDirectory(self, folder=".", name=""):
        """Loop through the path to get all the items

        Args:
            folder (string): The path to check
            name (string): name of the file to check

        Returns:
            List: List of all the items
        """
        if disabled:
            return False

        query = "trashed = false and 'me' in owners"

        if folder != "":
            query += f" and '{folder}' in parents"
        if name != "":
            query += f" and name contains '{name}'"

        try:
            files = []
            page_token = None
            while True:
                response = (
                    self.service.files()
                    .list(
                        q=query,
                        spaces="drive",
                        fields="nextPageToken, " "files(id, name)",
                        pageToken=page_token,
                    )
                    .execute()
                )
                files.extend(response.get("files", []))
                page_token = response.get("nextPageToken", None)
                if page_token is None:
                    break
        except HttpError as error:
            print(f"An error occurred: {error}")
            files = None

        return files

    def __checkIfExists(self, folder, name=""):
        """Check if an item with a certain name already exists

        Args:
            folder (string): Folder to search through
            name (string): name of the file to search for

        Returns:
            Bool: Does it exists
            item: The id of the item if it exists
        """
        if disabled:
            return False

        items = self.__ListDirectory(folder, name)
        if len(items) == 0:
            return False, None
        return True, items[0]

    def WriteData(self, data: any, path: str, Encoding: bool = False) -> bool:
        if disabled:
            return False

        pathInfo = os.path.split(path)

        if not isinstance(data, bytes):
            data = data.encode("utf-8")

        with open(self.tempFile, "wb") as f:
            f.write(data)

        exists, exId = self.__checkIfExists(pathInfo[0], pathInfo[1])
        if exists:
            deleted = self.__DeleteByID(exId.get("id"))
            print("deleted old file" if deleted else "failed to delete old file")

        metadata = {"name": pathInfo[1], "mimeType": "*/*", "parents": pathInfo[0]}

        fileId = None
        try:
            media = MediaFileUpload(self.tempFile, mimetype="*/*", resumable=True)

            fileId = (
                self.service.files()
                .create(body=metadata, media_body=media, fields="id")
                .execute()
            )
        except HttpError:
            print("Error occured trying to upload the data")

        return fileId

    def ReadData(self, path: str, Encoding: bool = False) -> any:
        if disabled:
            return False

        pathInfo = os.path.split(path)

        exists, fileID = self.__checkIfExists(pathInfo[0], pathInfo[1])
        if not exists:
            print("File not found on server!")
            return None

        try:
            request = self.service.files().get_media(fileId=fileID.get("id"))
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Downloading: {status.progress() * 100}%")

            return file.getvalue().decode("utf-8")
        except HttpError:
            print("Error occured downloading the file to be read")
            return None

    def MakeFolders(self, path: str):
        if disabled:
            return False

        fileId = None
        try:
            folders = [path]
            if path.find("/") > -1:
                folders = path.split("/")
            if path.find("\\") > -1:
                folders = path.split("\\")

            currentPath = ""
            for file in folders:

                if currentPath != "":
                    exists, fileId = self.__checkIfExists(currentPath.get("id"))
                    if exists:
                        currentPath = fileId
                        continue

                metadata = {
                    "name": file,
                    "mimeType": "application/vnd.google-apps.folder",
                }

                if currentPath != "":
                    metadata["parents"] = [currentPath.get("id")]

                fileId = (
                    self.service.files().create(body=metadata, fields="id").execute()
                )
                currentPath = fileId

            return fileId
        except HttpError:
            print("Error occured during making of folders")
            return fileId

    def DeleteFolder(self, path: str):
        if disabled:
            return False

        return self.__DeleteByPath(path)

    def DeleteFile(self, path: str):
        if disabled:
            return False

        return self.__DeleteByPath(path)

    def __DeleteByPath(self, path):
        pathInfo = os.path.split(path)
        exists, fileId = self.__checkIfExists(pathInfo[0], pathInfo[1])
        if exists:
            return self.__DeleteByID(fileId)
        return "Not found on server"

    def __DeleteByID(self, fileId):
        if disabled:
            return False

        try:
            self.service.files().delete(fileId=fileId).execute()
            return "Deleted"
        except HttpError:
            return "Not found"


def load():
    return save()
