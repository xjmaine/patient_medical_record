from typing import Optional

from health_app.models.base_model import BaseModel


class BasePersonModel(BaseModel):
    """
    Basemodel for common person attributes
    """

    def __init__(
            self,
            *,
            first_name: str,
            last_name: str,
            other_names: Optional[str] = None,
            contact: str,
            **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__other_names = other_names
        self.__contact = contact

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def other_names(self) -> Optional[str]:
        return self.__other_names

    @property
    def contact(self) -> str:
        return self.__contact

    @first_name.setter
    def first_name(self, value: str) -> None:
        self.__first_name = value

    @last_name.setter
    def last_name(self, value: str) -> None:
        self.__last_name = value

    @other_names.setter
    def other_names(self, value: Optional[str]) -> None:
        self.__other_names = value

    @contact.setter
    def contact(self, value: str) -> None:
        self.__contact = value

    def to_dict(self) -> dict:
        """
        converts the person model to dict
        :return:
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "other_names": self.other_names,
            "contact": self.contact,
            **super().to_dict()
        }