from src.core.Buttons.ButtonView import ButtonView
from src.core.Decorators.RegisterCommand import register_command
from discord import app_commands, Embed

@register_command
@app_commands.command(name="button_example", description="An example slash command that responds to a selected button.")
async def button_example(interaction):
    """
    This is a slash command that demonstrates how interactive buttons can be used.
    When the command is used, the bot sends an ephemeral embed with two buttons: Option 1 and Option 2.
    """
    await interaction.response.defer(thinking=True)
    
    await interaction.followup.send(
        embed=Embed(
            title="Command: /button_example",
            description="Click one of the buttons below:",
            color=0x5865F2
        ),
        view=ButtonView(
            # Pass in an array of tuples. 
            # Each tuple defines a button:
            # The first element is the button label (str)
            # The second is a coroutine function (async def) that accepts (interaction, embed_color) as its parameters
            buttons=[
                ("Option 1", option1),
                ("Option 2", option2)
            ]
        ),
        ephemeral=True  # Only visible to the user who ran the command, remove if you want the embed to be visible to anyone
    )

async def option1(interaction, embed_color):
    """
    Callback function for the 'Option 1' button.
    
    Parameters:
    - interaction: The Discord interaction object for the button click
    - embed_color: Color of the embed (passed by ButtonView)
    """
    embed = Embed(title="You chose:", description="Option 1", color=embed_color)
    await interaction.response.edit_message(embed=embed, view=None)

async def option2(interaction, embed_color):
    """
    Callback function for the 'Option 2' button.
    
    Parameters:
    - interaction: The Discord interaction object for the button click
    - embed_color: Color of the embed (passed by ButtonView)
    """
    embed = Embed(title="You chose:", description="Option 2", color=embed_color)
    await interaction.response.edit_message(embed=embed, view=None)