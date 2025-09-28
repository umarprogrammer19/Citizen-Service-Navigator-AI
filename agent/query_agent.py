from agents import Agent
from config import model
from agent.eligibility_agent import eligibility_agent
from agent.document_requirement_agent import document_agent
from agent.application_process import application_process_agent

query_agent = Agent(
    name="Query Handling Agent",
    instructions="Handle a citizen's request by processing the query and referring to the relevant service or citizen data.",
    model=model,
    tools=[
        eligibility_agent.as_tool(),
        document_agent.as_tool(),
        application_process_agent.as_tool(),
    ],
)


def handle_query(citizen_id: str, service_id: str, query_type: str):
    if query_type == "eligibility":
        return eligibility_agent.run(citizen_id, service_id)
    elif query_type == "documents":
        return document_agent.run(service_id)
    elif query_type == "application":
        return application_process_agent.run(service_id)
    else:
        return {"status": "Error", "message": "Invalid query type"}
