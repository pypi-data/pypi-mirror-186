# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgework']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0',
 'debugpy>=1.6.3,<2.0.0',
 'forge-core>=1.0.0,<2.0.0',
 'honcho>=1.1.0,<2.0.0',
 'hupper>=1.10.3,<2.0.0',
 'python-dotenv']

entry_points = \
{'console_scripts': ['forge-work = forgework:cli']}

setup_kwargs = {
    'name': 'forge-work',
    'version': '1.0.0',
    'description': 'Work library for Forge',
    'long_description': '# forge-work\n\nA single command to run everything you need for local Django development.\n\n![Forge work command example](https://user-images.githubusercontent.com/649496/176533533-cfd44dc5-afe5-42af-8b5d-33a9fa23f8d9.gif)\n\nThe following processes will run simultaneously (some will only run if they are detected as available):\n\n- [`manage.py runserver` (and migrations)](#runserver)\n- [`forge-db start --logs`](#forge-db)\n- [`forge-tailwind compile --watch`](#forge-tailwind)\n- [`npm run watch`](#package-json)\n- [`stripe listen --forward-to`](#stripe)\n- [`ngrok http --subdomain`](#ngrok)\n- [`celery worker`](#celery)\n\nIt also comes with [debugging](#debugging) tools to make local debugging easier with VS Code.\n\n## Installation\n\n### Django + Forge Quickstart\n\nIf you use the [Forge Quickstart](https://www.forgepackages.com/docs/forge/quickstart/),\neverything you need will be ready and available as `forge work`.\n\n### Install for existing Django projects\n\nFirst, install `forge-work` from [PyPI](https://pypi.org/project/forge-work/):\n\n```sh\npip install forge-work\n```\n\nNow instead of using the basic `manage.py runserver` (and a bunch of commands before and during that process), you can simply do:\n\n```sh\nforge work\n```\n\n## Development processes\n\n### Runserver\n\nThe key process here is still `manage.py runserver`.\nBut, before that runs, it will also wait for the database to be available and run `manage.py migrate`.\n\n### forge-db\n\nIf [`forge-db`](https://github.com/forgepackages/forge-db) is installed, it will automatically start and show the logs of the running database container.\n\n### forge-tailwind\n\nIf [`forge-tailwind`](https://github.com/forgepackages/forge-tailwind) is installed, it will automatically run the Tailwind `compile --watch` process.\n\n### package.json\n\nIf a `package.json` file is found and contains a `watch` script,\nit will automatically run.\nThis is an easy place to run your own custom JavaScript watch process.\n\n### Stripe\n\nIf a `STRIPE_WEBHOOK_PATH` env variable is set then this will add a `STRIPE_WEBHOOK_SECRET` to `.env` (using `stripe listen --print-secret`) and it will then run `stripe listen --forward-to <runserver:port/stripe-webhook-path>`.\n\n### Ngrok\n\nIf an `NGROK_SUBDOMAIN` env variable is set then this will run `ngrok http <runserver_port> --subdomain <subdomain>`.\nNote that [ngrok](https://ngrok.com/download) will need to be installed on your system already (however you prefer to do that).\n\n### Celery\n\nIf a `CELERY_APP` env variable is set, then an autoreloading celery worker will be started automatically.\n\n## Debugging\n\n[View on YouTube →](https://www.youtube.com/watch?v=pG0KaJSVyBw)\n\nSince `forge work` runs multiple processes at once, the regular [pdb](https://docs.python.org/3/library/pdb.html) debuggers can be hard to use.\nInstead, we include [microsoft/debugpy](https://github.com/microsoft/debugpy) and an `attach` function to make it even easier to use VS Code\'s debugger.\n\nFirst, import and run the `debug.attach()` function:\n\n```python\nclass HomeView(TemplateView):\n    template_name = "home.html"\n\n    def get_context_data(self, **kwargs):\n        context = super().get_context_data(**kwargs)\n\n        # Make sure the debugger is attached (will need to be if runserver reloads)\n        from forgework import debug; debug.attach()\n\n        # Add a breakpoint (or use the gutter in VSCode to add one)\n        breakpoint()\n\n        return context\n```\n\nWhen you load the page, you\'ll see "Waiting for debugger to attach...".\n\nAdd a new VS Code debug configuration (using localhost and port 5768) by saving this to `.vscode/launch.json` or using the GUI:\n\n```json\n// .vscode/launch.json\n{\n    // Use IntelliSense to learn about possible attributes.\n    // Hover to view descriptions of existing attributes.\n    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387\n    "version": "0.2.0",\n    "configurations": [\n        {\n            "name": "Forge: Attach to Django",\n            "type": "python",\n            "request": "attach",\n            "connect": {\n                "host": "localhost",\n                "port": 5678\n            },\n            "pathMappings": [\n                {\n                    "localRoot": "${workspaceFolder}",\n                    "remoteRoot": "."\n                }\n            ],\n            "justMyCode": true,\n            "django": true\n        }\n    ]\n}\n```\n\nThen in the "Run and Debug" tab, you can click the green arrow next to "Forge: Attach to Django" to start the debugger.\n\nIn your terminal is should tell you it was attached, and when you hit a breakpoint you\'ll see the debugger information in VS Code.\nIf Django\'s runserver reloads, you\'ll be prompted to reattach by clicking the green arrow again.\n',
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.forgepackages.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
