# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polaris',
 'polaris.collectstatic',
 'polaris.integrations',
 'polaris.locale',
 'polaris.management',
 'polaris.management.commands',
 'polaris.migrations',
 'polaris.sep1',
 'polaris.sep10',
 'polaris.sep12',
 'polaris.sep24',
 'polaris.sep31',
 'polaris.sep38',
 'polaris.sep6',
 'polaris.shared',
 'polaris.templates']

package_data = \
{'': ['*'],
 'polaris': ['static/polaris/base.css',
             'static/polaris/base.css',
             'static/polaris/base.css',
             'static/polaris/chevron-down.svg',
             'static/polaris/chevron-down.svg',
             'static/polaris/chevron-down.svg',
             'static/polaris/company-icon.svg',
             'static/polaris/company-icon.svg',
             'static/polaris/company-icon.svg',
             'static/polaris/scripts/*'],
 'polaris.locale': ['id/LC_MESSAGES/*', 'pt/LC_MESSAGES/*'],
 'polaris.templates': ['django/forms/widgets/*',
                       'polaris/*',
                       'polaris/widgets/*']}

install_requires = \
['aiohttp>=3.7,<4.0',
 'asgiref>=3.2,<4.0',
 'cryptography>=3.4,<4.0',
 'django-cors-headers>=3.7,<4.0',
 'django-environ',
 'django-model-utils>=4.1,<5.0',
 'django>=3.2,<4.0',
 'djangorestframework>=3.12,<4.0',
 'pyjwt>=2.1,<3.0',
 'sqlparse>=0.4.2,<0.5.0',
 'stellar-sdk>=8.0,<9.0',
 'toml',
 'whitenoise>=5.3,<6.0']

extras_require = \
{'dev-server': ['gunicorn', 'psycopg2-binary>=2.9,<3.0', 'watchdog>=2,<3'],
 'docs': ['readthedocs-sphinx-ext>=2.1,<3.0',
          'sphinx>=4.2,<5.0',
          'sphinx-rtd-theme>=1.0,<2.0',
          'sphinx-autodoc-typehints']}

setup_kwargs = {
    'name': 'django-polaris',
    'version': '2.3.6',
    'description': 'An extendable Django server for Stellar Ecosystem Proposals.',
    'long_description': "==============\nDjango Polaris\n==============\n\n.. image:: https://circleci.com/gh/stellar/django-polaris.svg?style=shield\n    :target: https://circleci.com/gh/stellar/django-polaris\n\n.. image:: https://codecov.io/gh/stellar/django-polaris/branch/master/graph/badge.svg?token=3DaW3jM6Q8\n    :target: https://codecov.io/gh/stellar/django-polaris\n\n.. image:: https://img.shields.io/badge/python-3.7%20%7C%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue?style=shield\n    :alt: Python - Version\n    :target: https://pypi.python.org/pypi/django-polaris\n\n.. _`email list`: https://groups.google.com/g/stellar-polaris\n.. _Stellar Development Foundation: https://www.stellar.org/\n.. _github: https://github.com/stellar/django-polaris\n.. _django app: https://docs.djangoproject.com/en/3.0/intro/reusable-apps/\n.. _`demo wallet`: http://demo-wallet.stellar.org\n.. _`reference server`: https://testanchor.stellar.org/.well-known/stellar.toml\n.. _`documentation`: https://django-polaris.readthedocs.io/\n\nPolaris is an extendable `django app`_ for Stellar Ecosystem Proposal (SEP) implementations maintained by the `Stellar Development Foundation`_ (SDF). Using Polaris, you can run a web server supporting any combination of SEP-1, 6, 10, 12, 24, 31, & 38.\n\nSee the complete `documentation`_ for information on how to get started with Polaris. The SDF also runs a `reference server`_ using Polaris that can be tested using our `demo wallet`_.\n\nFor important updates on Polaris's development and releases, please join the `email list`_.\n",
    'author': 'Stellar Development Foundation',
    'author_email': 'jake@stellar.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stellar/django-polaris',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
