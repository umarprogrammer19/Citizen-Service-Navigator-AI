from agents import Agent
from agent.eligibility_agent import eligibility_agent
from agent.application_process import application_drafting_agent
from agent.explanation_agent import explanation_agent
from config import model

# Orchestrator Agent
orchestrator_agent = Agent(
    name="Orchestrator",
    instructions="Orchestrates the citizen service process by invoking eligibility, application drafting, and explanation agents.",
    tools=[
        eligibility_agent.as_tool(
            tool_name="eligibility_check",
            tool_description="Evaluate if the citizen is eligible for the service.",
        ),
        application_drafting_agent.as_tool(
            tool_name="draft_application",
            tool_description="Pre-fill application forms.",
        ),
        explanation_agent.as_tool(
            tool_name="provide_explanation",
            tool_description="Provide explanation for ineligibility.",
        ),
    ],
    model=model,
)
