import requests
from agents import Agent


class PolicyRetrieverAgent(Agent):
    def retrieve_policy(self, url):
        try:
            # Send GET request to fetch policy data
            response = requests.get(url)

            # Check if the response status code is 200 (OK)
            if response.status_code == 200:
                try:
                    # Attempt to parse the JSON response
                    policy_data = response.json()
                    return policy_data
                except ValueError:
                    # Handle case where the response is not JSON
                    print(f"Error: Response from {url} is not valid JSON.")
                    return None
            else:
                print(
                    f"Error: Failed to retrieve data from {url}, Status Code: {response.status_code}"
                )
                return None
        except requests.exceptions.RequestException as e:
            # Catch and log any network-related errors
            print(
                f"Error: Network error occurred while fetching the policy data. {str(e)}"
            )
            return None
