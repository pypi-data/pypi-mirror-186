# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coder_dojo_common_python']

package_data = \
{'': ['*']}

extras_require = \
{'data': ['jupyterlab>=3.5.2,<4.0.0',
          'matplotlib>=3.6.3,<4.0.0',
          'numpy>=1.24.1,<2.0.0',
          'pandas>=1.5.2,<2.0.0',
          'plotly>=5.12.0,<6.0.0'],
 'games': ['pgzero>=1.2.1,<2.0.0', 'pygame>=2.1.2,<3.0.0']}

setup_kwargs = {
    'name': 'coder-dojo-common-python',
    'version': '0.0.2',
    'description': 'Common packages for coder dojo sessions',
    'long_description': '# Coder Dojo (Ham/Kingston) Common Python Packages\n\nBasic packages containing all the Python dependencies for the Coder Dojo Sessions.\n\n## Installation\nYou can install the package from PyPI using the following command.\n\n```shell\n\'pip install "coder-dojo-common-python[games,data]"\n```\n\n\nYou can install the package from GitHub using the following command.\n\n```shell\npip install \'coder_dojo_common_python[games,data] @ https://github.com/Stedders/coder-dojo-common-python/releases/download/v0.0.1/coder_dojo_common_python-0.0.1-py3-none-any.whl\'\n```\n\nThis will install the games and data packages for the v0.0.1 release.\n\nAs packages are updated or new packages added a new version will be published, please check the latest version\nat https://github.com/Stedders/coder-dojo-common-python/releases.\n\n## Development\n\nRequires poetry.\n\n### Install\n\n```shell\npoetry install\n```\n\n### Add package\n\nAll packages are added as optional and grouped into extras.\n\n```shell\npoetry add requests --optional\n```\n\nYou will then need to update the extra information to ensure the package is in the correct group.\n\nEither update the appropriate extras section or create a new section under extras in\nthe [pyproject.toml](pyproject.toml) file.\n\n```toml\n[tool.poetry.dependencies]\n#...stuff...\nrequests = { version = "^2.28.2", optional = true } # Package added as optional\n#...more stuff...\n\n[tool.poetry.extras]\n#...existing extras...\nweb = ["requesets"] # A new extra \'web\'\n```\n\n### Build package\n```shell\npoetry build\n```',
    'author': 'Stedders',
    'author_email': '3862686+Stedders@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
