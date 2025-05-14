from pathlib import Path
from typing import Any


class FileManager:
    """
    A base class for managing files
    This class provides common file operations.
    """

    def __init__(self, file_path: Path) -> None:
        """
        Initialize the FileManager class.

        :param file_path: The path to the file to be managed.
        """
        self.file_path = file_path

    def read_file(self) -> str:
        """
        Read the file and return its content as a string.

        :return: The content of the file as a string.
        """
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, *, content: Any) -> None:
        """
        Write the provided content to the file.

        :param content: The content to write to the file.
        """
        with open(self.file_path, 'w') as file:
            file.write(content)

    def append_to_file(self, *, content: Any) -> None:
        """
        Append content to the file.

        :param content: The content to append to the file.
        """
        with open(self.file_path, 'a') as file:
            file.write(content)

    # file validations
    def file_exists(self) -> bool:
        """
        Check if the file exists.

        :return: True if the file exists, False otherwise.
        """
        return self.file_path.exists()

    def create_file(self) -> None:
        """
        Create the file if it doesn't already exist
        Initialise the file with an empty string if it doesn't exist.
        """
        if not self.file_exists():
            with open(self.file_path, 'w') as file:
                file.write('')
