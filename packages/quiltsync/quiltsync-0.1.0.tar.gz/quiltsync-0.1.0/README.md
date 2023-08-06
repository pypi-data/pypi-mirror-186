# quiltsync
Graphical desktop client for synchronizing local filesystems with cloud object stores

## Usage

```
pip install quiltsync
quiltsync
```

## Running from Git

```
git clone https://github.com/quiltdata/quiltsync.git
cd quiltsync
poetry install # OR: 'poetry update'
DEBUG=1 poetry run quiltsync/main.py # enable hot-reload
poetry run quiltsync # run CLI
```

## Development

```
poetry env use python
poetry run pytest
poetry run ptw
```

## Releases
Be sure you to first set your [API token](https://pypi.org/manage/account/) using `poetry config pypi-token.pypi <pypi-api-token>`

```
poetry update
poetry version patch
poetry build && poetry publish
poetry version prepatch
```

# Implementation

## Kivy

Uses the [Kivy UI framework](https://kivy.org/doc/stable/html) for cross-platform Python applications.
Specifically, the [KivyMD Material Design toolkit](https://kivymd.readthedocs.io) for Kivy.

## Poetry

Use `[poetry](https://python-poetry.org/docs/)` to manage both dependencies and the virtual environment:

### Installing Poetry

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# WINDOWS: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```
