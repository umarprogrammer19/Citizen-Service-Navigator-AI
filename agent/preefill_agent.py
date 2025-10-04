from agents import Agent
from config import model

application_drafting_agent = Agent(
    name="Application Drafting Agent",
    instructions="This agent helps the citizen pre-fill application forms for eligible services.",
    model=model,
)
