# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ink_wizard', 'ink_wizard.commands', 'ink_wizard.template_generators']

package_data = \
{'': ['*'],
 'ink_wizard': ['templates/flipper/*',
                'templates/psp22/*',
                'templates/psp34/*',
                'templates/psp37/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['ink-wizard = ink_wizard.main:main']}

setup_kwargs = {
    'name': 'ink-wizard',
    'version': '0.1.6',
    'description': 'Ink Wizard is a CLI tool used to scaffold Flipper, PSP-22, PSP-34, PSP-37 smart contracts. CLI will ask user on what kind of functionality user needs. It will scaffold smart contracts based on user options.',
    'long_description': '# Ink Wizard\n\nInk Wizard is a CLI tool used to scaffold Flipper, PSP-22, PSP-34, PSP-37 smart contracts. CLI will ask user on what kind of functionality user needs. It will scaffold smart contracts based on user options.\n\nInk Wizard uses [OpenBrush](https://openbrush.io) smart contracts. Once you scaffold smart contracts, you can go to the Open Brush docs: https://docs.openbrush.io/ for further steps.\n\n\n# Installation\n\nYou can install `ink-wizard` either via pip or via homebrew(recommended).\nIf you want to install using pip, it is recommended to use virtualenv.\n\n```sh\nvirtualenv .venv\nsource .venv/bin/activate\npip install ink-wizard\n```\n\nIt you want to install it using homebrew, run the following commands:\n\n```sh\nbrew tap avirajkhare00/homebrew-ink-wizard\nbrew install ink-wizard\n```\n\nJust type `ink-wizard`, you are good to go.\n\n# Usage\n\nIn order to use ink-wizard, you should have `cargo-contract` installed. Run the following command to install it:\n```sh\ncargo install cargo-contract --version 2.0.0-beta\n```\n\nWhen a smart contract is scaffolded, you can go to the directory and can run `cargo-contract contract build`. It will generate .contract, wasm and metadata.json file that you can use.\n\n# Testing\n\nYou can test it either via running `./test.sh` file or you can run tests inside a docker container via `docker build .`\nTo run tests locally:\n```sh\nvirtualenv .venv\npip install -r requirements.txt\n./test.sh\n```\n\nOr you can run `docker build .` to run the tests.\n',
    'author': 'Aviraj Khare',
    'author_email': 'thisisavirajkhare@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
