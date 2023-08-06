from .Message import Message
from .PrintTraceback import PrintTraceback

disabled = False

try:
    from cryptography import fernet
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    Message.warn(
        "Failed to load encrypting class (Missing imports!)", timeS=2, colour="red"
    )
    PrintTraceback()
    disabled = True


class Encryption:
    """The major class to encrypt and decrypt data securly"""

    def __init__(self) -> None:
        self.fernet = fernet
        self.check: bool = not disabled
        self.key = None

    def GetKey(self) -> bytes:
        """Translates your encrypted (using utf-8) passcode into something more secure

        Returns:
            bytes: The result
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"

        Message().warn(
            "Please make sure you keep the key safe!",
            timeS=4,
            colour="RED",
        )
        if self.key is not None:
            return self.key

        key = Fernet.generate_key()
        self.key = key
        return self.key

    def EncryptData(self, data, passcode):
        if not isinstance(data, bytes):
            data = data.encode("utf-8")

        return Fernet(passcode).encrypt(data)

    def DecryptData(self, data, passcode):
        dta = Fernet(passcode).decrypt(data)
        if isinstance(dta, bytes):
            return dta.decode("utf-8")
        return dta

    def encrypt(self, data, passcode: bytes, *, fileName="encrypted"):
        """Encrypts the data that you want to in a safe file

        Args:
            data (_type_): The data to save
            passcode (bytes): The passcode to encrypt with
            fileName (str, optional): The name of the file. Defaults to "encrypted".
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"

        if not isinstance(data, bytes):
            data = data.encode("utf-8")

        with open(fileName, "wb") as f:
            f.write(self.EncryptData(data, passcode))
            return "Saved data"

    def decrypt(self, passcode: bytes, *, fileName="encrypted"):
        """Decrypt the data stored in the file

        Args:
            passcode (bytes): Your passcode to decypt with
            fileName (str, optional): The name of the file. Defaults to "encrypted".
            data (any, optional): ONLY REQUIRED IF YOU ALREADY HAVE ENCRYPTED DATA

        Returns:
            _type_: The decrypted data
        """
        if disabled:
            return "Missing Modules! Classs Disabled!!"

        with open(fileName, "rb") as f:
            data = self.DecryptData(f.read(), passcode)
            return data
