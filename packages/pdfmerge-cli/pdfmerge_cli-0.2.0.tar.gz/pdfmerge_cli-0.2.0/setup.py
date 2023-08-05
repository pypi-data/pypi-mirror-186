# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdfmerge']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'pypdf>=3.2.1,<4.0.0']

entry_points = \
{'console_scripts': ['pdfmerge = pdfmerge.main:pdf_merge']}

setup_kwargs = {
    'name': 'pdfmerge-cli',
    'version': '0.2.0',
    'description': 'pdf merge command line',
    'long_description': '# PDF Merge CLI\n\n[![ci](https://github.com/maguowei/pdfmerge/actions/workflows/ci.yml/badge.svg)](https://github.com/maguowei/pdfmerge/actions/workflows/ci.yml)\n[![Upload Python Package](https://github.com/maguowei/pdfmerge/actions/workflows/python-publish.yml/badge.svg)](https://github.com/maguowei/pdfmerge/actions/workflows/python-publish.yml)\n\n## Build\n\n```bash\n$ poetry build\n$ pip install dist/pdfmerge-cli-x.x.x.tar.gz\n```\n\n## Install\n\n```bash\n$ pip install pdfmerge-cli\n```\n\n## Usage\n\n```bash\n$ pdfmerge --input-dir .\n```\n',
    'author': 'maguowei',
    'author_email': 'i.maguowei@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/maguowei/pdfmerge',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
