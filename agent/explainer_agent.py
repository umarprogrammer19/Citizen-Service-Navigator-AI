from agents import Agent


class ExplainerAgent(Agent):
    def explain(self, eligibility_result):
        # explanation = f"You qualify for the housing support because your monthly income is within the limit."
        self.eligibility_result = eligibility_result
        return eligibility_result
