from database.mongo_connection import get_citizen_data, get_service_data
from agents import function_tool


@function_tool
def fetch_citizen_data(citizen_id: str):
    citizen_data = get_citizen_data(citizen_id)
    return citizen_data


@function_tool
def fetch_service_data(service_id: str):
    service_data = get_service_data(service_id)
    return service_data
