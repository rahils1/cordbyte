import discord
from discord.ext import commands

# Set up Discord intents - these define what events your bot will receive.
intents = discord.Intents.default()
intents.message_content = True  # Enables the bot to read message content (needed for on_message and message commands)

# Initialize the bot instance.
# command_prefix is the prefix for text commands (if you use them).
# You can change it to anything, or even make it a list of prefixes.
bot = commands.Bot(command_prefix="!/!/!/!/!", intents=intents)

"""
Notes:
- If you only use slash commands (app_commands), prefix is optional.
- The 'message_content' intent is required to read message content from users.
- Make sure you have enabled the "Message Content Intent" in the Discord Developer Portal for your bot.
"""