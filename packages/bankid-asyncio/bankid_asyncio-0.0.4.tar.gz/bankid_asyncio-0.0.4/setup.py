# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bankid_asyncio', 'bankid_asyncio.clients']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'pydantic>=1.9.2,<2.0.0']

setup_kwargs = {
    'name': 'bankid-asyncio',
    'version': '0.0.4',
    'description': 'BankID client for Python with asyncio support.',
    'long_description': '# bankid-asyncio 🏦\n\n## Badges 🏷\n![GitHub](https://img.shields.io/github/license/Kostiantyn-Salnykov/bankid_asyncio)\n![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/Kostiantyn-Salnykov/bankid_asyncio/python-package.yml?branch=main)\n![GitHub (branch)](https://img.shields.io/badge/branch-main-brightgreen)\n![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Kostiantyn-Salnykov/bankid_asyncio/main)\n[![codecov](https://codecov.io/gh/Kostiantyn-Salnykov/bankid_asyncio/branch/main/graph/badge.svg?token=F4XO2O9DXY)](https://codecov.io/gh/Kostiantyn-Salnykov/bankid_asyncio)\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bankid-asyncio)\n![PyPI - Format](https://img.shields.io/pypi/format/bankid-asyncio)\n![PyPI](https://img.shields.io/pypi/v/bankid-asyncio)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/bankid-asyncio)\n\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000?style=flat)](https://github.com/psf/black)\n\n## Dependencies ⛓\n\n[![Pydantic](https://img.shields.io/badge/pydantic-%5E1.10.1-orange)](https://pydantic-docs.helpmanual.io/)\n[![HTTPX](https://img.shields.io/badge/httpx-%5E0.23.0-orange)](https://www.python-httpx.org/)\n\n## Description 📖\n**bankid-asyncio** - is a BankID client for Python with asyncio support.\n\nAsynchronous realization turned out to be implemented due to the fact that the library is written based on HTTPX, which \nallows not only synchronous requests (**Client**), but also asynchronous ones (**AsyncClient**).\n\n## Install 💾\n\n### pip\n```{.terminal linenums="0"}\npip install bankid-asyncio\n```\n\n### Poetry\n```{.terminal linenums="0"}\npoetry add bankid-asyncio\n```\n\n## Documentation 🗂 (In progress)\n[Documentation🔗](https://kostiantyn-salnykov.github.io/bankid_asyncio/)\n',
    'author': 'Kostiantyn Salnykov',
    'author_email': 'kostiantyn.salnykov@gmail.com',
    'maintainer': 'Kostiantyn Salnykov',
    'maintainer_email': 'kostiantyn.salnykov@gmail.com',
    'url': 'https://kostiantyn-salnykov.github.io/bankid_asyncio/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
