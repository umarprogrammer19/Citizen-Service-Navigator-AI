from agents import Agent
import requests


class PolicyRetrieverAgent(Agent):
    def retrieve_policy(self, url):
        response = requests.get(url)
        policy_data = response.json() 
        return policy_data
