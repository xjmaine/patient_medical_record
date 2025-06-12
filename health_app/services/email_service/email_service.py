from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr
from typing import List, Dict, Any
from health_app.services.email_service.email_config import email_config


class EmailService:
    """
    Modular email service with multiple sending capabilities
    """

    def __init__(self):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=email_config.MAIL_USERNAME,
            MAIL_PASSWORD=email_config.MAIL_PASSWORD,
            MAIL_FROM=email_config.MAIL_FROM,
            MAIL_PORT=email_config.MAIL_PORT,
            MAIL_SERVER=email_config.MAIL_SERVER,
            MAIL_STARTTLS=email_config.MAIL_STARTTLS,
            MAIL_SSL_TLS=email_config.MAIL_SSL_TLS,
            TEMPLATE_FOLDER=email_config.TEMPLATE_FOLDER,
            USE_CREDENTIALS=email_config.USE_CREDENTIALS,
            VALIDATE_CERTS=email_config.VALIDATE_CERTS
        )
        self.fm = FastMail(self.conf)

    async def send_email(
            self,
            subject: str,
            recipients: List[EmailStr],
            body: str = None,
            template_name: str = None,
            template_data: Dict[str, Any] = None,
            subtype: MessageType = MessageType.plain
    ) -> None:
        """
        Email with optional template support
        """
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            template_body=template_data,
            subtype=subtype
        )

        if template_name:
            await self.fm.send_message(message, template_name=template_name)
        else:
            await self.fm.send_message(message)

    async def send_patient_registration(
            self,
            background_tasks: BackgroundTasks,
            patient_email: EmailStr,
            patient_name: str
    ) -> None:
        """Send registration confirmation email"""
        await self._send_background_email(
            background_tasks,
            subject="Welcome to The PMRMS Healthcare System",
            recipients=[patient_email],
            template_name="patient_registration.html",
            template_data={"name": patient_name}
        )

    async def send_appointment_notification(
            self,
            background_tasks: BackgroundTasks,
            patient_email: EmailStr,
            doctor_email: EmailStr,
            patient_name: str,
            doctor_name: str,
            appointment_details: Dict[str, Any]
    ) -> None:
        """Send appointment confirmation to both parties"""
        # Send to patient
        await self._send_background_email(
            background_tasks,
            subject="Appointment Confirmation",
            recipients=[patient_email],
            template_name="appointment_patient.html",
            template_data={
                "name": patient_name,
                "doctor": doctor_name,
                **appointment_details
            }
        )

        # Send to doctor
        await self._send_background_email(
            background_tasks,
            subject="New Appointment Scheduled",
            recipients=[doctor_email],
            template_name="appointment_doctor.html",
            template_data={
                "name": doctor_name,
                "patient": patient_name,
                **appointment_details
            }
        )

    async def _send_background_email(
            self,
            background_tasks: BackgroundTasks,
            subject: str,
            recipients: List[EmailStr],
            template_name: str = None,
            template_data: Dict[str, Any] = None
    ) -> None:
        """Helper method for background email sending"""
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            template_body=template_data,
            subtype=MessageType.html
        )
        background_tasks.add_task(
            self.fm.send_message, message, template_name=template_name
        )