from agents import Agent
from helpers import fetch_citizen_data
from config import model

application_drafting_agent = Agent(
    name="Application Drafting Agent",
    instructions=(
        "You are an application assistant. Pre-fill the application form for a citizen based on the provided data."
    ),
    model=model,  # Use OpenAI model to generate application form
    tools=[fetch_citizen_data],
)
