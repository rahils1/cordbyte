from src.core.Database.Models import getModel
from src.core.Decorators.RegisterCommand import register_command
from discord import app_commands, Embed

@register_command
@app_commands.command(name="sub", description="Subscribe this channel to receive updates")
async def sub(interaction):
    """
    Slash command to subscribe the current channel to receive updates.
    
    When called, this command will:
    1. Access the "channels" collection from MongoDB (or your configured DB).
    2. Insert or update a document where the `_id` is the channel ID.
    3. Respond with a confirmation message.

    Note:
    - This is a minimal MongoDB example. In a production app, your database schema
      and logic will likely be more complex (e.g., managing multiple subscriptions, user preferences, etc.).
    - The `getModel` returns a MongoDB collection-like object.
    """
    await interaction.response.defer(thinking=True)  # Show a loading state while processing

    model = await getModel("channels")  # Retrieve the MongoDB collection

    if model is not None:
        # Insert the channel's subscription entry
        model.find_one_and_update(
            {"_id": str(interaction.channel.id)},
            {"$set": {}},
            upsert=True     # Insert if it doesn't exist
        )

        # Success response
        await interaction.followup.send(
            embed=Embed(
                title="Subscribed!",
                description="This channel has been subscribed and will receive updates.",
                color=0x5865F2,
            )
        )
    else:
        # Fallback response if DB is not available
        await interaction.followup.send(
            embed=Embed(
                title="Sorry, there was a problem",
                description="This channel could not be subscribed. Please try again later.",
                color=0x5865F2,
            )
        )