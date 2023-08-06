# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ts2py', 'ts2py.syntax', 'ts2py.types', 'ts2py.utils']

package_data = \
{'': ['*'], 'ts2py': ['assets/*']}

install_requires = \
['dhparser>=1.3.3,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'typing-extensions>=4.4.0,<5.0.0']

entry_points = \
{'console_scripts': ['ts2py = ts2py.main:main']}

setup_kwargs = {
    'name': 'ts2py',
    'version': '0.0.2',
    'description': 'Python-Interoperability for Typescript-Interfaces',
    'long_description': '# ts2py\n\n![](https://img.shields.io/pypi/v/ts2py)\n![](https://img.shields.io/pypi/status/ts2py)\n![](https://img.shields.io/pypi/pyversions/ts2py)\n![](https://img.shields.io/pypi/l/ts2py)\n\nPython-interoperability for Typescript-Interfaces.\nTranspiles TypeScript-Interface-definitions to Python TypedDicts\n\n## What is this\nThis repo is born as a fork of [ts2python](https://github.com/jecki/ts2python) written by Eckhart Arnold <arnold@badw.de>, Bavarian Academy of Sciences and Humanities. The reason behind this fork was that I needed a **simpler** way to quickly convert *TypeScript* interfaces to Python *TypedDict*. Once I started looking into the initial code I decided to change (and remove) a lot of stuff.\nI also managed to split the code in multiple files and added [Typer](https://typer.tiangolo.com/) to create a beautiful CLI. The initial project should be much more powerful and should also have **support for run-time type-checking of JSON-data**.\n\n## Purpose\nNowadays **a lot** of applications are created with TypeScript. To enable a much better way of developing when dealing with Python backend it could be useful to quickly convert [Typescript-Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html) into Python [TypedDicts](https://www.python.org/dev/peps/pep-0589/). In order to enable structural validation on the Python-side, ts2py transpiles the typescript-interface definitions to Python-data structure definitions.\n\n## Installation\n\n``ts2py`` can be installed from the command line with the command:\n```\npip install ts2py\n```\n\nts2py requires the parsing-expression-grammar-framework [DHParser](https://gitlab.lrz.de/badw-it/DHParser) which will automatically be installed as a dependency by the `pip`-command. ts2py requires at least Python Version 3.10 to run. However, the Python-code it produces is backwards compatible down to Python 3.6 thanks to the [typing extensions](https://pypi.org/project/typing-extensions/).\n\n## Usage\n\nIn order to generate TypedDict-classes from Typescript-Interfaces, run `ts2py` on the Typescript-Interface definitions:\n```\nts2py interfaces.ts\n```\nThis generates a ``.py`` file in same directory as the source file that contains the TypedDict-classes and can simpy be imported in Python-Code:\n```python\nfrom interfaces import *\n```\n\n## License and Source Code\n\n``ts2py`` is open source software under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\n\nThe complete source-code of ts2py can be downloaded from the [its git-repository](https://github.com/thelicato/ts2py).\n',
    'author': 'Angelo Delicato',
    'author_email': 'thelicato@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/thelicato/ts2py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
