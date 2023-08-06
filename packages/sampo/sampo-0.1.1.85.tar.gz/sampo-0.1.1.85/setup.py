# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sampo',
 'sampo.generator',
 'sampo.generator.config',
 'sampo.generator.environment',
 'sampo.generator.pipeline',
 'sampo.generator.utils',
 'sampo.metrics',
 'sampo.metrics.resources_in_time',
 'sampo.scheduler',
 'sampo.scheduler.genetic',
 'sampo.scheduler.heft',
 'sampo.scheduler.heft_between',
 'sampo.scheduler.multi_agency',
 'sampo.scheduler.resource',
 'sampo.scheduler.timeline',
 'sampo.scheduler.topological',
 'sampo.scheduler.utils',
 'sampo.schemas',
 'sampo.structurator',
 'sampo.utilities',
 'sampo.utilities.generation',
 'sampo.utilities.sampler',
 'sampo.utilities.visualization']

package_data = \
{'': ['*']}

install_requires = \
['deap>=1.3.3,<1.4.0',
 'matplotlib>=3.6.2,<3.7.0',
 'numpy>=1.23.5,<1.24.0',
 'pandas>=1.5.2,<1.6.0',
 'pathos>=0.3.0,<0.3.1',
 'plotly>=5.11.0,<5.12.0',
 'pytest>=7.2.0,<7.3.0',
 'scipy>=1.9.3,<1.10.0',
 'seaborn>=0.12.1,<0.13.0',
 'sortedcontainers>=2.4.0,<2.5.0',
 'toposort>=1.7,<2.0']

setup_kwargs = {
    'name': 'sampo',
    'version': '0.1.1.85',
    'description': 'Open-source framework for adaptive manufacturing processes scheduling',
    'long_description': 'None',
    'author': 'iAirLab',
    'author_email': 'iairlab@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
