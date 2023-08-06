# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yandex_geocoder']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'yandex-geocoder',
    'version': '3.0.1',
    'description': 'Simple library for getting address or coordinates via Yandex geocoder',
    'long_description': '# Yandex Geocoder\n\nGet address coordinates via Yandex geocoder\n\n[![test](https://github.com/sivakov512/yandex-geocoder/workflows/test/badge.svg)](https://github.com/sivakov512/yandex-geocoder/actions?query=workflow%3Atest)\n[![Coverage Status](https://coveralls.io/repos/github/sivakov512/yandex-geocoder/badge.svg?branch=master)](https://coveralls.io/github/sivakov512/yandex-geocoder?branch=master)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![Python versions](https://img.shields.io/pypi/pyversions/yandex-geocoder.svg)](https://pypi.python.org/pypi/yandex-geocoder)\n[![PyPi](https://img.shields.io/pypi/v/yandex-geocoder.svg)](https://pypi.python.org/pypi/yandex-geocoder)\n\n## Installation\n\nInstall it via `pip` tool:\n\n```shell\npip install yandex-geocoder\n```\n\nor Poetry:\n\n```shell\npoetry add yandex-geocoder\n```\n\n## Usage example\n\nYandex Geocoder requires an API developer key, you can get it [here](https://developer.tech.yandex.ru/services/) to use this library.\n\n```python\nfrom decimal import Decimal\n\nfrom yandex_geocoder import Client\n\n\nclient = Client("your-api-key")\n\ncoordinates = client.coordinates("Москва Льва Толстого 16")\nassert coordinates == (Decimal("37.587093"), Decimal("55.733969"))\n\naddress = client.address(Decimal("37.587093"), Decimal("55.733969"))\nassert address == "Россия, Москва, улица Льва Толстого, 16"\n```\n\n## Development and contribution\n\nFirst of all you should install [Poetry](https://python-poetry.org).\n\n- install project dependencies\n\n```bash\nmake install\n```\n\n- run linters\n\n```bash\nmake lint\n```\n\n- run tests\n\n```bash\nmake test\n```\n\n- feel free to contribute!\n',
    'author': 'Nikita Sivakov',
    'author_email': 'sivakov512@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sivakov512/yandex-geocoder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
