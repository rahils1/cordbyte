from src.Secrets import MONGODB_URI, DB_NAME
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Initialize the client and database reference
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

try:
    print("Connecting to Database...")
    client.admin.command('ping')  # Try pinging the server to confirm connection
    print("Successfully connected to MongoDB.")
except ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")

# NOTE:
# This setup is specific to my MongoDB configuration and PyMongo.
# If you are using a different database (e.g., PostgreSQL, MySQL, SQLite),
# you will need to configure your connection differently.
# Always ensure your database credentials and connection parameters
# are correctly set up for your environment.