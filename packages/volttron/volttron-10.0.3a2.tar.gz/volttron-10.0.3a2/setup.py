# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['volttron',
 'volttron.client',
 'volttron.client.commands',
 'volttron.client.messaging',
 'volttron.client.vip',
 'volttron.client.vip.agent',
 'volttron.client.vip.agent.subsystems',
 'volttron.server',
 'volttron.server.router',
 'volttron.services.auth',
 'volttron.services.config_store',
 'volttron.services.control',
 'volttron.services.health',
 'volttron.services.routing',
 'volttron.types',
 'volttron.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'cryptography>=36.0.1,<37.0.0',
 'dateutils>=0.6.12,<0.7.0',
 'gevent>=21.12.0,<22.0.0',
 'pip==22.2.2',
 'psutil>=5.9.0,<6.0.0',
 'pyzmq>=22.3.0,<23.0.0',
 'toml>=0.10.2,<0.11.0',
 'tzlocal>=4.1,<5.0',
 'watchdog-gevent>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['vcfg = volttron.client.commands.config:main',
                     'vctl = volttron.client.commands.control:main',
                     'volttron = volttron.server.__main__:main',
                     'volttron-cfg = volttron.client.commands.config:main',
                     'volttron-ctl = volttron.client.commands.control:main']}

setup_kwargs = {
    'name': 'volttron',
    'version': '10.0.3a2',
    'description': 'VOLTTRON™ is an open source platform for distributed sensing and control. The platform provides services for collecting and storing data from buildings and devices and provides an environment for developing applications which interact with that data.',
    'long_description': 'VOLTTRON™ is an open source platform for distributed sensing and control. The platform provides services for collecting and storing data from buildings and devices and provides an environment for developing applications which interact with that data.\n\n[![Pytests](https://github.com/eclipse-volttron/volttron-core/actions/workflows/run-tests.yml/badge.svg)](https://github.com/eclipse-volttron/volttron-core/actions/workflows/run-tests.yml)\n[![pypi version](https://img.shields.io/pypi/v/volttron.svg)](https://pypi.org/project/volttron/)\n\n## Installation\n\nIt is recommended to use a virtual environment for installing volttron.\n\n```shell\npython -m venv env\nsource env/bin/activate\n\npip install volttron\n```\n\n### Quick Start\n\n 1. Setup VOLTTRON_HOME environment variable: export VOLTTRON_HOME=/path/to/volttron_home/dir \n \n    **NOTE** This is madatory if you have/had in the past, a monolithic    VOLTTRON version that used the default VOLTTRON_HOME $HOME/.volttron. This modular version of VOLTTRON cannot work with volttron_home used by monolithic version of VOLTTRON(version 8.3 or earlier)\n \n 2. Start the platform\n    ```bash\n    > volttron -vv -l volttron.log &>/dev/null &\n    ```\n\n 3. Install listener agent\n    ```bash\n    > vctl install volttron-listener --start\n    ```\n\n 4. View status of platform\n    ```bash\n    > vctl status\n    ```\n\n 5. Shutdown the platform\n    ```bash\n    > vctl shutdown --platform\n    ```\n\nFull VOLTTRON documentation available at [VOLTTRON Readthedocs](https://volttron.readthedocs.io)\n\n## Contributing to VOLTTRON\n\nPlease see the [contributing.md](CONTRIBUTING.md) document before contributing to this repository.\n\nPlease see [developing_on_modular.md](DEVELOPING_ON_MODULAR.md) document for developing your agents against volttron.\n',
    'author': 'volttron',
    'author_email': 'volttron@pnnl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://volttron.org',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
