# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dpyhr']

package_data = \
{'': ['*']}

install_requires = \
['watchdog>=2.2.1,<3.0.0']

setup_kwargs = {
    'name': 'dpyhr',
    'version': '0.1.0',
    'description': 'dpyhr. A discord.py module reloader written in pure python!',
    'long_description': "# dpyhr\ndpyhr is a hot cog reloader (that uses discord.py cog's implementation) to reload anytime you wanted to save!\n\n## Setup\n\n1. Install dpyhr with pip (`pip install dpyhr`)\n2. Import dpyhr and run it with\n\n```py\nimport dpyhr\n\ndpyhr.run(bot: commands.Bot, *paths: str, selection: Selection = Selection.normal, reloader: typing.Callable=None, conditional: typing.Callable=None, recursive: bool=False, **kwargs)\n```\n\n`dpyhr.run` have a documentation as this\n\n> Run dphyr in another thread.\n\n>   Args:\n>        bot (commands.Bot): For reloading extensions (if reloader doesn't exists)\n>        selection (Selection, optional): Observer selection. Defaults to Selection.normal.\n>        reloader (typing.Callable, optional): Reload module with your own function. Defaults to None.\n>        conditional (typing.Callable, optional): Conditional when event is triggered. Defaults to None.\n>       recursive (bool, optional): Recursive reloading. Defaults to False.\n>        **kwargs: Other arguments for observer.\n>    Returns:\n>        None: No returns.\n\n## Caution\n\ndpyhr wouldn't work if you called your bot outside of the entrypoint starter so nested path wouldn't work in this case. you need to run it inside directory where you want python file to run else reloader might get wrong path and spits errors out.\n",
    'author': 'timelessnesses',
    'author_email': 'mooping3roblox@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/timelessnesses/dpyhr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
