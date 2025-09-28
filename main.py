from fastapi import FastAPI
from pydantic import BaseModel
from agent.orchestrator_agent import Orchestrator

app = FastAPI()


class CitizenData(BaseModel):
    citizen_id: str
    first_name: str
    last_name: str
    age: int
    income_per_month_pkr: int
    housing_status: str
    service_requested: str


@app.post("/citizen-query/")
async def citizen_query(citizen_data: CitizenData, is_offline: bool = False):
    orchestrator = Orchestrator()
    result = orchestrator.process_query(citizen_data.dict(), is_offline)
    return result
