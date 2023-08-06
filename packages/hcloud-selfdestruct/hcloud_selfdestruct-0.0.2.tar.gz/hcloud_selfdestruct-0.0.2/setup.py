# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hcloud_selfdestruct']

package_data = \
{'': ['*']}

install_requires = \
['apprise>=1.2.1,<2.0.0', 'hcloud>=1.18.2,<2.0.0']

entry_points = \
{'console_scripts': ['hcloud-selfdestruct = hcloud_selfdestruct:main']}

setup_kwargs = {
    'name': 'hcloud-selfdestruct',
    'version': '0.0.2',
    'description': 'cli tool to self destruct a hetzner cloud server',
    'long_description': '<h1 align="center">💣 hcloud-selfdestruct</h1>\n<p align="center">\n  <i>A cli tool to self destruct a hetzner cloud server</i>\n</p>\n\n[![Stable Version](https://img.shields.io/pypi/v/hcloud-selfdestruct?color=blue)](https://pypi.org/project/hcloud-selfdestruct/)\n[![License](https://img.shields.io/badge/license-MIT-green?logo=opensourceinitiative&logoColor=fff)](https://github.com/worldworm/hcloud-selfdestruct/blob/main/LICENSE)\n[![Mentioned in Awesome hcloud](https://camo.githubusercontent.com/e5d3197f63169393ee5695f496402136b412d5e3b1d77dc5aa80805fdd5e7edb/68747470733a2f2f617765736f6d652e72652f6d656e74696f6e65642d62616467652e737667)](https://github.com/hetznercloud/awesome-hcloud)\n[![Open in GitHub Codespaces](https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-black?logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=565239435&machine=basicLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=WestEurope)\n\n\n## Why\n\nAre you using a hetzner cloud server for heavy and long-running computing power? But you don\'t want to have additional costs when the calculation is done?\n\nWith hcloud-selfdestruct, the server instance now self-destructs after the computation and generates no further costs.\n\n> **Warning**\n> This tool is in early development and may not work as expected.\n\n\n## Installation\n```bash\npip install hcloud-selfdestruct\n```\n## Usage\n```\nlongrunningcommand && hcloud-selfdestruct --api-token abcdefg &\n#-- or --\nsleep 1h && hcloud-selfdestruct --api-token abcdefg --server-id 12345678 --apprise-id gotify://example.com/token &\n```\n\n## Help\n```\n> hcloud-selfdestruct --help\nusage: hcloud-selfdestruct [-h] --api-token API_TOKEN [--server-id SERVER_ID] [--apprise-id APPRISE_ID] [--shutdown]\n\ncli tool to self destruct a hetzner cloud server\n\noptions:\n  -h, --help            show this help message and exit\n  --api-token API_TOKEN, --api API_TOKEN, --token API_TOKEN\n                        hetzner cloud api token\n\n  --server-id SERVER_ID, --server SERVER_ID, --id SERVER_ID\n                        server id\n\n  --apprise-id APPRISE_ID, --apprise APPRISE_ID, --notify APPRISE_ID\n                        apprise notification string\n\n  --shutdown            just shutdown the server and not destroy it\n```\n\nFind the apprise syntax here: [apprise wiki](https://github.com/caronc/apprise/wiki#notification-services)\n\nFind the server id here (enter without "#")\n![How to find the server id](./.media/howToFindServerId.png "How to find the server id")\n\n## Not yet tested\n- server instances with mounted volume\n- additional addons that could prevent deletion\n- complete self detection\n---\n<p align="center">\n  <i>© <a href="https://github.com/worldworm">worldworm</a> 2023</i><br>\n  <i>Licensed under <a href="https://github.com/worldworm/hcloud-selfdestruct/blob/main/LICENSE">MIT</a></i><br>\n</p>\n',
    'author': 'worldworm',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/worldworm/hcloud-selfdestruct',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
