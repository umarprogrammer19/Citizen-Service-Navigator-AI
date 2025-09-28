from agents import Agent
from helpers import get_service_data
from config import model

document_agent = Agent(
    name="Document Requirements Agent",
    instructions="Provide the list of required documents for a specific service based on the service ID.",
    model=model,
    tools=[get_service_data],
)


def get_required_documents(service_id: str):
    service_data = get_service_data(service_id)
    if service_data:
        return {"required_documents": service_data.get("required_documents", [])}
    return {"status": "Error", "message": "Service not found"}
