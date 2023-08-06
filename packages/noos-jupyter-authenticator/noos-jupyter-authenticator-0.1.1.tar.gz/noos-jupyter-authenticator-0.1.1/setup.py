# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['noos_jupyter_authenticator']

package_data = \
{'': ['*']}

install_requires = \
['jupyterhub>=3.0.0,<4.0.0', 'noos-pyk', 'tornado', 'traitlets']

setup_kwargs = {
    'name': 'noos-jupyter-authenticator',
    'version': '0.1.1',
    'description': 'JupyterHub authenticator for the Noos platform.',
    'long_description': '[![CircleCI](https://dl.circleci.com/status-badge/img/gh/noosenergy/noos-jupyter-authenticator/tree/master.svg?style=svg&circle-token=34ea00fda6c7b93facecbbd26d3a1d7ef1cda9d3)](https://dl.circleci.com/status-badge/redirect/gh/noosenergy/noos-jupyter-authenticator/tree/master)\n\n# Noos JupyterHub Authenticator\n\nBespoke JupyterHub `Authenticator`, to enable authentication of [Jupyter hub](https://jupyter.org/hub) via the Noos platform.\n\n\n## Installation\n\nThe python package is available from the [PyPi repository](https://pypi.org/project/noos-jupyter-authenticator),\n\n```sh\npip install noos-jupyter-authenticator\n```\n\n## Configuration\n\nEdit your `jupyterhub_config.py` file and add the following to register `noos_jupyter_authenticator` as a JupyterHub Authenticator class:\n\n```python\nc.Authenticator.auto_login = True\n\nc.JupyterHub.authenticator_class = "noos-jwt"\n\nc.NoosJWTAuthenticator.auth_server_url = "http://<hostname>"\n```\n\n:warning: This Authenticator only works with `jupyterhub >= 3.0.0`.\n\n\n## Development\n\n### Python package manager\n\nOn Mac OSX, make sure [poetry](https://python-poetry.org/) has been installed and pre-configured,\n\n```sh\nbrew install poetry\n```\n\n### Local dev workflows\n\nThe development workflows of this project can be managed by [noos-invoke](https://github.com/noosenergy/noos-invoke), a ready-made CLI for common CI/CD tasks.\n\n```\n$ noosinv\nUsage: noosinv [--core-opts] <subcommand> [--subcommand-opts] ...\n```\n',
    'author': 'Noos Energy',
    'author_email': 'contact@noos.energy',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/noosenergy/noos-jupyter-authenticator',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
