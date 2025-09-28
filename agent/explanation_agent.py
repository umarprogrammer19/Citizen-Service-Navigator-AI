from agents import Agent
from config import model

explanation_agent = Agent(
    name="Explanation Agent",
    instructions=(
        "If a citizen is ineligible for a service, provide clear, understandable explanations for why they are not eligible. "
        "Offer suggestions for alternative services if possible."
    ),
    model=model,
)
