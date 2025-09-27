from pydantic import BaseModel


class Citizen(BaseModel):
    cnic: str
    name: str
    dob: str
    district: str
    monthly_income: float
    disability_status: bool
    household_size: int
    utility_customer_ids: dict

    class Config:
        orm_mode = True
