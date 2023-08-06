# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['carrier_services', 'carrier_services.utils']

package_data = \
{'': ['*'], 'carrier_services': ['resources/*']}

install_requires = \
['atlassian-python-api>=3.32.2,<4.0.0',
 'bs4>=0.0.1,<0.0.2',
 'lxml>=4.9.2,<5.0.0',
 'pandas>=1.5.2,<2.0.0',
 'selenium>=4.7.2,<5.0.0',
 'tomli>=2.0.1,<3.0.0',
 'webdriver-manager>=3.8.5,<4.0.0']

setup_kwargs = {
    'name': 'carrier-services',
    'version': '0.1.0',
    'description': 'Get carrier services from shipping lines.',
    'long_description': '# carrier-services\nGet carrier services from shipping lines.\n\n## Installation\nFrom [PyPI](https://pypi.org/project/carrier-services/):\n\n    python -m pip install carrier-services\n\n## Setup\nThe following setup must be done before running:\n1. Install Google Chrome. Chrome version 109 or newer is required.\n2. Create below environment variables in your OS environment:\n    * `CS_SMTP_HOST`: SMTP host for sending notification emails\n    * `CS_CONFLUENCE_TOKEN`: Token for uploading carrier service master to Wiki\n<br/><br/>\n3. Update below directory paths in `site-packages/carrier_services/utils/config.toml` for directory location of data files and log files. For example:\n    ```\n    [environment]\n    directory.data = ""    # /home/user1/carrier_services/data"\n    directory.log = ""     # /home/user1/carrier_services/log"\n    ```\n    If left empty, <user_home>/carrier_services/data & <user_home>/carrier_services/log will be used: \n\n## How to Use\ncarrier-services is a console application, named `carrier_services`.\n\n    >>> python -m carrier_services\n',
    'author': 'Alex Cheng',
    'author_email': 'alex28.biz@gmail.com',
    'maintainer': 'Alex Cheng',
    'maintainer_email': 'alex28.biz@gmail.com',
    'url': 'https://github.com/alexcheng628/carrier-services',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
