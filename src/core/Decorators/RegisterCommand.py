"""
A simple decorator module to register slash commands.

Use `@register_command` to decorate your command functions so they get added
to the global `registered_commands` list, which can then be iterated over to
add commands to the bot's command tree during setup.

Example:
    @register_command
    @app_commands.command(name="hello", description="Say hello")
    async def hello_command(interaction):
        await interaction.response.send_message("Hello!")

Later in your bot setup:
    for cmd in registered_commands:
        bot.tree.add_command(cmd)
"""

registered_commands = []

def register_command(command):
    """
    Decorator to register a command function.

    Args:
        command (Callable): The command coroutine function to register.

    Returns:
        The original command function (unchanged).
    """
    registered_commands.append(command)
    return command