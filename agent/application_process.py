from agents import Agent
from helpers import get_service_data
from config import model

application_process_agent = Agent(
    name="Application Process Agent",
    instructions="Provide the step-by-step application process for a service.",
    model=model,
    tools=[get_service_data],  # Fetch service data to get application steps
)


def get_application_process(service_id: str):
    service_data = get_service_data(service_id)
    if service_data:
        return {
            "application_process": service_data.get("application_process_steps", [])
        }
    return {"status": "Error", "message": "Service not found"}
