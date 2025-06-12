from typing import Optional, List, Dict, Any

from health_app.models.doctor import Doctor
from health_app.repositories.repository_interface import IRepository
from health_app.utils.file_manager import FileManager


class DoctorRepository(IRepository):
    """
    Repository for handling doctor data.
    """

    def __init__(self, db_connection: FileManager):
        """
        Initialize the repository with a database connection.

        :param db_connection: The database connection.
        """
        self.__db_connection = db_connection

    def get_all(self) -> List[Doctor]:
        """
        Get all doctors.

        :return: A list of all doctors.
        """
        data = self.__db_connection.read_file()
        return [Doctor.from_dict(doctor_data) for doctor_data in data]

    def get_by_id(self, id: str) -> Optional[Doctor]:
        """
        Get a doctor by ID.

        :param id: The ID of the doctor.
        :return: The doctor with the specified ID, or None if not found.
        """
        data = self.__db_connection.read_file()
        for doctor_data in data:
            if doctor_data["id"] == id:
                return Doctor.from_dict(doctor_data)
        return None

    def create(self, data: Dict[str, Any]) -> Doctor:
        """
        Create a new doctor.

        :param data: The doctor data.
        :return: The created doctor.
        """
        doctor = Doctor.from_dict(data)
        self.__db_connection.append_to_file(doctor.to_dict())
        return doctor

    def update(self, id: str, data: Dict[str, Any]) -> Doctor:
        """
        Update a doctor.

        :param id: The ID of the doctor to update.
        :param data: The updated doctor data.
        :return: The updated doctor.
        """
        updated_doctor = Doctor.from_dict(data)
        data = self.__db_connection.read_file()

        for i, doctor_data in enumerate(data):
            if doctor_data["id"] == id:
                data[i] = updated_doctor.to_dict()
                self.__db_connection.write_file(data)
                return updated_doctor

        raise ValueError(f"Doctor with ID {id} not found.")

    def delete(self, id: str) -> bool:
        """
        Delete a doctor.

        :param id: The ID of the doctor to delete.
        :return: True if the doctor was deleted, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, doctor_data in enumerate(data):
            if doctor_data["id"] == id:
                del data[i]
                self.__db_connection.write_file(data)
                return True

        return False

    def restore(self, id: str) -> bool:
        """
        Restore a soft-deleted doctor.

        :param id: The ID of the doctor to restore.
        :return: True if the doctor was restored, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, doctor_data in enumerate(data):
            if doctor_data["id"] == id:
                doctor = Doctor.from_dict(doctor_data)
                doctor.date_deleted = None
                data[i] = doctor.to_dict()
                self.__db_connection.write_file(data)
                return True

        return False