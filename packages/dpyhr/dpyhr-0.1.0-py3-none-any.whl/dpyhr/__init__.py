"""
dphyr
A simple module for support hot reloading of discord.py "cogs" (extensions).
"""
import enum
from .normal import normal_start, Normal
from .polling import polling_start, Polling
import discord.ext.commands as commands
import typing

class Selection(enum.Enum):
    
    polling = Polling
    normal = Normal
    
def run(bot: commands.Bot, *paths: str, selection: Selection = Selection.normal, reloader: typing.Callable=None, conditional: typing.Callable=None, recursive: bool=False, **kwargs) -> None:
    """Run dphyr in another thread.

    Args:
        bot (commands.Bot): For reloading extensions (if reloader doesn't exists)
        selection (Selection, optional): Observer selection. Defaults to Selection.normal.
        reloader (typing.Callable, optional): Reload module with your own function. Defaults to None.
        conditional (typing.Callable, optional): Conditional when event is triggered. Defaults to None.
        recursive (bool, optional): Recursive reloading. Defaults to False.
        **kwargs: Other arguments for observer.
    Returns:
        None: No returns.
    """
    if not reloader:
        reloader = bot.reload_extension
    if not conditional:
        conditional = lambda event: event.src_path.endswith(".py")
    if selection == Selection.normal:
        normal_start(*paths, reloader=reloader, condition=conditional, recursive=recursive, **kwargs)
    elif selection == Selection.polling:
        polling_start(*paths, reloader=reloader, condition=conditional, recursive=recursive, **kwargs)
    else:
        raise ValueError("Invalid selection")