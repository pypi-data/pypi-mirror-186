# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webint_jobs', 'webint_jobs.templates']

package_data = \
{'': ['*']}

modules = \
['bgq']
install_requires = \
['gevent>=22.10.2,<23.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'sqlyte>=0.0.50',
 'txtint>=0.0.68',
 'webcli>=0.0.5',
 'webint>=0.0.569']

entry_points = \
{'console_scripts': ['bgq = bgq:main'], 'webapps': ['jobs = webint_jobs:app']}

setup_kwargs = {
    'name': 'bgq',
    'version': '0.1.0',
    'description': 'a simple asynchronous background job queue',
    'long_description': 'None',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ragt.ag/code/projects/bgq',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
