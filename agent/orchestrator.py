from agents import Agent
from agent.policy_retriever_agent import PolicyRetrieverAgent
from agent.eligibility_evaluator_agent import EligibilityEvaluatorAgent
from agent.form_filler_agent import FormFillerAgent
from agent.explainer_agent import ExplainerAgent


class OrchestratorAgent(Agent):
    def orchestrate(self, citizen_data):
        # Step 1: Retrieve Policy
        policy_agent = PolicyRetrieverAgent(name="Policy Retriever Agent")
        rules = policy_agent.retrieve_policy("https://zakat.punjab.gov.pk/forms")

        if not rules:
            print("Warning: Using fallback eligibility rules due to retrieval failure.")
            rules = [
                {"field": "monthly_income", "op": "<=", "value": 50000},
                {"field": "district", "op": "in", "value": ["Lahore", "Sheikhupura"]},
                {"field": "household_size", "op": ">=", "value": 2},
            ]

        # Step 2: Evaluate Eligibility
        eligibility_agent = EligibilityEvaluatorAgent(
            name="Eligibility Evaluator Agent"
        )
        is_eligible = eligibility_agent.evaluate_eligibility(citizen_data, rules)

        # Step 3: Fill Forms if Eligible
        form_agent = FormFillerAgent(name="Form Filler Agent")
        filled_form = form_agent.fill_form(citizen_data) if is_eligible else None

        # Step 4: Provide Explanation
        explainer_agent = ExplainerAgent(name="Explainer Agent")
        explanation = explainer_agent.explain(is_eligible)

        return {
            "eligibility": "Eligible" if is_eligible else "Not Eligible",
            "form": filled_form,
            "explanation": explanation,
        }
