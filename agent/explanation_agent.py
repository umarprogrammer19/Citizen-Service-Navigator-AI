from agents import Agent
from config import model

explanation_agent = Agent(
    name="Explanation Agent",
    instructions="This agent provides a plain-language explanation for a citizen's ineligibility for a service.",
    model=model,
)
