"""
A simple decorator module to register background tasks.

Use `@register_task` to decorate your async task functions (e.g., `@tasks.loop` coroutines),
so they get added to the global `registered_tasks` list. This list can then be iterated over
during bot startup to start all registered tasks automatically.

Example:
    @register_task
    @tasks.loop(minutes=1)
    async def my_background_task():
        # Task logic here
        pass

Later in your bot setup:
    for task in registered_tasks:
        if not task.is_running():
            task.start()
"""

registered_tasks = []

def register_task(task):
    """
    Decorator to register a task coroutine.

    Args:
        task (Callable): The coroutine function representing the background task.

    Returns:
        The original task coroutine (unchanged).
    """
    registered_tasks.append(task)
    return task
