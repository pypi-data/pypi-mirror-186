# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fireproxify']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.50,<2.0.0',
 'bs4>=0.0.1,<0.0.2',
 'lxml>=4.9.2,<5.0.0',
 'tldextract>=3.4.0,<4.0.0',
 'tzlocal>=4.2,<5.0']

entry_points = \
{'console_scripts': ['fire = fireproxify.cli:cli_main']}

setup_kwargs = {
    'name': 'fireproxify',
    'version': '0.0.1',
    'description': 'Fireprox as a package',
    'long_description': '# fireproxify\n\n[![Release](https://img.shields.io/github/v/release/yok4i/fireproxify)](https://img.shields.io/github/v/release/yok4i/fireproxify)\n[![Build status](https://img.shields.io/github/actions/workflow/status/yok4i/fireproxify/main.yml?branch=main)](https://github.com/yok4i/fireproxify/actions/workflows/main.yml?query=branch%3Amain)\n[![codecov](https://codecov.io/gh/yok4i/fireproxify/branch/main/graph/badge.svg)](https://codecov.io/gh/yok4i/fireproxify)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/yok4i/fireproxify)](https://img.shields.io/github/commit-activity/m/yok4i/fireproxify)\n[![License](https://img.shields.io/github/license/yok4i/fireproxify)](https://img.shields.io/github/license/yok4i/fireproxify)\n\nFireprox as a package\n\n- **Github repository**: <https://github.com/yok4i/fireproxify/>\n- **Documentation** <https://yok4i.github.io/fireproxify/>\n\n## Documentation in progress\n\nWhile the documentation for package is not ready, please see [Documentation for Fireprox](https://github.com/yok4i/fireprox).\n',
    'author': 'Mayk',
    'author_email': 'f7395296+yok4i@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yok4i/fireproxify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
