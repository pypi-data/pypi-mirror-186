"""
Custom exceptions for easier error handling

General exceptions can be used for convenient error catching
example:

class GeneralException(Exception):
    ...

class SpecificException(GeneralException):
    ...

try:
    raise SpecificException
except GeneralException:
    ...
"""


class CustomException(Exception):
    """ User defined exception"""

    def __init__(self, *args):
        self.text = "An undefined custom exception has been raised"

    def __str__(self):
        """ raising an exception invokes the __str__ override """
        return self.text


class FileHandlerException(CustomException):
    """ Exceptions for reading files """

    def __init__(self, *args):
        self.text = "Exception occurred during file read"


# ----------------- File Handling ----------------
class UnsupportedFileExtension(FileHandlerException):
    """ File extension handler doesn't exist """

    def __init__(self, bad_file: str):
        self.text = f"Unable to load file: \"{bad_file}\", unsupported extension"


class FileNotFoundError(FileHandlerException, FileNotFoundError):
    """ Override FileNotFound as a custom exception """
    def __init__(self, bad_file: str):
        self.text = f"Unable to load file: \"{bad_file}\", file does not exist"
