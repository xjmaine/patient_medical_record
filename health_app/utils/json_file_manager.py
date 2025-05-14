import json
from pathlib import Path
from typing import Any

from health_app.utils.file_manager import FileManager

class JSONFileManager(FileManager):
    """
    A class to manage JSON files.
    """
    def __init__(self, *, file_path: Path) -> None:
        """
        Initialize the JSONFileManager class.
        :param file_path: The path to the JSON file.
        """
        super().__init__(file_path)

    def read_file(self)->str:
        """
        Reads the Json file
        :return:
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write_file(self, *, content: Any) -> None:
        """
        Abstract methog to write the file
        :param content:
        :return:
        """
        with open(self.file_path, 'w') as file:
            json.dump(content, file, indent=4)

    # append to file


    #static methods here

