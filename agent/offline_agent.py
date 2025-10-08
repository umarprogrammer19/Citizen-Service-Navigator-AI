from agents import Agent
from config import model

# Degraded Mode Offline 
offline_mode_agent = Agent(
    name="Offline Mode Agent",
    instructions=(
        "Perform simplified eligibility checks in offline mode using basic data such as income and housing status."
    ),
    model=model,
)
