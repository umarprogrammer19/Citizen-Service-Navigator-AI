from agents import Agent


class EligibilityEvaluatorAgent(Agent):
    def evaluate_eligibility(self, citizen_data, rules):
        if not isinstance(rules, list):
            return False  # Return false if rules are not valid

        eligible = True
        for rule in rules:
            field = rule["field"]
            operator = rule["op"]
            value = rule["value"]

            # Basic checks for field comparisons
            if operator == "<=" and citizen_data[field] > value:
                eligible = False
            elif operator == ">=" and citizen_data[field] < value:
                eligible = False
            elif operator == "in" and citizen_data[field] not in value:
                eligible = False

        return eligible
