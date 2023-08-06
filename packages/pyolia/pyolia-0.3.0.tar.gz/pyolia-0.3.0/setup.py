# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyolia']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.1,<4.0.0', 'backoff>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'pyolia',
    'version': '0.3.0',
    'description': 'Async Python wrapper to interact with internal Veolia API',
    'long_description': '<p align=center>\n    <img src="https://upload.wikimedia.org/wikipedia/fi/thumb/2/2a/Veolia-logo.svg/250px-Veolia-logo.svg.png"/>\n</p>\n\n<p align=center>\n    <a href="https://pypi.org/project/pyolia/"><img src="https://img.shields.io/pypi/v/pyolia.svg"/></a>\n    <a href="https://github.com/tetienne/python-veolia-api/actions"><img src="https://github.com/tetienne/python-veolia-api/workflows/CI/badge.svg"/></a>\n    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>\n</p>\n\nSmall client to retrieve the water consumption from Veolia website: https://www.eau-services.com\n\n## Remarks\nVeolia publishes water consumption with a delay of 3 days. It  means if we are the 14, you will be only able to retrieve your data from the 11.\nTo retrieve the hourly water consumption, you have to update your preferences on this [page](https://www.eau-services.com/mon-espace-suivi-personnalise.aspx).\n\n## Installation\n\n```bash\npip install pyolia\n```\n\n## Getting started\n\n```python\nimport asyncio\nfrom datetime import datetime, timedelta\n\nfrom pyolia.client import VeoliaClient\n\n\nUSERNAME = "your username"\nPASSWORD = "your password"\n\nasync def main() -> None:\n    async with VeoliaClient(USERNAME, PASSWORD) as client:\n        now = datetime.now()\n        if now.day < 4:\n            now = now - timedelta(days=3)\n        consumption = await client.get_consumption(now.month, now.year)\n        print(consumption)\n        now = now - timedelta(days=3)\n        consumption = await client.get_consumption(now.month, now.year, now.day)\n        print(consumption)\n\n\nasyncio.run(main())\n```\n\n## Development\n\n### Installation\n\n- For Linux, install [pyenv](https://github.com/pyenv/pyenv) using [pyenv-installer](https://github.com/pyenv/pyenv-installer)\n- For MacOS, run `brew install pyenv`\n- Don\'t forget to update your `.bashrc` file (or similar):\n  ```\n  export PATH="~/.pyenv/bin:$PATH"\n  eval "$(pyenv init -)"\n  ```\n- Install the required [dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)\n- Install [poetry](https://python-poetry.org): `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`\n\n- Clone this repository\n- `cd python-veolia-api`\n- Install the required Python version: `pyenv install`\n- Init the project:\xa0`poetry install`\n- Run `poetry run pre-commit install`\n\n## PyCharm\n\nAs IDE you can use [PyCharm](https://www.jetbrains.com/pycharm/).\n\nUsing snap, run `snap install pycharm --classic` to install it.\n\nFor MacOS, run `brew cask install pycharm-ce`\n\nOnce launched, don\'t create a new project, but open an existing one and select the **python-veolia-api** folder.\n\nGo to _File | Settings | Project: nre-tag | Project Interpreter_. Your interpreter must look like `<whatever>/python-veolia-api/.venv/bin/python`\n',
    'author': 'Thibaut Etienne',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tetienne/python-veolia-api/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
