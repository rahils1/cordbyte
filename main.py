import os
import importlib
from src.Secrets import BOT_TOKEN
from src.core.Decorators.RegisterCommand import registered_commands
from src.Bot import bot
from src.core.Decorators.RegisterTask import registered_tasks

def load_all_command_modules():
    """
    Dynamically imports all Python files in the 'src/bot/commands' folder
    to register commands via the @register_command decorator.
    """
    folder = "src/bot/commands"
    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            importlib.import_module(f"src.bot.commands.{module_name}")

def load_all_task_modules():
    """
    Dynamically imports all Python files in the 'src/bot/events' folder
    to register background tasks via the @register_task decorator.
    """
    folder = "src/bot/events"
    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            importlib.import_module(f"src.bot.events.{module_name}")

@bot.event
async def setup_hook():
    """
    This special async event is called by discord.py when the bot is ready to set up.
    It loads all commands and tasks, registers slash commands with Discord, and
    starts any background tasks that were registered.
    """
    load_all_command_modules()
    load_all_task_modules()

    # Register all commands to the bot's command tree
    for cmd in registered_commands:
        bot.tree.add_command(cmd)

    # Sync commands with Discord's servers (slash commands appear)
    await bot.tree.sync()

    # Start all registered background tasks if not already running
    for task in registered_tasks:
        if not task.is_running():
            task.start()

@bot.event
async def on_ready(): 
    """
    Called when the bot has successfully connected and is ready.
    """
    print(f"Logged in as {bot.user}")

bot.run(BOT_TOKEN) # Run the bot with the token from environment variables/secrets