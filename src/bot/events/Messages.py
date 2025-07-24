from src.Bot import bot

@bot.event
async def on_message(message):
    """
    Event listener for every message sent in a channel the bot can see.

    Skips:
    - Messages from bots (including itself)

    Extend this function to:
    - Respond to certain phrases or keywords
    - Log messages
    - Implement custom triggers
    - Create mini-games, reaction roles, etc.

    Important:
    - If you're using `commands.Bot`, this overrides the default command processing.
      To fix that, you must add `await bot.process_commands(message)` at the end
      if you still want slash/message commands to work.
    """
    if message.author.bot: return

    # TODO: Add your custom message handling logic here
    # Example:
    # if "hello" in message.content.lower(): await message.channel.send("Hi there!")