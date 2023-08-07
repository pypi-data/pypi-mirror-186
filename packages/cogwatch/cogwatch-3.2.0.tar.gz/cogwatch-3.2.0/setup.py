# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cogwatch']

package_data = \
{'': ['*']}

install_requires = \
['watchfiles>=0.15,<0.16']

entry_points = \
{'console_scripts': ['example = runner:__poetry_run', 'fmt = scripts:fmt']}

setup_kwargs = {
    'name': 'cogwatch',
    'version': '3.2.0',
    'description': 'Automatic hot-reloading for your discord.py (or other supported libaries) command files.',
    'long_description': '<h1 align="center">Cog Watch</h1>\n    \n<div align="center">\n  <strong><i>Automatic hot-reloading for your discord.py command files.</i></strong>\n  <br>\n  <br>\n  \n  <a href="https://pypi.org/project/cogwatch">\n    <img src="https://img.shields.io/pypi/v/cogwatch?color=0073B7&label=Latest&style=for-the-badge" alt="Version" />\n  </a>\n  \n  <a href="https://python.org">\n    <img src="https://img.shields.io/pypi/pyversions/cogwatch?color=0073B7&style=for-the-badge" alt="Python Version" />\n  </a>\n</div>\n<br>\n\n`cogwatch` is a utility that you can plug into your `discord.py` bot *(or various\nsupported bot libraries)* that will watch your command files directory *(cogs)*\nand automatically reload them as you modify or move them around in real-time.\n\nNo more reloading your bot manually every time you edit an embed just to make\nsure it looks perfect!\n\n\n<img align="center" src="assets/example.png" alt="">\n<br><br>\n\n## Features\n\n- Automatically reloads commands in real-time as you edit them *(no !reload\n  <command_name> needed)*.\n- Can handle the loading of all your commands on start-up *(removes boilerplate)*.\n\n## Supported Libraries\n\n`cogwatch` *should* work with any library that forked from `discord.py`.\nHowever, these libraries have been explicitly tested to work:\n\n- [discord.py](https://discordpy.readthedocs.io/en/stable/)\n- [nextcord](https://docs.nextcord.dev/en/stable/)\n- [discord4py](https://docs.discord4py.dev/en/developer/)\n- [disnake](https://disnake.readthedocs.io/en/latest/)\n- [pycord](https://docs.pycord.dev/en/stable/)\n\n## Getting Started\n\nYou can install the library with `pip install cogwatch`.\n\nImport the `watch` decorator and apply it to your `on_ready` method and let the\nmagic take effect.\n\nSee the [examples](https://github.com/robertwayne/cogwatch/tree/master/examples)\ndirectory for more details.\n\n```python\nimport asyncio\nfrom discord.ext import commands\nfrom cogwatch import watch\n\n\nclass ExampleBot(commands.Bot):\n    def __init__(self):\n        super().__init__(command_prefix=\'!\')\n\n    @watch(path=\'commands\', preload=True)\n    async def on_ready(self):\n        print(\'Bot ready.\')\n\n    async def on_message(self, message):\n        if message.author.bot:\n            return\n\n        await self.process_commands(message)\n\n\nasync def main():\n    client = ExampleBot()\n    await client.start(\'YOUR_TOKEN_GOES_HERE\')\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n```\n\n## Configuration\n\nYou can pass any of these values to the decorator:\n\n`path=\'commands\'`: Root name of the cogs directory; cogwatch will only watch within this directory -- recursively.\n\n`debug`: Whether to run the bot only when the Python **\\_\\_debug\\_\\_** flag is True. Defaults to True.\n\n`loop`: Custom event loop. Defaults to the current running event loop.\n\n`default_logger`: Whether to use the default logger *(to sys.stdout)* or not. Defaults to True.\n\n`preload`: Whether to detect and load all found cogs on start. Defaults to False.\n\n`colors`: Whether to use colorized terminal outputs or not. Defaults to True.\n\n**NOTE:** `cogwatch` will only run if the **\\_\\_debug\\_\\_** flag is set on\nPython. You can read more about that\n[here](https://docs.python.org/3/library/constants.html). In short, unless you\nrun Python with the *-O* flag from your command line, **\\_\\_debug\\_\\_** will be\n**True**. If you just want to bypass this feature, pass in `debug=False` and it\nwon\'t matter if the flag is enabled or not.\n\n## Logging\n\nBy default, the utility has a logger configured so users can get output to the\nconsole. You can disable this by passing in `default_logger=False`. If you want\nto hook into the logger -- for example, to pipe your output to another terminal\nor `tail` a file -- you can set up a custom logger like so:\n\n```python\nimport logging\nimport sys\n\nwatch_log = logging.getLogger(\'cogwatch\')\nwatch_log.setLevel(logging.INFO)\nwatch_handler = logging.StreamHandler(sys.stdout)\nwatch_handler.setFormatter(logging.Formatter(\'[%(name)s] %(message)s\'))\nwatch_log.addHandler(watch_handler)\n```\n',
    'author': 'Rob Wagner',
    'author_email': 'rob@sombia.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/robertwayne/cogwatch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
