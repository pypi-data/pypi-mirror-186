# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['gino_starlette']
install_requires = \
['gino>=1.0,<2.0', 'starlette>=0.19,<1.0']

entry_points = \
{'gino.extensions': ['starlette = gino_starlette']}

setup_kwargs = {
    'name': 'gino-starlette',
    'version': '0.1.6',
    'description': 'An extension for GINO to integrate with Starlette',
    'long_description': "# gino-starlette\n\n[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0bec53f18d3b49aea6f558a269df318a)](https://app.codacy.com/gh/python-gino/gino-starlette?utm_source=github.com&utm_medium=referral&utm_content=python-gino/gino-starlette&utm_campaign=Badge_Grade_Settings)\n\n## Introduction\n\nAn extension for GINO to support starlette server.\n\n## Usage\n\nThe common usage looks like this:\n\n```python\nfrom starlette.applications import Starlette\nfrom gino.ext.starlette import Gino\n\napp = Starlette()\ndb = Gino(app, **kwargs)\n```\n\n## Configuration\n\nGINO adds a middleware to the Starlette app to setup and cleanup database according to\nthe configurations that passed in the `kwargs` parameter.\n\nThe config includes:\n\n| Name                         | Description                                                                                                       | Default     |\n| ---------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |\n| `driver`                     | the database driver                                                                                               | `asyncpg`   |\n| `host`                       | database server host                                                                                              | `localhost` |\n| `port`                       | database server port                                                                                              | `5432`      |\n| `user`                       | database server user                                                                                              | `postgres`  |\n| `password`                   | database server password                                                                                          | empty       |\n| `database`                   | database name                                                                                                     | `postgres`  |\n| `dsn`                        | a SQLAlchemy database URL to create the engine, its existence will replace all previous connect arguments.        | N/A         |\n| `retry_times`                | the retry times when database failed to connect                                                                   | `20`        |\n| `retry_interval`             | the interval in **seconds** between each time of retry                                                            | `5`         |\n| `pool_min_size`              | the initial number of connections of the db pool.                                                                 | N/A         |\n| `pool_max_size`              | the maximum number of connections in the db pool.                                                                 | N/A         |\n| `echo`                       | enable SQLAlchemy echo mode.                                                                                      | N/A         |\n| `ssl`                        | SSL context passed to `asyncpg.connect`                                                                           | `None`      |\n| `use_connection_for_request` | flag to set up lazy connection for requests.                                                                      | N/A         |\n| `retry_limit`                | the number of retries to connect to the database on start up.                                                     | 1           |\n| `retry_interval`             | seconds to wait between retries.                                                                                  | 1           |\n| `kwargs`                     | other parameters passed to the specified dialects, like `asyncpg`. Unrecognized parameters will cause exceptions. | N/A         |\n\n## Lazy Connection\n\nIf `use_connection_for_request` is set to be True, then a lazy connection is available\nat `request['connection']`. By default, a database connection is borrowed on the first\nquery, shared in the same execution context, and returned to the pool on response.\nIf you need to release the connection early in the middle to do some long-running tasks,\nyou can simply do this:\n\n```python\nawait request['connection'].release(permanent=False)\n```\n",
    'author': 'Tony Wang',
    'author_email': 'wwwjfy@gmail.com',
    'maintainer': 'Aobo Shi',
    'maintainer_email': 'shiaobo8@gmail.com',
    'url': 'https://github.com/python-gino/gino-starlette',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
