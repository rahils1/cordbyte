import os
from dotenv import load_dotenv

# Load environment variables from a .env file located at the project root
# This allows you to keep sensitive information like tokens and URIs out of source code
load_dotenv()

# Discord bot token - make sure to set this in your .env file as BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB connection URI - set this in .env as MONGODB_URI
MONGODB_URI = os.getenv("MONGODB_URI")

# Name of the MongoDB database to use - set this in .env as DB_NAME
DB_NAME = os.getenv("DB_NAME")

"""
Notes:
- Never commit your .env file or any files containing sensitive credentials to public repositories.
- Always use environment variables or secret management services for credentials.
- You can create a .env file with these entries like:

    BOT_TOKEN=your_discord_bot_token_here
    MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net
    DB_NAME=your_database_name

- The python-dotenv package must be installed (`pip install python-dotenv`).
"""