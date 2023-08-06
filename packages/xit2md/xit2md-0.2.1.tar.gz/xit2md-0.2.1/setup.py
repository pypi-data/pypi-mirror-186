# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xit2md']

package_data = \
{'': ['*']}

install_requires = \
['stage-left>=0.1.1,<0.3.0']

entry_points = \
{'console_scripts': ['xit2md = xit2md:main']}

setup_kwargs = {
    'name': 'xit2md',
    'version': '0.2.1',
    'description': 'Convert [x]it! to markdown',
    'long_description': '# xit2md\n\n[![Run tests](https://github.com/chris48s/xit2md/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/chris48s/xit2md/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/chris48s/xit2md/branch/main/graph/badge.svg?token=8W93RI841H)](https://codecov.io/gh/chris48s/xit2md)\n[![PyPI Version](https://img.shields.io/pypi/v/xit2md.svg)](https://pypi.org/project/xit2md/)\n![License](https://img.shields.io/pypi/l/xit2md.svg)\n![Python Compatibility](https://img.shields.io/badge/dynamic/json?query=info.requires_python&label=python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fxit2md%2Fjson)\n![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)\n\n[[x]it!](https://xit.jotaen.net/) is a plain-text file format for todos and check lists. xit2md converts a checklist in [x]it! format to markdown task lists. Markdown task lists are available in many markdown dialects including GitHub Flavored Markdown.\n\n## Installation\n\n```\npip install xit2md\n```\n\n## Usage\n\n### On the Console\n\n```sh\n# convert [x]it! file to markdown file\n$ xit2md in.xit > out.md\n\n# fetch [x]it! file from the web and convert to markdown\n$ curl "https://myserver.com/example.xit" | xit2md\n```\n\n### As a Library\n\n```pycon\n>>> from xit2md import xit2md_text\n\n>>> xit = """Named Group\n... [ ] Open\n... [x] Checked\n... [@] Ongoing\n... [~] Obsolete\n... [?] In Question\n... """\n\n>>> print(xit2md_text(xit, heading_level=2))\n## Named Group\n- [ ] Open\n- [x] Checked\n- [ ] Ongoing\n- [x] ~Obsolete~\n- [ ] In Question\n```\n',
    'author': 'chris48s',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chris48s/xit2md',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
