from typing import Optional

from health_app.models.base_model import BaseModel


class Patient(BaseModel):
    """
    Patient class representing a patient in the health application.

    (BaseModel) This class inherits from the BaseModel class and adds additional
    """

    def __init__(
        self,
        *,
        first_name: str,
        last_name: str,
        other_names: Optional[str]=None,
        gender: str,
        contact: str,
        address: str,
        emergency_contact: str,
        id: Optional[str]=None,
        date_created: Optional[str]=None,
        date_updated: Optional[str]=None,
        date_deleted: Optional[str]=None,
        **kwargs
    ) -> None:
        """
        Patient constructor.
        :param first_name:
        :param last_name:
        :param other_names:
        :param gender:
        :param contact:
        :param address:
        :param emergency_contact:
        :param id:
        :param date_created:
        :param date_updated:
        :param date_deleted:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.__gender = gender
        self.__address = address
        self.__emergency_contact = emergency_contact

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def address(self) -> str:
        return self.__address

    @property
    def emergency_contact(self) -> str:
        return self.__emergency_contact

    @gender.setter
    def gender(self, value: str) -> None:
        self.__gender = value

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @emergency_contact.setter
    def emergency_contact(self, value: str) -> None:
        self.__emergency_contact = value

    def to_dict(self) -> dict:
        """
        Convert the Patient instance to a dictionary.
        """
        return {
            "id": self.id,
            "gender": self.gender,
            "address": self.address,
            "emergency_contact": self.emergency_contact,
            "date_created": self._convert_to_string(date=self.date_created),
            "date_updated": self._convert_to_string(date=self.date_updated),
            "date_deleted": self._convert_to_string(date=self.date_deleted),
            **super().to_dict()  # Include person fields from BasePersonModel
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        """
        Create a Patient instance from a dictionary.
        """
        return cls(
            id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            other_names=data.get("other_names"),
            contact=data.get("contact"),
            gender=data.get("gender"),
            address=data.get("address"),
            emergency_contact=data.get("emergency_contact"),
            date_created=data.get("date_created"),
            date_updated=data.get("date_updated"),
            date_deleted=data.get("date_deleted")
        )