from fastapi import BackgroundTasks

from health_app.dependencies.email_dependencies import get_email_service
from health_app.models.appointment import Appointment
from health_app.repositories.appointment_repository import AppointmentRepository
from health_app.schemas.appointment_schema import CreateAppointmentSchema
from health_app.services.patient_service import PatientService


class DoctorService:
    pass


class AppointmentService:
    def __init__(self, repository: AppointmentRepository):
        self.__repository = repository
        self.__email_service = get_email_service()
        self.__patient_service = PatientService()
        self.__doctor_service = DoctorService()

    async def create(self, appointment: CreateAppointmentSchema) -> Appointment:
        created_appointment = self.__repository.create(data=appointment, model=Appointment)

        """
        patient and doctor details
        """
        patient = await self.__patient_service.get_by_id(appointment.patient_id)
        doctor = await self.__doctor_service.get_by_id(appointment.doctor_id)

        """
            appointment notification
        """
        background_tasks = BackgroundTasks()
        await self.__email_service.send_appointment_notification(
            background_tasks,
            patient_email=patient.contact,
            doctor_email=doctor.contact,
            patient_name=f"{patient.first_name} {patient.last_name}",
            doctor_name=f"{doctor.first_name} {doctor.last_name}",
            appointment_details={
                "date": created_appointment.appointment_date.strftime("%Y-%m-%d"),
                "time": created_appointment.appointment_date.strftime("%H:%M"),
                "status": created_appointment.status
            }
        )

        return created_appointment