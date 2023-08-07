# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['machinable', 'machinable.schedule', 'machinable.storage']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2,<2.0',
 'commandlib>=0.3.5,<0.4.0',
 'flatten-dict>=0.4,<0.5',
 'jsonlines>=3.1,<4.0',
 'observable>=1.0,<2.0',
 'omegaconf>=2.3.0,<3.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'python-baseconv>=1.2,<2.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=6.0,<7.0']}

entry_points = \
{'console_scripts': ['machinable = machinable.cli:Cli']}

setup_kwargs = {
    'name': 'machinable',
    'version': '4.0',
    'description': 'A modular configuration system for research projects',
    'long_description': '# machinable\n\n<div align="center">\n  <img style="width:15%;" src="https://raw.githubusercontent.com/machinable-org/machinable/main/docs/logo/logo.png">\n</div>\n\n<div align="center">\n\n[![Build status](https://github.com/machinable-org/machinable/workflows/build/badge.svg)](https://github.com/machinable-org/machinable/actions?query=workflow%3Abuild)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/machinable-org/machinable/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License](https://img.shields.io/github/license/machinable-org/machinable)](https://github.com/machinable-org/machinable/blob/main/LICENSE)\n\n</div>\n\n<br />\n\n**machinable** provides a system to manage research code effectively. Using a unified and modular representation, machinable can help structure your projects in a principled way so you can move quickly while enabling reuse and collaboration.\n\nVisit the [documentation](https://machinable.org/) to get started.\n',
    'author': 'Frithjof Gressmann',
    'author_email': 'hello@machinable.org',
    'maintainer': 'Frithjof Gressmann',
    'maintainer_email': 'hello@machinable.org',
    'url': 'https://machinable.org',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
