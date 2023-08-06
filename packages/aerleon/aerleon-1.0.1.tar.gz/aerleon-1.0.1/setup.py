# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aerleon', 'aerleon.lib', 'aerleon.utils', 'lib']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'absl-py>=1.2.0,<2.0.0',
 'ply>=3.11,<4.0',
 'typing_extensions>=4.4.0,<5.0.0']

extras_require = \
{':python_version <= "3.10"': ['importlib-metadata>=4.2,<5.0']}

entry_points = \
{'console_scripts': ['aclgen = aerleon.aclgen:EntryPoint']}

setup_kwargs = {
    'name': 'aerleon',
    'version': '1.0.1',
    'description': 'A firewall generation tool',
    'long_description': '![GitHub](https://img.shields.io/github/license/aerleon/aerleon) [![PyPI version](https://badge.fury.io/py/aerleon.svg)](https://badge.fury.io/py/aerleon) ![PyPI - Status](https://img.shields.io/pypi/status/aerleon)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aerleon) [![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/aerleon/aerleon/main.yml?branch=main) ![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/aerleon/aerleon)[![codecov](https://codecov.io/gh/aerleon/aerleon/branch/main/graph/badge.svg?token=C13SR6GMTD)](https://codecov.io/gh/aerleon/aerleon)\n\n# Aerleon\n\nGenerate firewall configs for multiple firewall platforms from a single platform-agnostic configuration language through a command line tool and Python API.\n\nAerleon is a fork of [Capirca](https://github.com/google/capirca) with the following enhancements:\n\n- New platform generators can now be added as plugins. Users no longer need to fork the project to add support for new platforms. Common platform support is still built in.\n- YAML is now supported for policy files, network definitions, and service definitions.\n- A powerful new Generate API is added that accepts policies, network definitions, and service definitions as native Python data.\n- Performance in address book generation for SRX and Palo Alto targets is greatly improved.\n- A detailed regression test suite was added to the project.\n- Unit and regression tests run automatically on all pull requests.\n- New developer tools are integrated with the project: Poetry, PyProject, nox, Codecov, Sigstore.\n\nSee the [1.0.1 Release Notes](https://github.com/aerleon/aerleon/releases/tag/1.0.1) for a complete list of changes.\n\n\n## Install\n\nAerleon requires Python 3.7 or higher.\n\n```bash\npip install aerleon\n```\n\n## Overview\n\nAerleon provides a command line tool and a Python API that will generate configs for multiple firewall platforms from a single platform-agnostic configuration language. It can generate configs for Cisco, Juniper, Palo Alto Networks and [many other firewall vendors](https://aerleon.readthedocs.io/en/latest/#core-supported-generators).\n\nA [getting started guide](https://aerleon.readthedocs.io/en/latest/getting_started/) walking through the basics of using Aerleon is avaiable on the docs website.\n\n## Documentation\n\nDocumentation can be found at [https://aerleon.readthedocs.io/en/latest/](https://aerleon.readthedocs.io/en/latest/).\n\n## Contributing\n\nContributions are welcome. Please review the [contributing guidelines](https://aerleon.readthedocs.io/en/latest/contributing/) and [code of conduct](https://github.com/aerleon/aerleon/blob/main/CODE_OF_CONDUCT.md) for this project.\n\n## Contact\n\nOfficial channels for communicating issues is via [Github Issues](https://github.com/aerleon/aerleon/issues).\n\nGeneral discussions can be had either in [Github Discussions](https://github.com/aerleon/aerleon/discussions) or in our [Slack Server](https://join.slack.com/t/aerleon/shared_invite/zt-1ngckm6oj-cK7yj63A~JgqjixEui2Vhw).\n\n### Contact Maintainers\n\nYou can always reach out to us on  [Slack](https://join.slack.com/t/aerleon/shared_invite/zt-1ngckm6oj-cK7yj63A~JgqjixEui2Vhw).\nYou many also reach out to us via e-mail.\n\nRob Ankeny ([ankenyr@gmail.com](mailto:ankenyr@gmail.com))\n\nJason Benterou ([jason.benterou@gmail.com](mailto:jason.benterou@gmail.com))\n\n## Resources\n- [Brief Overview (4 slides):](https://docs.google.com/present/embed?id=dhtc9k26_13cz9fphfb&autoStart=true&loop=true&size=1)\n- [Nanog49; Enterprise QoS](http://www.nanog.org/meetings/nanog49/presentations/Tuesday/Chung-EnterpriseQoS-final.pdf)\n- [Blog Post: Safe ACL Change through Model-based Analysis](https://tech.ebayinc.com/engineering/safe-acl-change-through-model-based-analysis/)\n- [Aerleon Slack](https://aerleon.slack.com/)\n- [#aerleon at NetworkToCode Slack](https://networktocode.slack.com/)\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tbody>\n    <tr>\n      <td align="center"><a href="https://github.com/itdependsnetworks"><img src="https://avatars.githubusercontent.com/u/9260483?v=4?s=100" width="100px;" alt="Ken Celenza"/><br /><sub><b>Ken Celenza</b></sub></a><br /><a href="https://github.com/aerleon/aerleon/commits?author=itdependsnetworks" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://github.com/fischa"><img src="https://avatars.githubusercontent.com/u/11302991?v=4?s=100" width="100px;" alt="Axel F"/><br /><sub><b>Axel F</b></sub></a><br /><a href="https://github.com/aerleon/aerleon/commits?author=fischa" title="Documentation">📖</a></td>\n    </tr>\n  </tbody>\n  <tfoot>\n    <tr>\n      <td align="center" size="13px" colspan="7">\n        <img src="https://raw.githubusercontent.com/all-contributors/all-contributors-cli/1b8533af435da9854653492b1327a23a4dbd0a10/assets/logo-small.svg">\n          <a href="https://all-contributors.js.org/docs/en/bot/usage">Add your contributions</a>\n        </img>\n      </td>\n    </tr>\n  </tfoot>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n\n## Credit\n\nFiles and code included in this project from Capirca are copyright Google and\nare included under the terms of the Apache License, Version 2.0. You may obtain\na copy of the License at\n\n  <http://www.apache.org/licenses/LICENSE-2.0>\n\nContributors who wish to modify files bearing a copyright notice are obligated\nby the terms of the Apache License, Version 2.0 to include at the top of the\nfile a prominent notice stating as much. Copyright notices must not be removed\nfrom files in this repository.\n\nThis README file and other documentation files may contain phrases and sections that are copyright Google.\nThis file and other documentation files are modified from the original by the Aerleon Project Team.\n',
    'author': 'Rob Ankeny',
    'author_email': 'ankenyr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aerleon/aerleon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
