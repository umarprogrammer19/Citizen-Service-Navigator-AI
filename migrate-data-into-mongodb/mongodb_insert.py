import json
from pymongo import MongoClient

# MongoDB connection URI (replace this with your connection string)
MONGODB_URI = "mongodb+srv://umarofficial0121_db_user:Ugsofficial190807@cluster0.rejq5v4.mongodb.net/"  

# Connect to MongoDB
client = MongoClient(MONGODB_URI)

# Create or connect to the database
db = client["citizen_service_db"]

# Create collections for citizen data, services, and messages
citizens_collection = db["citizens"]
services_collection = db["services"]
messages_collection = db["citizen_messages"]

# Load the mock data from the JSON files
with open("pakistan_citizen_mock_data_expanded.json") as f:
    citizens_data = json.load(f)

with open("citizen_services_mock_data_full.json") as f:
    services_data = json.load(f)

with open("citizen_messages_mock_updated.json") as f:
    messages_data = json.load(f)


# Insert data into MongoDB collections
def insert_data():
    # Insert citizen data
    if citizens_collection.count_documents({}) == 0:  # Avoid duplicate insertions
        citizens_collection.insert_many(citizens_data)
        print(f"Inserted {len(citizens_data)} citizen records.")

    # Insert service data
    if services_collection.count_documents({}) == 0:  # Avoid duplicate insertions
        services_collection.insert_many(services_data)
        print(f"Inserted {len(services_data)} service records.")

    # Insert messages data
    if messages_collection.count_documents({}) == 0:  # Avoid duplicate insertions
        messages_collection.insert_many(messages_data)
        print(f"Inserted {len(messages_data)} message records.")


if __name__ == "__main__":
    insert_data()
