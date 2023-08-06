# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['target_postgres',
 'target_postgres.tests',
 'target_postgres.tests.samples',
 'target_postgres.tests.samples.aapl',
 'target_postgres.tests.samples.sample_tap_countries']

package_data = \
{'': ['*'],
 'target_postgres.tests': ['data_files/*'],
 'target_postgres.tests.samples.sample_tap_countries': ['schemas/*']}

install_requires = \
['psycopg2-binary==2.9.5',
 'requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.17.0,<0.18.0']

entry_points = \
{'console_scripts': ['target-postgres = '
                     'target_postgres.target:TargetPostgres.cli']}

setup_kwargs = {
    'name': 'meltanolabs-target-postgres',
    'version': '0.0.1',
    'description': '`target-postgres` is a Singer target for Postgres, built with the Meltano SDK for Singer Targets.',
    'long_description': 'None',
    'author': 'Meltano',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.12',
}


setup(**setup_kwargs)
