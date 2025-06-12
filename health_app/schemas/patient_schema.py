from pydantic import field_validator, Field

from health_app.models.base_model import BaseModel
from health_app.schemas.base_schemas import BasePersonSchema, BaseReadSchema


class BasepatientSchema(BaseModel):
    """Base schema for patient models"""
    first_name: str
    last_name: str
    other_names: str | None = None
    gender: str
    contact: str
    address: str
    emergency_contact: str

class CreatePatientSchema(BasePersonSchema):
    """
    Schema for creating a new patient.
    """
    emergency_contact_name: str = Field(..., min_length=7)
    address: str = Field(..., min_length=2)
    gender: str = Field(..., min_length=1)
    date_of_birth: str = Field(..., min_length=10)

    @field_validator("gender")
    @classmethod
    def gender_id_valid(cls, value: str) -> str:
        """
        Validate that the given gender is valid.
        :param value: The gender to validate
        :param:
        """
        if not (value.lower().strip() in ["male", "female"]):
            raise ValueError("Invalid gender. Expected one of: male, female")
        return value.lower().strip()


class UpdatePatientSchema(BasePersonSchema):
    """
    Schema for updating a patient.
    """
    emergency_contact_name: str = Field(..., min_length=7)
    address: str = Field(..., min_length=2)
    gender: str = Field(..., min_length=1)
    date_of_birth: str = Field(..., min_length=10)

    @field_validator("gender")
    @classmethod
    def gender_id_valid(cls, value: str) -> str:
        """
        Validate that the given gender is valid.
        :param value: The gender to validate
        :param:
        """
        if not (value.lower().strip() in ["male", "female"]):
            raise ValueError("Invalid gender. Expected one of: male, female")
        return value.lower().strip()

class ReadPatientSchema(BaseReadSchema):
    """
    Schema for patient read operations
    """
    # Add any additional fields needed for the read model
    # These should match the Patient model's to_dict() output
    id: str
    first_name: str
    last_name: str
    other_names: str | None = None
    gender: str
    contact: str
    address: str
    emergency_contact: str
    date_created: str | None = None
    date_updated: str | None = None
    date_deleted: str | None = None