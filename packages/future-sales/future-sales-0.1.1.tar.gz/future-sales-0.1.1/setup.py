# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['future_sales', 'future_sales.data']

package_data = \
{'': ['*']}

install_requires = \
['category-encoders>=2.5.1,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'hyperopt>=0.2.7,<0.3.0',
 'pandas>=1.5.2,<2.0.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'xgboost>=1.7.2,<2.0.0']

entry_points = \
{'console_scripts': ['predict = future_sales.predict:predict',
                     'train = future_sales.train:train']}

setup_kwargs = {
    'name': 'future-sales',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Sabina Bayramova',
    'author_email': 'sb.sabina00@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
