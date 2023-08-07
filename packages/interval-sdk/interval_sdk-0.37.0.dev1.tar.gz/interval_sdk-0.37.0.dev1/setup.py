# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['interval_sdk', 'interval_sdk.classes', 'interval_sdk.components']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'typing-extensions>=4.4.0,<5.0.0',
 'websockets>=10.1,<11.0']

setup_kwargs = {
    'name': 'interval-sdk',
    'version': '0.37.0.dev1',
    'description': 'Python SDK for Interval.',
    'long_description': '# interval-sdk\n\n## Installation\n\nInstall using pip, (or your python package manager of choice):\n\n```\npip install interval-sdk\n```\n\n## API\n\n*Note:* Proper documentation is in progress!\n\nSee `src/demos/basic.py` and `src/tests` for a better overview, but in short:\n\n```python\nfrom interval_sdk import Interval, IO\n\n# Initialize Interval\ninterval = Interval("API_KEY")\n\n# Add an action using the function name as the slug\n@interval.action\nasync def hello_interval():\n    return {"hello": "from python!"}\n\n# Add an action using a custom slug (can contain hyphens) and additional configuration\n@interval.action(slug=\'echo-message\', unlisted=True)\nasync def echo_message(io: IO):\n    [message] = await io.group(io.input.text("Hello!", help_text="From python!"))\n\n    return {"message": message}\n\n\n# Synchronously listen, blocking forever\ninterval.listen()\n```\n\nTo not block, interval can also be run asynchronously using\n`interval.listen_async()`. You must provide your own event loop.\n\nThe task will complete as soon as connection to Interval completes, so you\nlikely want to run forever or run alongside another permanent task.\n\n```python\nimport asyncio\n\n# This is what synchronous `listen()` does under the hood\nloop = asyncio.get_event_loop()\nloop.create_task(interval.listen_async())\nloop.run_forever()\n```\n\nIf you are using `run_forever()`, you\'ll probably want to add signal handlers\nto close the loop gracefully on process termination:\n\n```python\nimport asyncio, signal\n\nloop = asyncio.get_event_loop()\nloop.create_task(interval.listen_async())\nfor sig in {signal.SIGINT, signal.SIGTERM}:\n    loop.add_signal_handler(sig, loop.stop)\nloop.run_forever()\n```\n\n\n## Contributing\n\nThis project uses [Poetry](https://python-poetry.org/) for dependency\nmanagement\n\n1. `poetry install` to install dependencies\n2. `poetry shell` to activate the virtual environment\n\nTasks are configured using [poethepoet](https://github.com/nat-n/poethepoet)\n(installed as a dev dependency).\n\n- `poe demo [demo_name]` to run a demo (`basic` by default if `demo_name` omitted)\n- `poe test` to run `pytest` (can also run `pytest` directly in virtual env)\n\nCode is formatted using [Black](https://github.com/psf/black). Please configure\nyour editor to format on save using Black, or run `poe format` to format the\ncode before committing changes.\n\n## Tests\n\n*Note:* Tests currently require a local instance of the Interval backend.\n\nTests use [pytest](https://docs.pytest.org/en/7.1.x/) and\n[playwright](https://playwright.dev/python/).\n\nCurrently assumes the `test-runner@interval.com` user exists already.\nRun `yarn test` in the `web` directory at least once to create it before\nrunning these.\n',
    'author': 'Jacob Mischka',
    'author_email': 'jacob@interval.com',
    'maintainer': 'Jacob Mischka',
    'maintainer_email': 'jacob@interval.com',
    'url': 'https://interval.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
