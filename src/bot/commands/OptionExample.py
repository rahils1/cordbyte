from discord import app_commands, Interaction, Embed
from typing import Literal
from src.core.Decorators.RegisterCommand import register_command 

@register_command
@app_commands.command( name="select_example", description="An example slash command that responds to a selected option.")
async def select_example(interaction: Interaction, option: Literal["Option A", "Option B", "Option C"]):
    """
    A slash command that lets the user select from preset options.
    
    Parameters:
    1. interaction (Interaction): The interaction object triggered by the user.
    2. option: A fixed list of choices the user can select from: "Option A", "Option B", or "Option C". Modify the option list for your desired list of options
    
    Behavior:
    Sends back a confirmation embed that echoes the user's selected option.
    """
    await interaction.response.defer(thinking=True)

    await interaction.followup.send(
        embed=Embed(
            title="Command: /select_example",
            description=f"You selected **{option}**.",
            color=0x5865F2
        )
    )