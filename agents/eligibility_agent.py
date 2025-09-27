from agents import Agent

class EligibilityAgent(Agent):
    def __init__(self, rules_db):
        self.rules_db = rules_db

    def evaluate_eligibility(self, citizen_data):
        # extract eligibility rules for the given district
        rules = self.rules_db.get_rules(citizen_data["district"])

        eligible = True
        for rule in rules:
            if not self.apply_rule(rule, citizen_data):
                eligible = False
                break

        return eligible

    def apply_rule(self, rule, citizen_data):
        if (
            rule["field"] == "monthly_income"
            and citizen_data["monthly_income"] > rule["value"]
        ):
            return False
        return True
