# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flet',
 'flet.__pyinstaller',
 'flet.__pyinstaller.rthooks',
 'flet.auth',
 'flet.auth.providers',
 'flet.cli',
 'flet.cli.commands']

package_data = \
{'': ['*']}

install_requires = \
['flet-core==0.4.0.dev1058',
 'httpx>=0.23.3,<0.24.0',
 'oauthlib>=3.2.2,<4.0.0',
 'packaging>=23.0,<24.0',
 'watchdog>=2.2.1,<3.0.0',
 'websocket-client>=1.4.2,<2.0.0',
 'websockets>=10.4,<11.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.4.0,<5.0.0']}

entry_points = \
{'console_scripts': ['flet = flet.cli.cli:main'],
 'pyinstaller40': ['hook-dirs = flet.__pyinstaller:get_hook_dirs']}

setup_kwargs = {
    'name': 'flet',
    'version': '0.4.0.dev1058',
    'description': 'Flet for Python - easily build interactive multi-platform apps in Python',
    'long_description': '# Flet - quickly build interactive apps for web, desktop and mobile in Python\n\n[Flet](https://flet.dev) is a rich User Interface (UI) framework to quickly build interactive web, desktop and mobile apps in Python without prior knowledge of web technologies like HTTP, HTML, CSS or JavaSscript. You build UI with [controls](https://flet.dev/docs/controls) based on [Flutter](https://flutter.dev/) widgets to ensure your programs look cool and professional.\n\n## Requirements\n\n* Python 3.7 or above on Windows, Linux or macOS\n\n## Installation\n\n```\npip install flet\n```\n\n## Hello, world!\n\n```python\nimport flet\nfrom flet import Page, Text\n\ndef main(page: Page):\n    page.add(Text("Hello, world!"))\n\nflet.app(target=main)\n```\n\nRun the sample above and the app will be started in a native OS window:\n\n![Sample app in a browser](https://flet.dev//img/docs/getting-started/flet-counter-macos.png "Sample app in a native window")\n\nContinue with [Python guide](https://flet.dev/docs/getting-started/python) to learn how to make a real app.\n\nBrowse for more [Flet examples](https://github.com/flet-dev/examples/tree/main/python).\n\nJoin to a conversation on [Flet Discord server](https://discord.gg/dzWXP8SHG8).\n',
    'author': 'Appveyor Systems Inc.',
    'author_email': 'hello@flet.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
