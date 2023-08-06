# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['splatlog',
 'splatlog.json',
 'splatlog.lib',
 'splatlog.lib.functions',
 'splatlog.lib.rich',
 'splatlog.lib.rich.formatter',
 'splatlog.verbosity']

package_data = \
{'': ['*']}

install_requires = \
['rich>=9', 'typeguard==3.0.0b2']

setup_kwargs = {
    'name': 'splatlog',
    'version': '0.3.1',
    'description': "Python logger that accepts ** values and prints 'em out.",
    'long_description': 'splatlog\n==============================================================================\n\nPython logger that accepts ** values and prints \'em out.\n\nBecause I\'ll forget, and because I know I\'ll look here when I do...\n\nPublishing\n------------------------------------------------------------------------------\n\n1.  Update the version in `pyproject.toml`.\n    \n2.  Commit, tag `vX.Y.Z`, push.\n    \n3.  Log in to [PyPI](https://pypi.org) and go to\n    \n    https://pypi.org/manage/account/\n    \n    to generate an API token.\n    \n4.  Throw `poetry` at it:\n    \n        poetry publish --build --username __token__ --password <token>\n    \n5.  Bump patch by 1 and append `a0`, commit and push (now we\'re on the "alpha"\n    of the next patch version).\n\nBulding Docs\n------------------------------------------------------------------------------\n\n    poetry run novella -d ./docs\n    \nServing them:\n\n    poetry run novella -d ./docs --serve\n    \n\nRunning Tests\n------------------------------------------------------------------------------\n\nAll of them:\n\n    poetry run dr.t ./splatlog/**/*.py ./docs/content/**/*.md\n\nSingle file, fail-fast, printing header panel (so you can find where they\nstart and end easily during repeated runs):\n\n    poetry run dr.t -fp <filename>\n',
    'author': 'nrser',
    'author_email': 'neil@neilsouza.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
