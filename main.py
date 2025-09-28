# from fastapi import FastAPI
# from pydantic import BaseModel
# from agent.orchestrator_agent import Orchestrator

# app = FastAPI()


# # Citizen Data Schema
# class CitizenData(BaseModel):
#     citizen_id: str
#     first_name: str
#     last_name: str
#     age: int
#     income_per_month_pkr: int
#     housing_status: str
#     service_requested: str


# # Service Data Schema
# class ServiceData(BaseModel):
#     service_id: str
#     query_type: str  # Could be 'eligibility', 'documents', or 'application'


# # Question Query Schema
# class QuestionData(BaseModel):
#     question: str
#     citizen_data: CitizenData = None
#     service_data: ServiceData = None
#     is_offline: bool = False


# @app.post("/ask-agent/")
# async def ask_agent(question_data: QuestionData):
#     orchestrator = Orchestrator()
#     # Asynchronously process the question
#     response = await orchestrator.process_question(
#         question_data.question,
#         citizen_data=(
#             question_data.citizen_data.dict() if question_data.citizen_data else None
#         ),
#         service_data=(
#             question_data.service_data.dict() if question_data.service_data else None
#         ),
#         is_offline=question_data.is_offline,
#     )
#     return response

from fastapi import FastAPI
from pydantic import BaseModel
from agent.orchestrator_agent import Orchestrator
from agents import Runner

app = FastAPI()


# Citizen Data Schema
class CitizenData(BaseModel):
    citizen_id: str
    first_name: str
    last_name: str
    age: int
    income_per_month_pkr: int
    housing_status: str
    service_requested: str


# Service Data Schema
class ServiceData(BaseModel):
    service_id: str
    query_type: str  # Could be 'eligibility', 'documents', or 'application'


# Question Query Schema
class QuestionData(BaseModel):
    question: str
    citizen_data: CitizenData = None
    service_data: ServiceData = None
    is_offline: bool = False


@app.post("/ask-agent/")
async def ask_agent(question_data: QuestionData):
    orchestrator = Orchestrator()
    # Asynchronously process the question
    response = await Runner.run(
        orchestrator,
        question_data.question,
    )
    # response = await orchestrator.process_question(
    #     question_data.question,
    #     citizen_data=(
    #         question_data.citizen_data.dict() if question_data.citizen_data else None
    #     ),
    #     service_data=(
    #         question_data.service_data.dict() if question_data.service_data else None
    #     ),
    #     is_offline=question_data.is_offline,
    # )
    return response.final_output
