# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dj_currencies',
 'dj_currencies.management',
 'dj_currencies.management.commands',
 'dj_currencies.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2,<5.0', 'psycopg2-binary>=2.7,<4.0']

setup_kwargs = {
    'name': 'dj-currencies',
    'version': '1.1.0',
    'description': 'A reusable Django app that integrates https://openexchangerates.org/',
    'long_description': 'Documentation\n-------------\n\nThe full documentation is at https://dj-currencies.readthedocs.io.\n\nQuickstart\n----------\n\nFor Django 2 support, please use version 0.1.2.\nDjango 3 support added in version 1.0.\nDjango 4 support from version >=1.1.\n\nInstall djcurrencies::\n\n    pip install dj-currencies\n\nAdd it to your `INSTALLED_APPS`:\n\n.. code-block:: python\n\n    INSTALLED_APPS = (\n        ...\n        \'dj_currencies\',\n        ...\n    )\n\nSettings\n========\n\n\n.. code-block:: python\n\n    DJANGO_CURRENCIES = {\n        \'DEFAULT_BACKEND\': \'djmoney_rates.backends.OpenExchangeBackend\',\n        \'OPENEXCHANGE_APP_ID\': \'\',\n        \'BASE_CURRENCIES\': [\'USD\'],\n        \'MAX_CACHE_DAYS\': 7\n    }\n\n**DEFAULT_BACKEND**: The selected backend to sync exchange rates\n\n**OPENEXCHANGE_APP_ID**: Must be configured if you use **OpenExchangeBackend**\n\n**BASE_CURRENCIES**: A list of base currencies to use. At the time of this version, you will only be able to convert currency from any one of the base currency to target currency.\n\n**MAX_CACHE_DAYS**: Only use the cache within this time limit. If exchange rates was not synced within the time frame, an exception will thrown\n\n.. NOTE::\n   You will need to have at least "OPENEXCHANGE_APP_ID" configured if you use **OpenExchangeBackend**\n\n\n\nFeatures\n--------\n\n* [open exchange rates](openexchangerates.org) integration\n* Extensible backend design, hook your own exchange rate sources\n* Multi base currencies support, no double conversion to lose precision\n* Store historical exchange rates\n* offline currency conversion\n\nRunning Tests\n-------------\n\nDoes the code actually work?\n\n::\n\n    source <YOURVIRTUALENV>/bin/activate\n    (myenv) $ python runtests.py\n',
    'author': 'Lihan',
    'author_email': 'lihan@covergenius.com',
    'maintainer': 'Lihan Li',
    'maintainer_email': 'lihan@covergenius.com',
    'url': 'https://github.com/CoverGenius/dj-currencies',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
