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

    def process_question(
        self, question: str, citizen_data: dict = None, is_offline=False
    ):
        """Process the question asked by the citizen and direct it to the appropriate agent."""
        if "eligible" in question.lower() or "eligibility" in question.lower():
            # If the question is about eligibility
            if citizen_data:
                eligibility = self.eligibility_agent.run(citizen_data)
                if eligibility:
                    return {
                        "status": "Eligible",
                        "message": "You are eligible for the requested service.",
                    }
                else:
                    return {
                        "status": "Ineligible",
                        "message": "You are not eligible for the requested service.",
                    }
            else:
                return {"status": "Error", "message": "No citizen data provided."}

        elif "apply" in question.lower() or "application" in question.lower():
            # If the question is about applying for a service
            if citizen_data:
                application = self.drafting_agent.run(citizen_data)
                guidance = self.guidance_agent.run(citizen_data)
                return {
                    "status": "Eligible",
                    "application": application,
                    "guidance": guidance,
                }
            else:
                return {"status": "Error", "message": "No citizen data provided."}

        elif "documents" in question.lower():
            # If the question is about required documents
            return {
                "status": "Information",
                "message": "Required documents: CNIC, recent utility bill, etc.",
            }

        elif "offline" in question.lower():
            # If the question is related to offline status
            eligibility = self.offline_agent.run(citizen_data)
            return {"status": "Offline Eligibility", "eligibility": eligibility}

        else:
            return {"status": "Unknown", "message": "I don't understand the question."}
