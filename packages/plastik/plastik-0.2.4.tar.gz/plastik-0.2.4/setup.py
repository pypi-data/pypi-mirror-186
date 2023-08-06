# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['plastik']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.4.0,<22.0.0', 'matplotlib>=3.5.0,<4.0.0', 'numpy>=1.21.4,<2.0.0']

setup_kwargs = {
    'name': 'plastik',
    'version': '0.2.4',
    'description': 'plastic surgery for plt',
    'long_description': '# plastik\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n> plt assist, plastic surgery for plt\n\n## TODO\n\n* Add and set up tests in pre-commit\n\n## Install\n\nThis module is available through [PyPI]:\n\n```sh\npip install plastik\n```\n\nInstalling the development version is done using [poetry]:\n\n```sh\ngit clone https://github.com/engeir/plastik.git\ncd plastik\npoetry install\n```\n\n## Usage\n\n### Functions\n\n* `dark_theme`\n* `log_tick_format`\n* `topside_legends`\n\n### Classes\n\n* `Ridge`\n\n### Example use\n\nSee [examples](examples/example.ipynb).\n\n[PyPI]: https://pypi.org/\n[poetry]: https://python-poetry.org\n',
    'author': 'Eirik Rolland Enger',
    'author_email': 'eirroleng@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/engeir/plastik',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
