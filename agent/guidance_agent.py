from agents import Agent
from config import model

guidance_agent = Agent(
    name="Guidance Agent",
    instructions=(
        "You provide detailed step-by-step instructions for citizens to apply for a service, "
        "including necessary documents and application procedures."
    ),
    model=model,
)
