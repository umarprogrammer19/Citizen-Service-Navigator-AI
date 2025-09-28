from agents import Agent
from agent.eligibility_agent import eligibility_agent
from agent.drafting_agent import application_drafting_agent
from agent.guidance_agent import guidance_agent
from agent.explanation_agent import explanation_agent
from agent.offline_agent import offline_mode_agent


class Orchestrator:
    def __init__(self):
        self.eligibility_agent = eligibility_agent
        self.drafting_agent = application_drafting_agent
        self.guidance_agent = guidance_agent
        self.explanation_agent = explanation_agent
        self.offline_agent = offline_mode_agent

    def process_query(self, citizen_data: dict, is_offline=False):
        if is_offline:
            eligibility = self.offline_agent.run(citizen_data)
        else:
            eligibility = self.eligibility_agent.run(citizen_data)

        if eligibility:
            application = self.drafting_agent.run(citizen_data)
            guidance = self.guidance_agent.run(citizen_data)
            return {
                "status": "Eligible",
                "application": application,
                "guidance": guidance,
            }
        else:
            explanation = self.explanation_agent.run(citizen_data)
            return {"status": "Ineligible", "message": explanation}
