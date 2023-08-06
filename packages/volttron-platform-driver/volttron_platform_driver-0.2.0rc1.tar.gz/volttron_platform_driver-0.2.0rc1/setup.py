# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['platform_driver']

package_data = \
{'': ['*']}

install_requires = \
['volttron-lib-base-driver>=0.2.0rc0,<0.3.0']

entry_points = \
{'console_scripts': ['volttron-platform-driver = platform_driver.agent:main']}

setup_kwargs = {
    'name': 'volttron-platform-driver',
    'version': '0.2.0rc1',
    'description': 'The Platform Driver agent is a special purpose agent that manages communication between the Volttron platform and devices. The Platform driver features a number of endpoints for collecting data and sending control signals using the message bus and automatically publishes data to the bus on a specified interval.',
    'long_description': '# Platform Driver Agent\n\n![Passing?](https://github.com/eclipse-volttron/volttron-platform-driver/actions/workflows/run-tests.yml/badge.svg)\n[![pypi version](https://img.shields.io/pypi/v/volttron-platform-driver.svg)](https://pypi.org/project/volttron-platform-driver/)\n\n\nThe Platform Driver agent is a special purpose agent a user can install on the platform to manage communication of the platform with devices. The Platform driver features a number of endpoints for collecting data and sending control signals using the message bus and automatically publishes data to the bus on a specified interval.\n\n# Prerequisites\n\n* Python 3.8\n\n## Python\n\n<details>\n<summary>To install Python 3.8, we recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.8\npyenv install 3.8.10\n\n# make it available globally\npyenv global system 3.8.10\n```\n</details>\n\n# Installation\n\n  1. Create and activate a virtual environment.\n\n     ```shell\n     python -m venv env\n     source env/bin/activate\n     ```\n\n  2. Installing volttron-platform-driver requires a running volttron instance.\n\n     ```shell\n     pip install volttron\n     ```    \n     Start platform with output going to volttron.log\n     ```shell\n     volttron -vv -l volttron.log &\n     ```\n\n  3. Install and start the volttron-platform-driver.\n\n     ```shell\n     vctl install volttron-platform-driver --vip-identity platform.driver --start\n     ```\n     #### Note:\n      In the above command, if no --vip-identity is not provided the default value would be "platform.driver". This comes  \n      from the file volttron-platform-driver-<version>-default-vip-id that is at the top level of this agent repository. The \n      pyproject.toml file in this repository is configured to include this file(volttron-platform-driver-<version>-default-vip-id) \n      as part of agent wheel. \n\n\n  4. View the status of the installed agent\n    \n     ```shell\n     vctl status\n     ```\n\n# Development\n\nPlease see the following for contributing guidelines [contributing](https://github.com/eclipse-volttron/volttron-core/blob/develop/CONTRIBUTING.md).\n\nPlease see the following helpful guide about [developing modular VOLTTRON agents](https://github.com/eclipse-volttron/volttron-core/blob/develop/DEVELOPING_ON_MODULAR.md)\n\n\n# Disclaimer Notice\n\nThis material was prepared as an account of work sponsored by an agency of the\nUnited States Government.  Neither the United States Government nor the United\nStates Department of Energy, nor Battelle, nor any of their employees, nor any\njurisdiction or organization that has cooperated in the development of these\nmaterials, makes any warranty, express or implied, or assumes any legal\nliability or responsibility for the accuracy, completeness, or usefulness or any\ninformation, apparatus, product, software, or process disclosed, or represents\nthat its use would not infringe privately owned rights.\n\nReference herein to any specific commercial product, process, or service by\ntrade name, trademark, manufacturer, or otherwise does not necessarily\nconstitute or imply its endorsement, recommendation, or favoring by the United\nStates Government or any agency thereof, or Battelle Memorial Institute. The\nviews and opinions of authors expressed herein do not necessarily state or\nreflect those of the United States Government or any agency thereof.\n',
    'author': 'VOLTTRON Team',
    'author_email': 'volttron@pnnl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eclipse-volttron/platform-driver-agent',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
