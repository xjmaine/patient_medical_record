from typing import Optional, List, Dict, Any

from health_app.models.appointment import Appointment
from health_app.repositories.repository_interface import IRepository
from health_app.utils.file_manager import FileManager


class AppointmentRepository(IRepository):
    """
    Repository for handling appointment data.
    """

    def __init__(self, db_connection: FileManager):
        """
        Initialize the repository with a database connection.

        :param db_connection: The database connection.
        """
        self.__db_connection = db_connection

    def get_all(self) -> List[Appointment]:
        """
        Get all appointments.

        :return: A list of all appointments.
        """
        data = self.__db_connection.read_file()
        return [Appointment.from_dict(appointment_data) for appointment_data in data]

    def get_by_id(self, id: str) -> Optional[Appointment]:
        """
        Get an appointment by ID.

        :param id: The ID of the appointment.
        :return: The appointment with the specified ID, or None if not found.
        """
        data = self.__db_connection.read_file()
        for appointment_data in data:
            if appointment_data["id"] == id:
                return Appointment.from_dict(appointment_data)
        return None

    def create(self, data: Dict[str, Any]) -> Appointment:
        """
        Create a new appointment.

        :param data: The appointment data.
        :return: The created appointment.
        """
        appointment = Appointment.from_dict(data)
        self.__db_connection.append_to_file(appointment.to_dict())
        return appointment

    def update(self, id: str, data: Dict[str, Any]) -> Appointment:
        """
        Update an appointment.

        :param id: The ID of the appointment to update.
        :param data: The updated appointment data.
        :return: The updated appointment.
        """
        updated_appointment = Appointment.from_dict(data)
        data = self.__db_connection.read_file()

        for i, appointment_data in enumerate(data):
            if appointment_data["id"] == id:
                data[i] = updated_appointment.to_dict()
                self.__db_connection.write_file(data)
                return updated_appointment

        raise ValueError(f"Appointment with ID {id} not found.")

    def delete(self, id: str) -> bool:
        """
        Delete an appointment.

        :param id: The ID of the appointment to delete.
        :return: True if the appointment was deleted, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, appointment_data in enumerate(data):
            if appointment_data["id"] == id:
                del data[i]
                self.__db_connection.write_file(data)
                return True

        return False

    def restore(self, id: str) -> bool:
        """
        Restore a soft-deleted appointment.

        :param id: The ID of the appointment to restore.
        :return: True if the appointment was restored, False otherwise.
        """
        data = self.__db_connection.read_file()

        for i, appointment_data in enumerate(data):
            if appointment_data["id"] == id:
                appointment = Appointment.from_dict(appointment_data)
                appointment.date_deleted = None
                data[i] = appointment.to_dict()
                self.__db_connection.write_file(data)
                return True

        return False