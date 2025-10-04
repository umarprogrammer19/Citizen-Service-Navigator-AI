from pymongo import MongoClient
from agents import function_tool
import os

MONGODB_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGODB_URL)
db = client["citizen_service_db"]

citizens_collection = db["citizens"]
services_collection = db["services"]
messages_collection = db["citizen_messages"]


@function_tool
def get_citizen_data(citizen_id: str):
    return citizens_collection.find_one({"citizen_id": citizen_id})


@function_tool
def get_service_data(service_id: str):
    return services_collection.find_one({"service_id": service_id})


@function_tool
def get_citizen_messages(case_id: str):
    return messages_collection.find_one({"case_id": case_id})
