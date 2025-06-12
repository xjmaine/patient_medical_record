from abc import ABC, abstractmethod
from typing import Type, Optional, List, Dict, Any

from health_app.models.base_model import BaseModel
from health_app.schemas.base_schemas import BaseReadSchema


class IRepository(ABC):
    """
    Interface for repository classes.
    """

    @abstractmethod
    def get_all(self) -> List[BaseModel]:
        """
        Get all records.
        """
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[BaseModel]:
        """
        Get a record by ID.
        """
        pass

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> BaseModel:
        """
        Create a new record.
        """
        pass

    @abstractmethod
    def update(self, id: str, data: Dict[str, Any]) -> BaseModel:
        """
        Update a record.
        """
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        """
        Delete a record.
        """
        pass

    @abstractmethod
    def restore(self, id: str) -> bool:
        """
        Restore a soft-deleted record.
        """
        pass