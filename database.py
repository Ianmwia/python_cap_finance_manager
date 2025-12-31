from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["finance_manager"]

income_collection = db["incomes"]
expense_collection = db["expenses"]
users_collection = db["users"]

#total_users = users_collection.count_documents({})
#print(total_users)