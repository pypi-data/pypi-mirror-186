# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybravia']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp']

setup_kwargs = {
    'name': 'pybravia',
    'version': '0.3.1',
    'description': 'Python async library for remote control of Sony Bravia TVs 2013 and newer.',
    'long_description': '# pybravia\n\n<a href="https://pypi.org/project/pybravia/"><img src="https://img.shields.io/pypi/v/pybravia" alt="PyPi release"></a> <img src="https://img.shields.io/github/actions/workflow/status/Drafteed/pybravia/ci.yml?branch=master" alt="GitHub Workflow Status"> <img src="https://img.shields.io/github/license/Drafteed/pybravia" alt="MIT License"> <img src="https://img.shields.io/badge/code%20style-black-black" alt="Code style">\n\nPython Bravia provides an easy-to-use async interface for controlling of Sony Bravia TVs 2013 and newer.\n\nThis library primarily being developed with the intent of supporting [Home Assistant](https://www.home-assistant.io/integrations/braviatv/).\n\nFor more information, take a look at [BRAVIA Professional Display Knowledge Center](https://pro-bravia.sony.net/develop/).\n\n## Requirements\n\nThis library supports Python 3.8 and higher.\n\n## Installation\n\n```sh\npip install pybravia\n```\n\n## Connect and API usage\n\n### With PSK (recommended)\n\n```py\nfrom pybravia import BraviaClient, BraviaError\n\nasync with BraviaClient("192.168.1.20") as client:\n    try:\n        connected = await client.connect(psk="sony")\n\n        info = await client.get_system_info()\n\n        print(info)\n\n        await client.volume_up()\n    except BraviaError:\n        print("could not connect")\n```\n\n### With PIN code\n\n#### Start pairing process and display PIN on the TV\n\n```py\nfrom pybravia import BraviaClient, BraviaError\n\nasync with BraviaClient("192.168.1.20") as client:\n    try:\n        await client.pair("CLIENTID", "NICKNAME")\n    except BraviaError:\n        print("could not connect")\n```\n\n#### Connect and usage\n\n```py\nfrom pybravia import BraviaClient, BraviaError\n\nasync with BraviaClient("192.168.1.20") as client:\n    try:\n        connected = await client.connect("PIN", "CLIENTID", "NICKNAME")\n\n        info = await client.get_system_info()\n\n        print(info)\n\n        await client.volume_up()\n    except BraviaError:\n        print("could not connect")\n```\n\n## Contributing\n\nSee an issue? Have something to add? Issues and pull requests are accepted in this repository.\n\n## License\n\nThis project is released under the MIT License. Refer to the LICENSE file for details.\n',
    'author': 'Arem Draft',
    'author_email': 'artemon_93@mail.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Drafteed/pybravia',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
