from fastapi import FastAPI
from pydantic import BaseModel
from agent.query_agent import handle_query

app = FastAPI()


# Citizen Data Schema
class CitizenData(BaseModel):
    citizen_id: str


# Service Data Schema
class ServiceData(BaseModel):
    service_id: str
    query_type: str  # Could be 'eligibility', 'documents', or 'application'


@app.post("/ask-agent/")
async def ask_agent(citizen_data: CitizenData, service_data: ServiceData):
    response = handle_query(
        citizen_data.citizen_id, service_data.service_id, service_data.query_type
    )
    return response
