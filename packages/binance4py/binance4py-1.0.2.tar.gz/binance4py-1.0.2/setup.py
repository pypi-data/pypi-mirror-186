# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['binance4py', 'binance4py.resources']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0']

setup_kwargs = {
    'name': 'binance4py',
    'version': '1.0.2',
    'description': 'Python binance API wrapper',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/ren3104/binance4py/main/assets/binance4py_logo.png" alt="binance4py logo" width="480">\n</p>\n\n<p align="center">\n  <a href="https://github.com/ren3104/binance4py/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ren3104/binance4py"></a>\n  <a href="https://pypi.org/project/binance4py"><img src="https://img.shields.io/pypi/v/binance4py?color=blue&logo=pypi&logoColor=FFE873" alt="PyPi package version"></a>\n  <a href="https://pypi.org/project/binance4py"><img src="https://img.shields.io/pypi/pyversions/binance4py.svg?logo=python&logoColor=FFE873" alt="Supported python versions"></a>\n  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>\n</p>\n\nThis is an asynchronous Python wrapper for Binance exchange API.\n\n## Features\n- Implementation of all general, market, spot and websocket endpoints\n- Easy to contribute and use\n- Fully typed\n\n## Installation\n```bash\npip install -U binance4py\n```\n\n## Quick Start\n```python\nimport asyncio\nfrom binance4py import Binance\n\n\nasync def handle_kline(k):\n    print(k)\n\n\nasync def main():\n    client = Binance("<API_KEY>", "<API_SECRET>", testnet=True)\n    async with client:\n        print(await client.general.server_time())\n        await client.ws.start()\n        await client.ws.kline(handle_kline, "btcbusd", "1m")\n        print(await client.ws.subscriptions())\n        await client.ws.wait_stop()\n\n\nasyncio.run(main())\n```\n\n## Using a different TLD and Cluster\nThis example will change all binance urls that support this from `https://api.binance.com` to `https://api2.binance.jp`\n```\nclient = Binance(\n    tld="jp",\n    cluster=2\n)\n```\n\n## Using a different json dumper/loader\n```\nimport ujson\n\n\nclient = Binance(\n    json_dumps=ujson.dumps,\n    json_loads=ujson.loads\n)\n```\n',
    'author': 'ren3104',
    'author_email': '2ren3104@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ren3104/binance4py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
