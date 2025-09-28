from fastapi import APIRouter, HTTPException
from models.citizen import Citizen
from agent.orchestrator_agent import OrchestratorAgent

router = APIRouter()


@router.post("/check-eligibility")
async def check_eligibility(citizen_data: Citizen):
    orchestrator_agent = OrchestratorAgent()
    result = orchestrator_agent.orchestrate(citizen_data.dict())

    if result["eligibility"] == "Not Eligible":
        raise HTTPException(
            status_code=400, detail="Not eligible for the requested services"
        )

    # Return the generated PDF if eligible
    if result.get("form"):
        return result["form"]  # This is the StreamingResponse containing the PDF
    else:
        return {
            "eligibility": result["eligibility"],
            "explanation": result["explanation"],
        }
