from builtins import Exception


class InvalidDateFormatException(Exception):
    """Exception raised for invalid date format."""
    def __init__(self, date_format)->None:
        self.date_format = date_format
        err_msg = f"Invalid date format: {self.date_format}"
        super().__init__(err_msg)


class FileWriteError(Exception):
    """Exception raised for file write error."""
    def __init__(self, file_path)->None:
        self.file_path = file_path
        err_msg = f"File write error: {self.file_path}"


# file readinr error


# file not found

#saved object not found on fetch
class EntityDoesNotExistException(Exception):
    """Exception raised when an entity does not exist."""
    pass


class FailedToSaveObjectException(Exception):
    """Exception raised when an object fails to save."""
    pass