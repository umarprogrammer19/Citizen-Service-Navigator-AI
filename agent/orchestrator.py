from agents import Agent
from agent.policy_retriever_agent import PolicyRetrieverAgent
from agent.eligibility_evaluator_agent import EligibilityEvaluatorAgent
from agent.form_filler_agent import FormFillerAgent
from agent.explainer_agent import ExplainerAgent


class OrchestratorAgent(Agent):
    def orchestrate(self, citizen_data):
        # Orchestrate agents to handle citizen eligibility, form filling, and explanation
        policy_agent = PolicyRetrieverAgent(name="PolicyRetriever Agent")

        # Retrieve eligibility rules, with fallback if None
        rules = policy_agent.retrieve_policy("https://example.com/eligibility_policy")
        if not rules:
            print("Warning: Using fallback eligibility rules due to retrieval failure.")
            rules = {
                "program_id": "housing_support_lahore_2025",
                "eligibility": [
                    {"field": "monthly_income", "op": "<=", "value": 50000},
                    {
                        "field": "district",
                        "op": "in",
                        "value": ["Lahore", "Sheikhupura"],
                    },
                    {"field": "household_size", "op": ">=", "value": 2},
                ],
                "required_docs": ["CNIC", "utility bill copy", "income certificate"],
                "form_url": "https://example.com/form",
            }

        eligibility_agent = EligibilityEvaluatorAgent(name="Eligibility Evaluator Agent")
        is_eligible = eligibility_agent.evaluate_eligibility(citizen_data, rules)

        if is_eligible:
            form_agent = FormFillerAgent(name="Form Filler Agent")
            filled_form = form_agent.fill_form(citizen_data)

            explainer_agent = ExplainerAgent("Explainer Agent")
            explanation = explainer_agent.explain(is_eligible)
            return {
                "eligibility": "Eligible",
                "form": filled_form,
                "explanation": explanation,
            }

        return {"eligibility": "Not Eligible"}
