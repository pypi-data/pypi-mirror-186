# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['notional']

package_data = \
{'': ['*']}

install_requires = \
['emoji>=2.0,<3.0',
 'html5lib>=1.1,<2.0',
 'notion-client>=2.0.0,<3.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'urllib3>=1.26.10,<2.0.0']

entry_points = \
{'console_scripts': ['build-docs = devtools:build_docs',
                     'cleanup = devtools:cleanup',
                     'preflight = devtools:preflight',
                     'unit-test = devtools:run_unit_tests']}

setup_kwargs = {
    'name': 'notional',
    'version': '0.7.1',
    'description': 'A high-level interface for the Notion SDK.',
    'long_description': '# notional #\n\n[![PyPI](https://img.shields.io/pypi/v/notional.svg)](https://pypi.org/project/notional)\n[![LICENSE](https://img.shields.io/github/license/jheddings/notional)](LICENSE)\n[![Style](https://img.shields.io/badge/style-black-black)](https://github.com/ambv/black)\n\nA high level interface and object model for the Notion SDK.  This is loosely modeled\nafter concepts found in [SQLAlchemy](http://www.sqlalchemy.org) and\n[MongoEngine](http://mongoengine.org).  Built on the excellent\n[notion-sdk-py](https://github.com/ramnes/notion-sdk-py) library, this module provides\nhigher-level access to the API.\n\n> :warning: **Work In Progress**: The interfaces in this module are still in development\nand are likely to change.  Furthermore, documentation is pretty sparse so use at your\nown risk!\n\nThat being said, if you do use this library, please\n[drop me a message](https://github.com/jheddings/notional/discussions)!\n\n## Installation ##\n\nInstall the most recent release using PyPi:\n\n```shell\npip install notional\n```\n\n*Note:* it is recommended to use a virtual environment (`venv`) for installing libraries\nto prevent conflicting dependency versions.\n\n## Usage ##\n\nConnect to the API using an integration token or an OAuth access token:\n\n```python\nimport notional\n\nnotion = notional.connect(auth=AUTH_TOKEN)\n\n# ¡¡ fun & profit !!\n```\n\n## Getting Help ##\n\nIf you are stuck, the best place to start is the\n[Discussion](https://github.com/jheddings/notional/discussions) area.  Use this also as\na resource for asking questions or providing general suggestions.\n\n### Known Issues ###\n\nSee [Issues](https://github.com/jheddings/notional/issues) on github.\n\n### Feature Requests ###\n\nSee [Issues](https://github.com/jheddings/notional/issues) on github.\n\n## Contributing ##\n\nI built this module so that I could interact with Notion in a way that made sense to\nme.  Hopefully, others will find it useful.  If someone is particularly passionate about\nthis area, I would be happy to consider other maintainers or contributors.\n\nAny pull requests or other submissions are welcome.  As most open source projects go, this\nis a side project.  Large submissions will take time to review for acceptance, so breaking\nthem into smaller pieces is always preferred.  Thanks in advance!\n\nTo get started, please read the full [contribution guide](.github/CONTRIBUTING.md).\n',
    'author': 'Jason Heddings',
    'author_email': 'jheddings@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jheddings/notional/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
