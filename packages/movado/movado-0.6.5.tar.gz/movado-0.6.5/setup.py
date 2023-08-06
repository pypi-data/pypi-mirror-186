# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['movado']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.0,<2.0',
 'numpy>=1.19,<2.0',
 'plotly>=4.14,<5.0',
 'river==0.14',
 'scikit-learn>=0.24,<0.25',
 'scipy>=1.5,<2.0',
 'vowpalwabbit>=8,<9']

setup_kwargs = {
    'name': 'movado',
    'version': '0.6.5',
    'description': 'Approximation utility for expensive fitness functions',
    'long_description': 'None',
    'author': 'Daniele Paletti',
    'author_email': 'danielepaletti98@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
