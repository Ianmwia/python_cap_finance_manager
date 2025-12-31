from pymongo import MongoClient

MONGO_URI = "mongodb+srv://iansnr10_db_user:5RX8IPaawRZm9kxK@financemanagercluster.vxpefms.mongodb.net/?appName=financemanagercluster"

client = MongoClient(MONGO_URI)

db = client["finance_manager"]

income_collection = db["incomes"]
expense_collection = db["expenses"]
users_collection = db["users"]
