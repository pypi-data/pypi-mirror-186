# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quiltsync',
 'quiltsync.AboutScreen',
 'quiltsync.LoginScreen',
 'quiltsync.Package',
 'quiltsync.Resource']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.3,<0.24.0',
 'kivymd>=1.1.1,<2.0.0',
 'quiltplus>=0.6.0,<0.7.0',
 'trio>=0.22.0,<0.23.0']

entry_points = \
{'console_scripts': ['quiltsync = quiltsync.main:run']}

setup_kwargs = {
    'name': 'quiltsync',
    'version': '0.1.0',
    'description': 'Graphical desktop client to sync Quilt data packages between local filesystems and cloud object stores',
    'long_description': "# quiltsync\nGraphical desktop client for synchronizing local filesystems with cloud object stores\n\n## Usage\n\n```\npip install quiltsync\nquiltsync\n```\n\n## Running from Git\n\n```\ngit clone https://github.com/quiltdata/quiltsync.git\ncd quiltsync\npoetry install # OR: 'poetry update'\nDEBUG=1 poetry run quiltsync/main.py # enable hot-reload\npoetry run quiltsync # run CLI\n```\n\n## Development\n\n```\npoetry env use python\npoetry run pytest\npoetry run ptw\n```\n\n## Releases\nBe sure you to first set your [API token](https://pypi.org/manage/account/) using `poetry config pypi-token.pypi <pypi-api-token>`\n\n```\npoetry update\npoetry version patch\npoetry build && poetry publish\npoetry version prepatch\n```\n\n# Implementation\n\n## Kivy\n\nUses the [Kivy UI framework](https://kivy.org/doc/stable/html) for cross-platform Python applications.\nSpecifically, the [KivyMD Material Design toolkit](https://kivymd.readthedocs.io) for Kivy.\n\n## Poetry\n\nUse `[poetry](https://python-poetry.org/docs/)` to manage both dependencies and the virtual environment:\n\n### Installing Poetry\n\n```\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -\n# WINDOWS: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -\n```\n",
    'author': 'Ernest Prabhakar',
    'author_email': 'ernest@quiltdata.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
