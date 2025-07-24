# Cordbyte — Discord Bot Template

Cordbyte is a modular and easy-to-extend Discord bot template built with [discord.py](https://discordpy.readthedocs.io/).  
It supports slash commands, interactive buttons, background tasks, and MongoDB integration.

---

## Features

- Slash commands with automatic registration  
- Button-based interactive commands  
- Background tasks with easy decorators  
- MongoDB integration for persistent storage  
- Environment variable configuration for secrets

---

## Getting Started

### Prerequisites

- Python 3.9+  
- MongoDB instance (local or cloud)  
- Discord Bot Token with **Message Content Intent** enabled in Discord Developer Portal

### Discord Bot Setup & OAuth2 Scopes

1. In the [Discord Developer Portal](https://discord.com/developers/applications), create your bot and copy its **Client ID** and **Token**.

2. Under **OAuth2 > URL Generator**, select these scopes to invite your bot:  
   - `bot`  
   - `applications.commands`

3. For permissions, either:  
   - Check **Administrator** (for full privileges, easier setup but less secure), or  
   - Select only the permissions your bot needs, such as:  
     - Send Messages  
     - Manage Messages  
     - Embed Links  
     - Use Slash Commands

4. Copy the generated invite URL and use it to add the bot to your server.


### Installation

1. Clone this repository  
   ```bash
   git clone https://github.com/rahils1/cordbyte.git
   cd cordbyte
   ```
2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file in the project root with the following variables:
   ```ini
   BOT_TOKEN=your_discord_bot_token_here
   MONGODB_URI=your_mongodb_connection_string
   DB_NAME=your_database_name
   ```
5. Run the bot
   ```bash
   python main.py
   ```
