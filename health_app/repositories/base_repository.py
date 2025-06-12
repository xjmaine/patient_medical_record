from typing import Type

from pydantic import BaseModel

from health_app.exceptions.custom_exceptions import FileWriteError
from health_app.utils.file_manager import FileManager

class BaseRepository:
    """
    Base repository to provide common methods via interfacing
    """

    def __init__(self, db_connection: FileManager)->None:
        """
        Initialise the Base Repo with a db conn
        :param db_connection:
        """
        self.__db_connection = db_connection

    # create new db record
    def create(self, data: BaseModel, model: Type[BaseModel])->None:
        """
        Abstract method to create a new db record
        :param model:
        :param data: data to create
        :return: created object
        """
        data_dict = data.model_dump()
        model_instance = model(**data_dict)
        self.__save(object_to_save=model_instance.model_dump())

    def __save(self, object_to_save: dict)->None:
        """
        save object to db
        """
        if not isinstance(object_to_save, dict):
            raise TypeError("object_to_save must be a dict")

        #try catch connection
        try:
            if self.__db_connection.file_exists():
                existing_data = self.__db_connection.read_file()
            if not isinstance(object_to_save, dict):
                existing_data = [existing_data, object_to_save]
            else:
                existing_data=[]
                # raise TypeError("object_to_save must be a dict")
            
            existing_data.append(object_to_save)
            self.__db_connection.write_file(content=existing_data)
        except Exception as e:
            raise FileWriteError(str(self.__db_connection.file_path)) from e

    #update


    # delete


    # restore fro soft delete

    # patch