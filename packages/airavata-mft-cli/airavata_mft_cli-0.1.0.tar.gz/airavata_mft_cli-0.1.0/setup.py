# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airavata_mft_cli', 'airavata_mft_cli.storage']

package_data = \
{'': ['*']}

install_requires = \
['pick==2.2.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['mft = airavata_mft_cli.main:app']}

setup_kwargs = {
    'name': 'airavata-mft-cli',
    'version': '0.1.0',
    'description': 'Command Line Client for Airavata MFT data transfer framework',
    'long_description': '# Airavata MFT Command Line Client',
    'author': 'Dimuthu Wannipurage',
    'author_email': 'dimuthu.upeksha2@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
