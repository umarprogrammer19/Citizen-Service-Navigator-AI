from agents import Agent


class EligibilityEvaluatorAgent(Agent):
    def evaluate_eligibility(self, citizen_data, rules):
        eligible = True
        for rule in rules:
            if (
                rule["field"] == "monthly_income"
                and citizen_data["monthly_income"] > rule["value"]
            ):
                eligible = False
                break
        return eligible
