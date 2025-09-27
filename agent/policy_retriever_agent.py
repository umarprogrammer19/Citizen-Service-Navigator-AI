import requests
from agents import Agent
from PyPDF2 import PdfReader  # Python PDF library for PDF parsing


class PolicyRetrieverAgent(Agent):
    def retrieve_policy(self, url):
        try:
            # Fetch PDF or other policy documents
            response = requests.get(url)

            if response.status_code == 200:
                # If it's a PDF, parse it
                if url.endswith(".pdf"):
                    policy_data = self.parse_pdf(response.content)
                    return policy_data
                else:
                    # If it's JSON or another format, try parsing
                    try:
                        return response.json()
                    except ValueError:
                        print(f"Error: Response from {url} is not valid JSON.")
                        return None
            else:
                print(
                    f"Error: Failed to retrieve data from {url}, Status Code: {response.status_code}"
                )
                return None
        except requests.exceptions.RequestException as e:
            print(
                f"Error: Network error occurred while fetching the policy data. {str(e)}"
            )
            return None

    def parse_pdf(self, pdf_content):
        reader = PdfReader(pdf_content)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
