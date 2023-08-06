# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_babel']

package_data = \
{'': ['*']}

install_requires = \
['Babel>=2.11.0,<3.0.0',
 'Flask>=2.0.0,<3.0.0',
 'Jinja2>=3.1.2,<4.0.0',
 'pytz>=2022.7,<2023.0']

setup_kwargs = {
    'name': 'flask-babel',
    'version': '3.0.0',
    'description': 'Adds i18n/l10n support fo Flask applications.',
    'long_description': '# Flask Babel\n\n![Tests](https://github.com/python-babel/flask-babel/workflows/Tests/badge.svg?branch=master)\n[![PyPI](https://img.shields.io/pypi/v/flask-babel.svg?maxAge=2592000)](https://pypi.python.org/pypi/Flask-Babel)\n\nImplements i18n and l10n support for Flask. This is based on the Python\n[babel][] and [pytz][] modules.\n\n## Documentation\n\nThe latest documentation is available [here][docs].\n\n[babel]: https://github.com/python-babel/babel\n[pytz]: https://pypi.python.org/pypi/pytz/\n[docs]: https://python-babel.github.io/flask-babel/\n[semver]: https://semver.org/\n',
    'author': 'Armin Ronacher',
    'author_email': 'None',
    'maintainer': 'Tyler Kennedy',
    'maintainer_email': 'tk@tkte.ch',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
