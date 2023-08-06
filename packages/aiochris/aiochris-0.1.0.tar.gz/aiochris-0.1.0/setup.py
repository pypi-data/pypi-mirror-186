# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chris', 'chris.client', 'chris.link', 'chris.models', 'chris.util']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=22.1.0,<23.0.0',
 'aiohttp>=3.8.3,<4.0.0',
 'async-property>=0.2.1,<0.3.0',
 'pyserde==0.8.3',
 'yarl>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'aiochris',
    'version': '0.1.0',
    'description': 'ChRIS client built on aiohttp',
    'long_description': '# aiochris\n\n[![Tests](https://github.com/FNNDSC/aiochris/actions/workflows/test.yml/badge.svg)](https://github.com/FNNDSC/aiochris/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/FNNDSC/aiochris/branch/master/graph/badge.svg?token=48EEYZ3PUU)](https://codecov.io/gh/FNNDSC/aiochris)\n[![PyPI](https://img.shields.io/pypi/v/aiochris)](https://pypi.org/project/aiochris/)\n[![License - MIT](https://img.shields.io/pypi/l/aiochris)](https://github.com/FNNDSC/aiochris/blob/master/LICENSE)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n[_ChRIS_](https://chrisproject.org) Python client library built on\n[aiohttp](https://github.com/aio-libs/aiohttp) (async HTTP client) and\n[pyserde](https://github.com/yukinarit/pyserde)\n([dataclasses](https://docs.python.org/3/library/dataclasses.html) deserializer).\n\n## Installation\n\nRequires Python 3.10 or 3.11.\n\n```shell\npip install aiochris\n# or\npoetry add aiochris\n```\n\n## Quick Example\n\n```python\nimport asyncio\nfrom chris import ChrisClient\n\n\nasync def readme_example():\n    chris = await ChrisClient.from_login(\n        username=\'chris\',\n        password=\'chris1234\',\n        url=\'https://cube.chrisproject.org/api/v1/\'\n    )\n    dircopy = await chris.search_plugins(name_exact=\'pl-brainmgz\', version=\'2.0.3\').get_only()\n    plinst = await dircopy.create_instance(compute_resource_name=\'host\')\n    feed = await plinst.get_feed()\n    await feed.set(name="hello, aiochris!")\n    await chris.close()  # do not forget to clean up!\n\n\nasyncio.run(readme_example())\n```\n\n## Documentation Links\n\n- Client documentation: https://fnndsc.github.io/aiochris\n- Developer documentation: https://github.com/FNNDSC/aiochris/wiki\n',
    'author': 'FNNDSC',
    'author_email': 'dev@babyMRI.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
