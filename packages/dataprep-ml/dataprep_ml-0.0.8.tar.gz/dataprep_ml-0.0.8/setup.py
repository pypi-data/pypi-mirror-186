# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataprep_ml']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=6.5.0,<7.0.0',
 'dataclasses-json>=0.5.4,<0.6.0',
 'numpy>=1,<2',
 'pandas>=1,<2',
 'pydateinfer==0.3.0',
 'python-dateutil>=2.1',
 'scipy>=1.5.4',
 'type-infer>=0.0.7']

setup_kwargs = {
    'name': 'dataprep-ml',
    'version': '0.0.8',
    'description': 'Automated dataframe analysis for Machine Learning pipelines.',
    'long_description': '# dataprep_ml\nData utilities for Machine Learning pipelines.\n\n\n## Submodules\n\n1. Data cleaning\n2. Data analysis\n3. Data splitting\n',
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
