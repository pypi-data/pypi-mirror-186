# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quart_events']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-multisubscriber-queue', 'quart']

entry_points = \
{'console_scripts': ['pytest = pytest:main'],
 'pytest11': ['quart_events = quart_events.pytest_plugin']}

setup_kwargs = {
    'name': 'quart-events',
    'version': '0.4.3',
    'description': 'aquart extension to facilitate event message brokering',
    'long_description': "#  quart-events\n\n[![PyPI version](https://img.shields.io/pypi/v/quart-events)](https://pypi.org/project/quart-events/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/quart-events)](https://pypi.org/project/quart-events/)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![](https://github.com/smithk86/quart-events/workflows/pytest/badge.svg)](https://github.com/smithk86/quart-events/actions?query=workflow%3Apytest)\n\n## Usage\n\nquart_events.EventBroker loads a blueprint into Quart which allows clients to subscribe to events via a WebSockets. The app can then generate events that can be sent to all subscribed clients in real-time.\n\nPlease see [test/app.py](https://github.com/smithk86/quart-events/blob/main/test/testapp/) for an example app. This app is used when running testing via py.test but can also be run standalone.\n\n## Change Log\n\n### [0.4.2] - 2021-12-23\n\n- Change build system from setuptools to poetry\n\n### [0.4.0] - 2021-11-08\n\n- add type hints and type validation with mypy\n- requires asyncio-multisubscriber-queue 0.3.0\n- pytest plugin to facilitate capturing events while other tests are running; plugin name is *quart_events_catcher*\n- added optional callbacks\n- websocket auth improvements\n    - token is now seemlessly managed using the user's session data\n    - token has an expiration; user is disconnected from the socket upon expiration\n    - a callback is available to further validate user using other criteria (like Flask-Login)\n",
    'author': 'Kyle Smith',
    'author_email': 'smithk86@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/smithk86/quart-events',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
