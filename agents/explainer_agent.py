from agents import Agent


class ExplainerAgent(Agent):
    def explain_eligibility(self, citizen_data):
        explanation = f"Based on your income of {citizen_data['monthly_income']}, you are eligible for housing support."
        return explanation
