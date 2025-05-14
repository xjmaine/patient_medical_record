from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PatientCreate(BaseModel):
    """
    schema for creating patient data
    """
    first_name: str
    last_name: str
    other_names: Optional[str] = None
    gender: str
    contact: str
    address: str
    emergency_contact: str


class PatientResponse(PatientCreate):
    """
    Schema for returning patient data in responses.
    """
    id: str
    date_created: datetime
    date_updated: datetime
    date_deleted: Optional[datetime]
