
from pymongo import MongoClient
from src.config.config import Config

# Establish MongoDB connection
client = MongoClient(Config.DATABASE_URI)
db = client[Config.DB_NAME]

def store_deposit(deposit):
    try:
        deposit_dict = deposit.to_dict()
        result = db.deposits.insert_one(deposit_dict)
        return result.inserted_id
    except Exception as e:
        print(f'Error storing deposit: {e}')
        raise