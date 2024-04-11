import pymongo
from dotenv import load_dotenv
import os

load_dotenv()


def connectDB():
    ConnectionString  = os.getenv("CONNECTION_STR")

    client = pymongo.MongoClient(ConnectionString)

    db = client["compareX"]
    collection = db["users"]

    return collection;