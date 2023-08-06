# dpyhr
dpyhr is a hot cog reloader (that uses discord.py cog's implementation) to reload anytime you wanted to save!

## Setup

1. Install dpyhr with pip (`pip install dpyhr`)
2. Import dpyhr and run it with

```py
import dpyhr

dpyhr.run(bot: commands.Bot, *paths: str, selection: Selection = Selection.normal, reloader: typing.Callable=None, conditional: typing.Callable=None, recursive: bool=False, **kwargs)
```

`dpyhr.run` have a documentation as this

> Run dphyr in another thread.

>   Args:
>        bot (commands.Bot): For reloading extensions (if reloader doesn't exists)
>        selection (Selection, optional): Observer selection. Defaults to Selection.normal.
>        reloader (typing.Callable, optional): Reload module with your own function. Defaults to None.
>        conditional (typing.Callable, optional): Conditional when event is triggered. Defaults to None.
>       recursive (bool, optional): Recursive reloading. Defaults to False.
>        **kwargs: Other arguments for observer.
>    Returns:
>        None: No returns.

## Caution

dpyhr wouldn't work if you called your bot outside of the entrypoint starter so nested path wouldn't work in this case. you need to run it inside directory where you want python file to run else reloader might get wrong path and spits errors out.
