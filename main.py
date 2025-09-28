from fastapi import FastAPI
from pydantic import BaseModel
from agent.orchestrator_agent import orchestrator_agent
from pymongo import MongoClient
from agents import Runner
import os
from database.mongo_connection import get_citizen_data, get_service_data

app = FastAPI()

client = MongoClient(os.environ.get("MONGODB_URL"))
db = client["citizen_service_db"]
citizens_collection = db["citizens"]
services_collection = db["services"]


class CitizenData(BaseModel):
    citizen_id: str
    first_name: str
    last_name: str
    age: int
    income_per_month_pkr: int
    housing_status: str
    service_requested: str


class ServiceData(BaseModel):
    service_id: str
    query_type: str


@app.post("/ask-agent/")
async def ask_agent(question_data):
    citizen_data = get_citizen_data(question_data.citizen_data.citizen_id)

    service_data = get_service_data(question_data.service_data.service_id)

    result = await Runner.run(
        orchestrator_agent, input=question_data, context=[citizen_data, service_data]
    )
    return result.final_output
