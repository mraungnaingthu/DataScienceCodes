from dotenv import load_dotenv
import os

load_dotenv()

class MongoConfig:
    """This is MongoDB Configuration"""
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")