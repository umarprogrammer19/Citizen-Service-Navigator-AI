from agents import Agent
from helpers import fetch_citizen_data, fetch_service_data
from config import model

eligibility_agent = Agent(
    name="Eligibility Agent",
    instructions=(
        "You will evaluate whether a citizen is eligible for a given public service based on the provided data "
        "such as income, housing status, and other relevant factors."
    ),
    model=model,  # Use OpenAI model for complex evaluation
    tools=[fetch_citizen_data, fetch_service_data],
)
