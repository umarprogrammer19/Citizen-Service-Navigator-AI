from database.mongo_connection import get_citizen_data, get_service_data
from agents import Agent
from config import model

# Eligibility Agent
eligibility_agent = Agent(
    name="Eligibility Agent",
    instructions="Determine if the citizen qualifies for a specific service based on their profile and the service's eligibility criteria.",
    model=model,  
    tools=[get_citizen_data, get_service_data], 
)


def evaluate_eligibility(citizen_id: str, service_id: str):
    citizen_data = get_citizen_data(citizen_id)
    service_data = get_service_data(service_id)

    if citizen_data and service_data:
        # Check eligibility criteria based on mock data
        eligibility_criteria = service_data["eligibility_criteria"]

        # Logic to compare citizen data with service criteria
        # Example: Income comparison, family status, etc.
        eligible = True
        for key, value in eligibility_criteria.items():
            if citizen_data.get(key) != value:
                eligible = False
                break

        return {
            "eligible": eligible,
            "message": "You are eligible" if eligible else "You are not eligible",
        }
    return {"status": "Error", "message": "Citizen or service data not found"}
