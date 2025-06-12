from typing import Optional, List, Dict, Any

from health_app.models.patient import Patient
from health_app.repositories.repository_interface import IRepository
from health_app.utils.file_manager import FileManager


class PatientRepository(IRepository):
    """
    Class responsible for Patient data
    Inherits from IRepository and implements abstract methods
    """

    def __init__(self, db_connection: FileManager):
        """
        Initialize the repository with a database connection.

        :param db_connection: The database connection.
        """
        self.__db_connection = db_connection

    def get_all(self) -> List[Patient]:
        """
        Get all patients.

        :return: A list of all patients.
        """
        data = self.__db_connection.read_file()
        return [Patient.from_dict(patient_data) for patient_data in data]

    def get_by_id(self, id: str) -> Optional[Patient]:
        """
        Get a patient by ID.

        :param id: The ID of the patient.
        :return: The patient with the specified ID, or None if not found.
        """
        data = self.__db_connection.read_file()
        for patient_data in data:
            if patient_data["id"] == id:
                return Patient.from_dict(patient_data)
        return None

    def create(self, data: Dict[str, Any]) -> Patient:
        """
        Create a new patient.

        :param data: The patient data.
        :return: The created patient.
        """
        patient = Patient.from_dict(data)
        self.__db_connection.append_to_file(patient.to_dict())
        return patient

    def update(self, id: str, data: Dict[str, Any]) -> Patient:
        """
        Update a patient.

        :param id: The ID of the patient to update.
        :param data: The updated patient data.
        :return: The updated patient.
        """
        updated_patient = Patient.from_dict(data)
        data = self.__db_connection.read_file()

        for i, patient_data in enumerate(data):
            if patient_data["id"] == id:
                data[i] = updated_patient.to_dict()
                self.__db_connection.write_file(data)
                return updated_patient

        raise ValueError(f"Patient with ID {id} not found.")

    def delete(self, id: str) -> bool:
        """
        Delete a patient.

        :param id: The ID of the patient to delete.
        :return: True if the patient was deleted, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, patient_data in enumerate(data):
            if patient_data["id"] == id:
                del data[i]
                self.__db_connection.write_file(data)
                return True

        return False

    def restore(self, id: str) -> bool:
        """
        Restore a soft-deleted patient.

        :param id: The ID of the patient to restore.
        :return: True if the patient was restored, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, patient_data in enumerate(data):
            if patient_data["id"] == id:
                patient = Patient.from_dict(patient_data)
                patient.date_deleted = None
                data[i] = patient.to_dict()
                self.__db_connection.write_file(data)
                return True

        return False