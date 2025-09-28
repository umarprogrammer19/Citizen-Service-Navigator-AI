from pydantic import BaseModel


class Service(BaseModel):
    service_id: str
    service_name: str
    description: str
    eligibility_criteria: dict
    required_documents: list
    application_process_steps: list
