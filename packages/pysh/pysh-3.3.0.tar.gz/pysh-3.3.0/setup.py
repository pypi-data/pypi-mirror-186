# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysh']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysh',
    'version': '3.3.0',
    'description': 'A library of small functions that simplify scripting in python',
    'long_description': '# pysh\n\nA library of small functions that simplify scripting in python\n\n## Installation\n\n```bash\npip install pysh\n```\n\n## Usage\n\n### sh\n\nRun a shell command and display the output:\n\n```python\nsh("git status")\n```\n\nCapture the output of a shell command:\n\n```python\nres = sh("git status", capture=True)\nprint(res.stdout)\n```\n\n### cd\n\nChange the current working directory:\n\n```python\ncd("path/to/dir")\n```\n\nChange the current working directory temporarily:\n\n```python\nwith cd("path/to/dir"):\n    sh("git status")\n```\n\n### env\n\nSet an environment variable:\n\n```python\nenv(var="value")\n```\n\nSet an environment variable temporarily:\n\n```python\nwith env(PGPASSWORD="MyPassword", PGUSER="postgres"):\n    sh("createdb -h localhost -p 5432 -O postgres mydb")\n```\n\n### which\n\nChecks whether an executable/script/builtin is available:\n\n```python\ngit_is_installed = which("git")\n```\n',
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ovsyanka83/pysh',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
