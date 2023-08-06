# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['live_debugger']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'live-debugger',
    'version': '0.1.0',
    'description': 'A simple library for CPython that allows you to collect stacktrace data from running processes in production environments without stopping the execution of the process.',
    'long_description': 'Live Debugger\n=============\n\nOverview\n********\n\nLive Debugger is a library for CPython that allows to collect stacktrace data from running\nprocesses in production environments without stopping the world. The library provides\nsafe building blocks and concepts for developers to collect stack snapshot from\nprocesses. It is designed to be minimal and extensible. It also makes no assumptions\non what the process plans to do with the collected data, focusing only on providing immutable\nsafe data.\n\nThe debugger implementation uses CPython debugging functions available in the standard\nlibrary to intercept function call and collect stack frames data. Stackframes are transformed\ninto immutable data structures so no harm can be done to the running process.\n\nThe main benefits of using this library are:\n\n* Free (as in freedom)\n* Depends only on CPython standard libraries\n* Easy to extend\n* Easy to use\n* Small codebase\n\n\nInstallation\n************\n\nThis library is available in `PyPI <https://pypi.org/>`_ so you can install it as a normal Python package:\n\n.. code-block:: bash\n\n   pip install live-debugger\n\n\nUsage\n*****\n\n.. code-block:: python\n   \n   >>> from live_debugger import api\n   >>> cookie = api.add_point("flask_example/app.py", 33, print)\n   >>> api.clear_point(cookie)\n\n\nNext\n****\n\n* Async support\n* Anonymization\n\n\nCredits\n*******\n\n* Yunier Rojas García\n* ChatGPT -- for helping me writing this README\n\n\nLicense\n*******\nAGPL v3\n',
    'author': 'Yunier Rojas García',
    'author_email': 'yunier.rojas@gmail.com',
    'maintainer': 'Yunier Rojas García',
    'maintainer_email': 'yunier.rojas@gmail.com',
    'url': 'https://gitlab.com/yunier.rojas/python-live-debugger',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
