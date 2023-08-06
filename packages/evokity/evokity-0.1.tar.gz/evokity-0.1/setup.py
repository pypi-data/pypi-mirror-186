# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['evokity']

package_data = \
{'': ['*']}

install_requires = \
['eckity>=0.2.3,<0.3.0']

setup_kwargs = {
    'name': 'evokity',
    'version': '0.1',
    'description': '',
    'long_description': '# Evokity\n\n<p align="center">\nCollection of essential <a href=https://github.com/EC-KitY/EC-KitY> Evolutionary Computaion Kit</a> utilities.\n</p>\n\n<p align="center">\n  <img src="https://img.shields.io/github/actions/workflow/status/amitkummer/evolutionary-mini-project/integration.yaml?label=Tests%2C%20Linting%20%26%20Formatting&style=for-the-badge">\n</p>\n\n## Development\n\nRequires `poetry` installed (tested with `v1.2.2`).\n\nInstall the dependencies:\n\n```sh\npoetry install\n```\n\nSpawn a shell within the project\'s environment:\n\n```\npoetry shell\n```\n\n\n## Unit Tests\n\nTo run the unit-tests, use:\n\n```\npytest\npytest -s // To show captured stdout.\n```\n\n\n## Formatting\n\nTo run formatting, use:\n\n```\nblack evokity tests\n```\n\n',
    'author': 'amitkummer',
    'author_email': 'amit.kummer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
