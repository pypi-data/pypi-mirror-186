# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['topicwizard',
 'topicwizard.blueprints',
 'topicwizard.components',
 'topicwizard.components.documents',
 'topicwizard.components.topics',
 'topicwizard.components.words',
 'topicwizard.plots',
 'topicwizard.prepare']

package_data = \
{'': ['*']}

install_requires = \
['dash-extensions>=0.1.10,<0.2.0',
 'dash-iconify>=0.1.2,<0.2.0',
 'dash-mantine-components>=0.11.1,<0.12.0',
 'dash>=2.7.1,<3.0.0',
 'joblib>=1.2.0,<2.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'wordcloud>=1.8.2.2,<2.0.0.0']

setup_kwargs = {
    'name': 'topic-wizard',
    'version': '0.1.0',
    'description': 'Pretty and opinionated topic model visualization in Python.',
    'long_description': '# topic-wizard\nPowerful topic model visualization in Python\n',
    'author': 'Márton Kardos',
    'author_email': 'power.up1163@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.8,<4.0.0',
}


setup(**setup_kwargs)
