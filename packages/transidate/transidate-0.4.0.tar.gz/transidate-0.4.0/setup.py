# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['transidate']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0',
 'cryptography>=3.3.0',
 'lxml>=4.6.0',
 'prettytable>=2.0.0',
 'pydantic>=1.8.0',
 'requests>=2.24.0',
 'rich>=9.12.0']

entry_points = \
{'console_scripts': ['transidate = transidate.cli:cli']}

setup_kwargs = {
    'name': 'transidate',
    'version': '0.4.0',
    'description': 'Commandline tool for XML transit data validation.',
    'long_description': "[![PyPI version](https://badge.fury.io/py/transidate.svg)](https://badge.fury.io/py/transidate)\n[![test](https://github.com/ciaranmccormick/transidate/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/ciaranmccormick/transidate/actions/workflows/test.yaml)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/ciaranmccormick/transidate/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n[![codecov](https://codecov.io/gh/ciaranmccormick/transidate/branch/develop/graph/badge.svg?token=I3693DR0S9)](https://codecov.io/gh/ciaranmccormick/transidate)\n\n\n# Transidate\n\nTransidate is a commandline tool for validating transit data files such as TransXChange\nNeTEx and SIRI.\n\nTransidate can validate several transit data formats out of the box.\n\n## Compatibility\n\nTransidate requires Python 3.7 or later.\n\n\n## Installing\n\nInstall transidate using `pip` or any other PyPi package manager.\n\n```sh\npip install transidate\n```\n\n## Validate an XML file\n\nTransidate comes with a help guide to get you started. This will list all the options as\nwell as the transit data formats that are supported.\n\n```sh\ntransidate --help\n```\n\nTo validate a data source just specify the path to the data and the schema to validate\nthe data against. If the `--version` is not specified the data is automatically\nvalidated again TransXChange v2.4.\n\n```sh\ntransidate validate --version TXC2.4 linear.xml\n```\n\n![XML with no violations](https://raw.githubusercontent.com/ciaranmccormick/transidate/main/imgs/transidategoodfile.gif)\nIf transidate finds any schema violations it will print the details of the violation\nsuch as the file it occurred in, the line number of the violation and details.\n\n![XML with violations](https://raw.githubusercontent.com/ciaranmccormick/transidate/main/imgs/transidatebadfile.gif)\n## Validate many files at once\n\nYou can also use transidate to validate a archived collection of files.\n\n```sh\ntransidate validate --version TXC2.4 routes.zip\n```\n\n![Zip with no violations](https://raw.githubusercontent.com/ciaranmccormick/transidate/main/imgs/transidategoodzip.gif)\nThis will iterate over each XML file contained within the zip and collate all the\nviolations.\n\n![Zip with violations](https://raw.githubusercontent.com/ciaranmccormick/transidate/main/imgs/transidatebadzip.gif)\n## Export violations to CSV\n\nSchema violations can be saved to a CSV file using the `--csv` flag.\n\n```sh\ntransidate validate --version TXC2.4 --csv routes.zip\n```\n\n## Configuration\n\nTransidate comes configured with several schemas out of the box. It is really\neasy to add your own schema validators to `transidate`. The first step is to\ncreate a configuration file e.g. `touch transidate.cfg`.\n\nTransidate fetches schemas from web in a zip format, to add a schema you\njust need to define the name, url and root.\n\n```ini\n[MYSCHEMA] # The 'version'\nurl=http://linktoschema.url/schema.zip # where transidate can get the schema\nroot=schema_root_file.xml # the root of the schema\n```\n\nThen you can just pass the schema configuration using `--schemas`.\n\n```sh\ntransidate validate --version MYSCHEMA --schemas transidate.cfg linear.xml\n```\n\nYou can list all the avialble schemas list th `list` command.\n\n```sh\ntransidate list\n```\n\n![List schemas](https://raw.githubusercontent.com/ciaranmccormick/transidate/main/imgs/transidatelist.gif)\n",
    'author': 'Ciaran McCormick',
    'author_email': 'ciaran@ciaranmccormick.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
