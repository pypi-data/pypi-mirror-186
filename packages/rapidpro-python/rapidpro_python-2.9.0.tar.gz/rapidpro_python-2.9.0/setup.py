# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['temba_client', 'temba_client.v2']

package_data = \
{'': ['*']}

install_requires = \
['iso8601>=0.1.13,<0.2.0', 'pytz', 'requests>=2.25.0,<3.0.0']

setup_kwargs = {
    'name': 'rapidpro-python',
    'version': '2.9.0',
    'description': 'Python client library for the RapidPro API',
    'long_description': "RapidPro Python Client\n======================\n\n[![Build Status](https://github.com/rapidpro/rapidpro-python/workflows/CI/badge.svg)](https://github.com/rapidpro/rapidpro-python/actions?query=workflow%3ACI)\n[![Coverage Status](https://codecov.io/gh/rapidpro/rapidpro-python/branch/main/graph/badge.svg)](https://codecov.io/gh/rapidpro/rapidpro-python) \n[![PyPI Release](https://img.shields.io/pypi/v/rapidpro-python.svg)](https://pypi.python.org/pypi/rapidpro-python/)\n\nOfficial Python client library for the [RapidPro](http://rapidpro.github.io/rapidpro/). Supports latest Python 3.\n\nVisit [here](http://rapidpro-python.readthedocs.org/) for complete documentation.\n\nInstallation\n------------\n\n```\npip install rapidpro-python\n```\n\nExample\n-------\n\n```python\nfrom temba_client.v2 import TembaClient\nclient = TembaClient('rapidpro.io', 'your-api-token')\nfor contact_batch in client.get_contacts(group='Reporters').iterfetches(retry_on_rate_exceed=True):\n    for contact in contact_batch:\n        print(contact.name)\n```\n\nIf you don't know your API token then visit the [API Explorer](http://rapidpro.io/api/v2/explorer)\n\nDevelopment\n-----------\n\nFor discussions about future development, see the [RapidPro Developers Group](https://groups.google.com/forum/#!forum/rapidpro-dev).\n\nTo run the tests:\n\n```\nnosetests --with-coverage --cover-erase --cover-package=temba_client --cover-html\n```\n",
    'author': 'Nyaruka',
    'author_email': 'code@nyaruka.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
