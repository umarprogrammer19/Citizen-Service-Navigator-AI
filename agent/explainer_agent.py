from agents import Agent


class ExplainerAgent(Agent):
    def explain(self, is_eligible):
        if is_eligible:
            explanation = "You qualify for the program based on your income and district eligibility."
        else:
            explanation = "You do not qualify for the program due to certain eligibility criteria."
        return explanation
