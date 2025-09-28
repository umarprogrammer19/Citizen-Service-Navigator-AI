# from agents import Runner
# from agent.eligibility_agent import eligibility_agent
# from agent.drafting_agent import application_drafting_agent
# from agent.guidance_agent import guidance_agent
# from agent.explanation_agent import explanation_agent
# from agent.offline_agent import offline_mode_agent
# from agent.document_requirement_agent import document_agent
# from agent.application_process import application_process_agent


# class Orchestrator:
#     def __init__(self):
#         # Ensure these are Agent instances, not just references to functions
#         self.eligibility_agent = eligibility_agent
#         self.drafting_agent = application_drafting_agent
#         self.guidance_agent = guidance_agent
#         self.explanation_agent = explanation_agent
#         self.offline_agent = offline_mode_agent
#         self.document_agent = document_agent
#         self.application_process_agent = application_process_agent

#     async def process_question(
#         self,
#         question: str,
#         citizen_data: dict = None,
#         service_data: dict = None,
#         is_offline=False,
#     ):
#         """Process a question asked by the citizen and route it to the appropriate agent."""

#         # Handle specific questions about eligibility
#         if "eligible" in question.lower() or "eligibility" in question.lower():
#             if citizen_data and service_data:
#                 # Use the correct Agent instance, not just the function
#                 result = await Runner.run(self.eligibility_agent, citizen_data)
#                 return result.final_output
#             else:
#                 return {"status": "Error", "message": "Missing citizen or service data"}

#         # Handle questions about required documents
#         elif "documents" in question.lower():
#             if service_data:
#                 result = await Runner.run(self.document_agent, service_data)
#                 return result.final_output
#             else:
#                 return {"status": "Error", "message": "Missing service data"}

#         # Handle questions about the application process
#         elif "apply" in question.lower() or "application" in question.lower():
#             if service_data:
#                 application = await Runner.run(
#                     self.application_process_agent, service_data
#                 )
#                 guidance = await Runner.run(self.guidance_agent, service_data)
#                 return {
#                     "status": "Application Process",
#                     "application": application.final_output,
#                     "guidance": guidance.final_output,
#                 }
#             else:
#                 return {"status": "Error", "message": "Missing service data"}

#         # Handle offline queries
#         elif "offline" in question.lower():
#             if citizen_data:
#                 eligibility = await Runner.run(self.offline_agent, citizen_data)
#                 return {
#                     "status": "Offline Eligibility",
#                     "eligibility": eligibility.final_output,
#                 }
#             else:
#                 return {"status": "Error", "message": "Missing citizen data"}

#         # Handle general or unknown queries
#         else:
#             return {
#                 "status": "Unknown",
#                 "message": "Sorry, I could not understand the question. Please ask about eligibility, documents, or application.",
#             }
from agents import Runner
from agent.eligibility_agent import eligibility_agent
from agent.drafting_agent import application_drafting_agent
from agent.guidance_agent import guidance_agent
from agent.explanation_agent import explanation_agent
from agent.offline_agent import offline_mode_agent
from agent.document_requirement_agent import document_agent
from agent.application_process import application_process_agent

class Orchestrator:
    def __init__(self):
        # Ensure these are Agent instances, not just references to functions
        self.eligibility_agent = eligibility_agent
        self.drafting_agent = application_drafting_agent
        self.guidance_agent = guidance_agent
        self.explanation_agent = explanation_agent
        self.offline_agent = offline_mode_agent
        self.document_agent = document_agent
        self.application_process_agent = application_process_agent

    async def process_question(
        self,
        question: str,
        citizen_data: dict = None,
        service_data: dict = None,
        is_offline=False,
    ):
        """Process a question asked by the citizen and route it to the appropriate agent."""
        
        # Handle specific questions about eligibility
        if "eligible" in question.lower() or "eligibility" in question.lower():
            if citizen_data and service_data:
                result = await Runner.run(self.eligibility_agent, f"{citizen_data}, {service_data}")
                return result.final_output
            else:
                return {"status": "Error", "message": "Missing citizen or service data"}

        # Handle questions about required documents
        elif "documents" in question.lower():
            if service_data:
                result = await Runner.run(self.document_agent, service_data)
                return result.final_output
            else:
                return {"status": "Error", "message": "Missing service data"}

        # Handle questions about the application process
        elif "apply" in question.lower() or "application" in question.lower():
            if service_data:
                application = await Runner.run(self.application_process_agent, service_data)
                guidance = await Runner.run(self.guidance_agent, service_data)
                return {
                    "status": "Application Process",
                    "application": application.final_output,
                    "guidance": guidance.final_output,
                }
            else:
                return {"status": "Error", "message": "Missing service data"}

        # Handle offline queries
        elif "offline" in question.lower():
            if citizen_data:
                eligibility = await Runner.run(self.offline_agent, citizen_data)
                return {
                    "status": "Offline Eligibility",
                    "eligibility": eligibility.final_output,
                }
            else:
                return {"status": "Error", "message": "Missing citizen data"}

        # Handle general or unknown queries
        else:
            return {
                "status": "Unknown",
                "message": "Sorry, I could not understand the question. Please ask about eligibility, documents, or application.",
            }
