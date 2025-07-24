from src.core.Database.Models import getModel
from src.core.Decorators.RegisterCommand import register_command
from discord import app_commands, Embed

@register_command
@app_commands.command(name="unsub", description="Unsubscribe this channel to stop receiving updates")
async def unsub(interaction):
    """
    Slash command to unsubscribe the current channel from receiving updates.

    When called, this command will:
    1. Access the "channels" collection from MongoDB (or your configured DB).
    2. Attempt to delete a document where the `_id` matches the current channel's ID.
    3. Respond with a message indicating whether the unsubscribe was successful.

    Note:
    - This is a basic implementation using MongoDB.
    - In production, you might want to include extra metadata, audit logs, or use soft deletes.
    """
    await interaction.response.defer(thinking=True)

    model = await getModel("channels")  # Retrieve the MongoDB collection

    if model is not None:
        # Attempt to delete the channel's subscription entry
        result = model.delete_one({"_id": str(interaction.channel.id)})

        if result.deleted_count > 0:
            # If the document was deleted, confirmation is sent
            await interaction.followup.send(
                embed=Embed(
                    title="Unsubscribed!",
                    description="This channel has been unsubscribed and will no longer receive updates.",
                    color=0x5865F2,
                )
            )
        else:
            # If the document didn't exist, let the user know
            await interaction.followup.send(
                embed=Embed(
                    title="Not Subscribed",
                    description="This channel was not subscribed to updates.",
                    color=0x5865F2,
                )
            )
    else:
        # Fallback response if DB connection failed
        await interaction.followup.send(
            embed=Embed(
                title="Sorry, there was a problem",
                description="This channel could not be unsubscribed. Please try again later.",
                color=0x5865F2,
            )
        )