from database.mongo_connection import get_citizen_data, get_service_data
from agents import Agent, ModelSettings
from config import model

from agents import function_tool


@function_tool
def check_eligibility(citizen_data, service_data):
    """
    This function checks if a citizen is eligible for a particular service.
    It uses criteria stored in the `service_data` and matches it with the `citizen_data`.
    """
    eligibility_criteria = service_data["eligibility_criteria"]

    # Check eligibility based on the criteria
    if (
        citizen_data["age"] >= eligibility_criteria["min_age"]
        and citizen_data["income_per_month_pkr"] <= eligibility_criteria["max_income"]
    ):
        return {"eligible": True, "message": "You are eligible for the service."}
    else:
        return {"eligible": False, "message": "You are not eligible for the service."}


# Eligibility Agent
eligibility_agent = Agent(
    name="Eligibility Agent",
    instructions="Determine if the citizen qualifies for a specific service based on their profile and the service's eligibility criteria.",
    model=model,
    model_settings=ModelSettings(tool_choice="required"),
    tools=[check_eligibility, get_citizen_data, get_service_data],
)
