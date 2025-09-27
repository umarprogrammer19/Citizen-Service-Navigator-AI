from pydantic import BaseModel


class Citizen(BaseModel):
    name: str
    email: str
    dob: str
    district: str
    monthly_income: float
    disability_status: bool = False
    utility_ids: dict = {}

    class Config:
        orm_mode = True


class CitizenInDB(Citizen):
    id: str
