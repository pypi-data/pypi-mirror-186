# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hitfactorpy',
 'hitfactorpy.parsers',
 'hitfactorpy.parsers.match_report',
 'hitfactorpy.parsers.match_report.pandas',
 'hitfactorpy.parsers.match_report.strict']

package_data = \
{'': ['*']}

install_requires = \
['httpx[http2]>=0.23.3,<0.24.0',
 'pandas>=1.5.2,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'hitfactorpy',
    'version': '0.0.2',
    'description': 'Python tools for parsing and analyzing practical match reports',
    'long_description': '# hitfactorpy\n\nPython tools for parsing and analyzing practical match reports.\n\n## Status\n\n**Work in progress...**\n\nDocumentation website: https:/cahna.github.io/hitfactorpy\n',
    'author': 'Conor Heine',
    'author_email': 'conor.heine@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
