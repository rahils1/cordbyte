import asyncio
from discord import Embed
from discord.ext import tasks
import datetime
from src.core.Decorators.RegisterTask import register_task
from src.Bot import bot
from src.core.Database.Models import getModel

testTime = datetime.time(hour=12, minute=0, tzinfo=datetime.timezone.utc)

@register_task
@tasks.loop(time=testTime) # You can also do hours/minutes/seconds=n for an update every n hours/minutes/seconds
async def send_update():
    """
    Scheduled task that sends a daily update message to all subscribed channels.

    How it works:
    - Runs every day at 12:00 UTC (changeable via the `testTime` variable).
    - Loads the "channels" collection from MongoDB.
    - Iterates over every channel ID (_id) in the collection and sends an embedded update message.
    - Sleeps 1.5 seconds between messages to avoid hitting rate limits.

    Notes:
    - This example uses a simple `_id`-based subscription model with MongoDB.
    - You can expand this logic to include filters like guilds, tags, roles, or categories.
    - Failed sends (e.g., missing permissions) are caught and logged to the console.
    """
    model = await getModel("channels")
    
    if model is not None:
        # Get all documents representing subscribed channels
        subscriptions = list(model.find())

        # Message embed to be sent to each channel
        embed = Embed(
            title="Update!",
            description="This is the message that you've subscribed for. To unsubscribe, use the `/unsub` command.",
            color=0x5865F2
        )
        
        for sub in subscriptions:
            try:
                # Each subscription's _id is assumed to be the channel ID
                channel = bot.get_channel(int(sub["_id"]))
                if channel is not None:
                    await channel.send(embed=embed)
                    await asyncio.sleep(1.5)  # Prevent Discord rate limits
            except Exception as e:
                print(f"Failed to send update to channel {sub['_id']}: {e}")