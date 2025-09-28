from fastapi import FastAPI
from pydantic import BaseModel
from agent.orchestrator_agent import Orchestrator

app = FastAPI()


# Define the CitizenData schema (to be used for citizen-related questions)
class CitizenData(BaseModel):
    citizen_id: str
    first_name: str
    last_name: str
    age: int
    income_per_month_pkr: int
    housing_status: str
    service_requested: str


# Define the QuestionData schema
class QuestionData(BaseModel):
    question: str
    citizen_data: CitizenData = None
    is_offline: bool = False


@app.post("/ask-agent/")
async def ask_agent(question_data: QuestionData):
    orchestrator = Orchestrator()

    # Pass the question and citizen data to the orchestrator
    response = orchestrator.process_question(
        question_data.question,
        citizen_data=(
            question_data.citizen_data.dict() if question_data.citizen_data else None
        ),
        is_offline=question_data.is_offline,
    )

    return response
