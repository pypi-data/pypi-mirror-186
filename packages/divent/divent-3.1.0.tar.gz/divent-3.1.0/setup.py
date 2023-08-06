# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['divent']

package_data = \
{'': ['*'],
 'divent': ['static/css/*',
            'static/fonts/*',
            'static/img/*',
            'templates/*',
            'translations/*']}

install_requires = \
['disnake>=2.7.0,<3.0.0',
 'ics==0.8.0.dev0',
 'python-dotenv>=0.21.0,<0.22.0',
 'quart>=0.18.3,<0.19.0',
 'requests-oauthlib>=1.3.1,<2.0.0',
 'sentry-sdk>=1.13.0,<2.0.0',
 'uvicorn>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['divent = divent.bot:__main__']}

setup_kwargs = {
    'name': 'divent',
    'version': '3.1.0',
    'description': 'The discord scheduled event calendar generator',
    'long_description': '# Divent\n> The discord scheduled event calendar generator\n\n[![Build Status](https://ci.crystalyx.net/api/badges/Xefir/Divent/status.svg)](https://ci.crystalyx.net/Xefir/Divent)\n[![Docker Hub](https://img.shields.io/docker/pulls/xefir/divent)](https://hub.docker.com/r/xefir/divent)\n\nSimple website that guides you to invite a bot to read and format scheduled events to a subscribable calendar.\n\n## Installing / Getting started\n\n### 1) Create the bot\n\n- Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.\n- Enable the `Build-A-Bot` option in the `Bot` panel.\n- Click on `Reset Token` and keep it in a safe place, you will need it.\n- Click on `Reset Secret` in the `OAuth2` panel, copy both `Client ID` and `Client Secret` and keep it in a safe place, you will need it.\n- Configure the rest of your app and bot as you like (name, icon, username, etc.)\n\n### 2) With Docker\n\n- Install [Docker](https://docs.docker.com/get-docker/)\n- Run\n```bash\ndocker run -p 5000 \\\n    -e DISCORD_TOKEN=your_bot_token \\\n    -e OAUTH2_CLIENT_ID=your_client_id \\\n    -e OAUTH2_CLIENT_SECRET=your_client_secret \\\n    xefir/divent\n```\n\n### 2) Without Docker\n\n- Install [Python 3](https://www.python.org/downloads/)\n- Install [Pip](https://pip.pypa.io/en/stable/installation/)\n- Run `pip install divent`\n- Run\n```bash\nDISCORD_TOKEN=your_bot_token \\\nOAUTH2_CLIENT_ID=your_client_id \\\nOAUTH2_CLIENT_SECRET=your_client_secret \\\ndivent\n```\n\n### 3) Open your browser\n\nThe app is accessible at http://localhost:5000\n\n## Links\n\n- [Project homepage](https://divent.crystalyx.net/)\n- [Source repository](https://git.crystalyx.net/Xefir/Divent)\n- [Issue tracker](https://git.crystalyx.net/Xefir/Divent/issues)\n- [My other projects](https://git.crystalyx.net/Xefir)\n- [The WTFPL licence](http://www.wtfpl.net/)\n- [Docker hub](https://hub.docker.com/r/xefir/divent)\n- [Pypi](https://pypi.org/project/Divent/)\n- [Donations](https://paypal.me/Xefir)\n',
    'author': 'Xéfir Destiny',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://divent.crystalyx.net/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
