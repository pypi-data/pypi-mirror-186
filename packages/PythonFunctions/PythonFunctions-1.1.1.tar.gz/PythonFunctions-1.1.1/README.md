# Functions

This is a gigantic folder, with multiple functions for multiple use cases. The only folder that you will need, is [PythonFunctions](./src/PythonFunctions/).

## Documentation

Every file has it own documentation, which can be found here: [Documentation](https://python-functions.readthedocs.io/en/latest/).
Outdated (ish) but local documents can be found here: [Local documentation](Documentation/ReadMe.md)

## Expanding

This file is still in development and more is to come! If you want to contribute, follow the same file structure and submit a pull request.
What you see now is not the final version.

## Contributing

Please read [Contributing.md](Contribution.md)

## Update Log

Please see [Updatelog.md](Updatelog.md) for updates after the latest update

For versions before `1.1.0` please see the test.pypi directory.

### 1.1.1

- Fixed issue with how i did the update check (also made a new function because of it)
- Added documentation for how to mute the update output

### 1.1.0

- Created documentation on readthedocs
- Added dependencies to pyproject.toml
- Renamed some stuff
- Improved some checks
- Fixed some bugs
- Added Version.txt to inform people of outdated versions.
- Removed loading all the modules on __init__
- Updated and fixed tests

## Credits

This project uses functions and modules from other people to run. Most of the modules have been auto imported (and kept up to date) but some require you to manually install them (check that module infomation).

### Colourama

[Github](https://github.com/tartley/colorama)
Brings colours to the terminal

### Readchar

[Github](https://github.com/magmax/python-readchar)
Taking an input straight away, instead of getting the user to press enter afterwards

### Cryptography

[Github](https://github.com/pyca/cryptography)
Encrypting and decrypting data. Quick and simple

### Requests

[Github](https://github.com/psf/requests)
Checking if you have the latest version
