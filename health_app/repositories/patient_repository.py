from health_app.repositories.repository_interface import IRepository

class PatientRepository(IRepository):
    """
    Class responsible for Patient data
    Inherits from IRepository and implements abstract mthods
    """

    def get_all(self) -> list[dict]:
        pass

    def get_by_id(self, id: int) -> dict:
        pass