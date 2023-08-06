# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['citric']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23.0,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.6',
                             'typing-extensions>=4.4.0,<5.0.0'],
 'docs': ['furo==2022.4.7',
          'myst-parser==0.17.2',
          'sphinx==4.5.0',
          'sphinx-autoapi==1.8.4',
          'sphinx-autobuild>=2021.3.14,<2022.0.0',
          'sphinx-autodoc-typehints==1.18.1',
          'sphinx-copybutton>=0.5.0,<0.6.0']}

setup_kwargs = {
    'name': 'citric',
    'version': '0.4.3',
    'description': 'A client to the LimeSurvey Remote Control API 2, written in modern Python.',
    'long_description': '<div align="center">\n\n# Citric\n\n<div>\n  <a href="https://github.com/edgarrmondragon/citric/actions?workflow=Tests">\n    <img alt="Tests" src="https://github.com/edgarrmondragon/citric/workflows/Tests/badge.svg"/>\n  </a>\n  <a href="https://results.pre-commit.ci/latest/github/edgarrmondragon/citric/main">\n    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/edgarrmondragon/citric/main.svg"/>\n  </a>\n  <a href="https://github.com/edgarrmondragon/citric/blob/main/LICENSE">\n    <img alt="License" src="https://img.shields.io/github/license/edgarrmondragon/citric"/>\n  </a>\n  <a href="https://citric.readthedocs.io/en/latest/?badge=latest">\n    <img alt="Documentation Status" src="https://readthedocs.org/projects/citric/badge/?version=latest"/>\n  </a>\n  <a href="https://codecov.io/gh/edgarrmondragon/citric">\n    <img alt="codecov" src="https://codecov.io/gh/edgarrmondragon/citric/branch/main/graph/badge.svg"/>\n  </a>\n  <a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fedgarrmondragon%2Fcitric?ref=badge_shield">\n    <img alt="FOSSA Status" src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fedgarrmondragon%2Fcitric.svg?type=shield"/>\n  </a>\n</div>\n\n<div>\n  <a href="https://pypi.org/project/citric">\n    <img alt="PyPI version" src="https://img.shields.io/pypi/v/citric.svg?color=blue"/>\n  </a>\n  <a href="https://pypi.org/project/citric">\n    <img alt="Python versions" src="https://img.shields.io/pypi/pyversions/citric.svg"/>\n  </a>\n  <a href="https://pypi.org/project/citric">\n    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/citric?color=blue"/>\n  </a>\n  <a href="https://pypi.org/project/citric">\n    <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/citric"/>\n  </a>\n</div>\n\n<div>\n  <a href="https://github.com/edgarrmondragon/citric/search?l=python">\n    <img alt="GitHub languages" src="https://img.shields.io/github/languages/top/edgarrmondragon/citric">\n  </a>\n  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/edgarrmondragon/citric">\n  <a href="https://github.com/edgarrmondragon/citric/stargazers">\n    <img alt="GitHub stars" src="https://img.shields.io/github/stars/edgarrmondragon/citric">\n  </a>\n  <a href="https://github.com/edgarrmondragon/citric/commits/main">\n    <img alt="Github last-commit" src="https://img.shields.io/github/last-commit/edgarrmondragon/citric"/>\n  </a>\n</div>\n\nA client to the LimeSurvey Remote Control API 2, written in modern\nPython.\n</div>\n\n## Installation\n\n```console\n$ pip install citric\n```\n\n## Usage\n\n```python\nfrom citric import Client\n\nwith Client(\n    "https://mylimesite.limequery.com/admin/remotecontrol",\n    "myusername",\n    "mypassword",\n) as client\n    for survey in client.list_surveys():\n        print(survey["surveyls_title"])\n```\n\n## Documentation\n\nCode samples and API documentation are available at [citric.readthedocs.io](https://citric.readthedocs.io/).\n\n## Contributing\n\nIf you\'d like to contribute to this project, please see the [contributing guide](https://citric.readthedocs.io/en/latest/contributing/getting-started.html).\n\n## Credits\n\n- [Claudio Jolowicz][claudio] and [his amazing blog post][hypermodern].\n\n[claudio]: https://twitter.com/cjolowicz/\n[hypermodern]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/\n\n## License\n[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fedgarrmondragon%2Fcitric.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fedgarrmondragon%2Fcitric?ref=badge_large)\n',
    'author': 'Edgar Ramírez-Mondragón',
    'author_email': 'edgarrm358@gmail.com',
    'maintainer': 'Edgar Ramírez-Mondragón',
    'maintainer_email': 'edgarrm358@gmail.com',
    'url': 'https://github.com/edgarrmondragon/citric',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
