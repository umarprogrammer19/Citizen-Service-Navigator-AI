from pydantic import BaseModel


class CitizenMessage(BaseModel):
    case_id: str
    citizen_id: str
    request_text: str
    request_type: str
    timestamp: str
    citizen_profile: dict
