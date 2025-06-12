from typing import Optional, List, Dict, Any

from health_app.models.medical_record import MedicalRecord
from health_app.repositories.repository_interface import IRepository
from health_app.utils.file_manager import FileManager


class MedicalRecordRepository(IRepository):
    """
    Repository for handling medical record data.
    """

    def __init__(self, db_connection: FileManager):
        """
        Initialize the repository with a database connection.

        :param db_connection: The database connection.
        """
        self.__db_connection = db_connection

    def get_all(self) -> List[MedicalRecord]:
        """
        Get all medical records.

        :return: A list of all medical records.
        """
        data = self.__db_connection.read_file()
        return [MedicalRecord.from_dict(record_data) for record_data in data]

    def get_by_id(self, id: str) -> Optional[MedicalRecord]:
        """
        Get a medical record by ID.

        :param id: The ID of the medical record.
        :return: The medical record with the specified ID, or None if not found.
        """
        data = self.__db_connection.read_file()
        for record_data in data:
            if record_data["id"] == id:
                return MedicalRecord.from_dict(record_data)
        return None

    def create(self, data: Dict[str, Any]) -> MedicalRecord:
        """
        Create a new medical record.

        :param data: The medical record data.
        :return: The created medical record.
        """
        record = MedicalRecord.from_dict(data)
        self.__db_connection.append_to_file(record.to_dict())
        return record

    def update(self, id: str, data: Dict[str, Any]) -> MedicalRecord:
        """
        Update a medical record.

        :param id: The ID of the medical record to update.
        :param data: The updated medical record data.
        :return: The updated medical record.
        """
        updated_record = MedicalRecord.from_dict(data)
        data = self.__db_connection.read_file()

        for i, record_data in enumerate(data):
            if record_data["id"] == id:
                data[i] = updated_record.to_dict()
                self.__db_connection.write_file(data)
                return updated_record

        raise ValueError(f"Medical record with ID {id} not found.")

    def delete(self, id: str) -> bool:
        """
        Delete a medical record.

        :param id: The ID of the medical record to delete.
        :return: True if the medical record was deleted, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, record_data in enumerate(data):
            if record_data["id"] == id:
                del data[i]
                self.__db_connection.write_file(data)
                return True

        return False

    def restore(self, id: str) -> bool:
        """
        Restore a soft-deleted medical record.

        :param id: The ID of the medical record to restore.
        :return: True if the medical record was restored, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, record_data in enumerate(data):
            if record_data["id"] == id:
                record = MedicalRecord.from_dict(record_data)
                record.date_deleted = None
                data[i] = record.to_dict()
                self.__db_connection.write_file(data)
                return True

        return False