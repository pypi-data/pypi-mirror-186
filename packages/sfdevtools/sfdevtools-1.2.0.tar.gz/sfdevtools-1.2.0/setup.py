# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sfdevtools',
 'sfdevtools.app',
 'sfdevtools.devTools',
 'sfdevtools.observability',
 'sfdevtools.observability.PyLogstash']

package_data = \
{'': ['*']}

install_requires = \
['logging-json>=0.2.1,<0.3.0']

setup_kwargs = {
    'name': 'sfdevtools',
    'version': '1.2.0',
    'description': '',
    'long_description': '## How to publish to pypi\n```bash\n# set up pypi token\npoetry config pypi-token.pypi my-token\n\n# build the project\npoetry build\n\n# publish the project\npoetry publish\n\n# DONE\n```\n',
    'author': 'SulfredLee',
    'author_email': 'sflee1112@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
