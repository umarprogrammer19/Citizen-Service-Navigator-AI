from pymongo import MongoClient
import os

MONGODB_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGODB_URL)
db = client["citizen_service_db"]

citizens_collection = db["citizens"]
services_collection = db["services"]
messages_collection = db["citizen_messages"]


# Fetch citizen data based on citizen_id
def get_citizen_data(citizen_id: str):
    return citizens_collection.find_one({"citizen_id": citizen_id})


# Fetch service data based on service_id
def get_service_data(service_id: str):
    return services_collection.find_one({"service_id": service_id})


# Fetch citizen messages based on case_id
def get_citizen_messages(case_id: str):
    return messages_collection.find_one({"case_id": case_id})
