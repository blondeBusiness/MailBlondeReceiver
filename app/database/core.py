# app/database/core.py
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "test")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set in environment (.env)")

# client is global to reuse connections
_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

def get_client() -> MongoClient:
    """Return the pymongo MongoClient (lazy connected)."""
    return _client


def get_db():
    """Return the configured database instance."""
    return _client[MONGO_DB_NAME]


def ping():
    """Optional: test connection to MongoDB. Raises on failure."""
    try:
        # will raise ServerSelectionTimeoutError if cannot connect
        _client.admin.command("ping")
        return True
    except ServerSelectionTimeoutError:
        return False


def close_client():
    """Close the global client (call on shutdown)."""
    _client.close()

