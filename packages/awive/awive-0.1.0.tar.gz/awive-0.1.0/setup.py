# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awive', 'awive.algorithms']

package_data = \
{'': ['*']}

install_requires = \
['autopep8>=2.0.0,<3.0.0',
 'bandit>=1.7.4,<2.0.0',
 'flake8>=5.0.4,<6.0.0',
 'isort>=5.10.1,<6.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'mypy>=0.982,<0.983',
 'opencv-python>=4.6.0.66,<5.0.0.0',
 'pandas>=1.5.1,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pydocstyle>=6.1.1,<7.0.0',
 'requests>=2.28.1,<3.0.0',
 'types-requests>=2.28.11.5,<3.0.0.0',
 'wget>=3.2,<4.0']

setup_kwargs = {
    'name': 'awive',
    'version': '0.1.0',
    'description': "Joseph Pena's bachelor thesis work",
    'long_description': '# AWIVE\nAWIVE, the acrynomes of Adaptive Water Image Velocimetry Estimator, is a\nsoftware package for the estimation of the velocity field from a sequence of\nimages. It is composed by the methods STIV and OTV, which aim at estimate\nvelocimetry with a low computational cost.\n\n## Installing\n\nInstall and update using pip:\n\n```bash\npip install awive\n```\n\n',
    'author': 'Joseph P.',
    'author_email': 'joseph.pena@utec.edu.pe',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.9.16',
}


setup(**setup_kwargs)
