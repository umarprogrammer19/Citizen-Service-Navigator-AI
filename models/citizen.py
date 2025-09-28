from pydantic import BaseModel


class Citizen(BaseModel):
    citizen_id: str
    first_name: str
    last_name: str
    age: int
    income_per_month_pkr: int
    housing_status: str
    service_requested: str
