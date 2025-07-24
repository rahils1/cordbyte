from discord import ui
import discord

class ButtonView(ui.View):
    """
    A custom View that displays a list of buttons.
    
    Parameters:
        buttons (list[tuple[str, Callable]]): 
            A list of tuples where each tuple contains:
            - A label (str) for the button
            - A callback function to run when the button is pressed
        embed_color (int): 
            The color used for the embed that buttons may modify. Defaults to Discord blurple (0x5865F2).
    
    Usage:
        ButtonView(
            buttons=
            [
                ("Option 1", callback1), 
                ("Option 2", callback2)
            ]
        )
    """
    def __init__(self, *, buttons, embed_color=0x5865F2):
        super().__init__(timeout=None)

        for button, func in buttons:
            self.add_item(UIButton(button, embed_color, func))

class UIButton(ui.Button):
    """
    A single clickable Discord UI button with a callback handler.

    Parameters:
        message (str): The text displayed on the button.
        color (int): The color to use in the embed shown after clicking.
        callback_func (Callable): A coroutine function to call when the button is clicked.

    The callback function must have the signature:
        async def callback(interaction: discord.Interaction, embed_color: int)
    """
    def __init__(self, message: str, color, callback_func):
        super().__init__(label=message, style=discord.ButtonStyle.primary)
        self.message = message
        self.callback_func = callback_func
        self.embed_color = color

    async def callback(self, interaction):
        """
        Called when the button is clicked.
        Forwards the interaction and embed color to the provided callback function.
        """
        await self.callback_func(interaction, self.embed_color)