# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mindsdb_evaluator',
 'mindsdb_evaluator.accuracy',
 'mindsdb_evaluator.calibration']

package_data = \
{'': ['*']}

install_requires = \
['dataprep-ml>=0.0.8,<0.0.9',
 'numpy>=1,<2',
 'pandas>=1,<2',
 'scikit-learn>=1.0.0,<=1.0.2',
 'type-infer>=0.0.9,<0.0.10']

setup_kwargs = {
    'name': 'mindsdb-evaluator',
    'version': '0.0.6',
    'description': 'Model evaluation for Machine Learning pipelines.',
    'long_description': '# mindsdb_evaluator\n\nModel evaluation for Machine Learning pipelines.',
    'author': 'MindsDB Inc.',
    'author_email': 'hello@mindsdb.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
