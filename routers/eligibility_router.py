from fastapi import APIRouter, HTTPException
from models.citizen import Citizen
from agent.orchestrator import OrchestratorAgent

router = APIRouter()


@router.post("/check-eligibility")
async def check_eligibility(citizen_data: Citizen):
    orchestrator_agent = OrchestratorAgent()
    result = orchestrator_agent.orchestrate(citizen_data.dict())

    if result["eligibility"] == "Not Eligible":
        raise HTTPException(
            status_code=400, detail="Not eligible for the requested services"
        )

    return result
