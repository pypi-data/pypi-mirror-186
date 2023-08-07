# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nibiru',
 'nibiru.crypto',
 'nibiru.msg',
 'nibiru.pytypes',
 'nibiru.query_clients']

package_data = \
{'': ['*']}

install_requires = \
['aiocron>=1.8,<2.0',
 'aiohttp>=3.8.3,<4.0.0',
 'asyncio>=3.4.3,<4.0.0',
 'bech32>=1.2.0,<2.0.0',
 'bip32>=3.3,<4.0',
 'ecdsa>=0.18.0,<0.19.0',
 'hdwallets>=0.1.2,<0.2.0',
 'importlib-metadata>=5.0.0,<6.0.0',
 'mnemonic>=0.20,<0.21',
 'nibiru-proto==0.17.1',
 'packaging>=21.3,<22.0',
 'pre-commit>=2.20.0,<3.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'shutup>=0.2.0,<0.3.0',
 'websocket-client>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'nibiru',
    'version': '0.17.0',
    'description': 'Python SDK for interacting with Nibiru.',
    'long_description': '# Python SDK - Nibiru Chain    <!-- omit in toc -->\n\n> Python-based client for interacting with the Nibiru blockchain.\n\n<!-- Badges -->\n\n[![Nibiru Test workflow][tests-badge]][tests-workflow]\n[![PyPI Version][pypi-image]][pypi-url]\n[![][documentation-image]][documentation-url]\n[![][discord-badge]][discord-url]\n[![][stars-image]][stars-url]\n[![MIT license][license-badge]][license-link]\n\n<!-- Badges links -->\n\n<!-- pypi -->\n[pypi-image]: https://img.shields.io/pypi/v/nibiru\n[pypi-url]: https://pypi.org/project/nibiru/\n[stars-image]: https://img.shields.io/github/stars/NibiruChain?style=social\n[stars-url]: https://github.com/NibiruChain\n[documentation-image]: https://readthedocs.org/projects/nibiru-py/badge/?version=latest\n[documentation-url]: https://nibiru-py.readthedocs.io/en/latest/?badge=latest\n[discord-badge]: https://dcbadge.vercel.app/api/server/sgPw8ZYfpQ?style=flat\n[discord-url]: https://discord.gg/sgPw8ZYfpQ\n[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg\n[license-link]: https://github.com/NibiruChain/py-sdk/blob/master/LICENSE\n[tests-badge]: https://github.com/NibiruChain/py-sdk/actions/workflows/pytests.yml/badge.svg\n[tests-workflow]: https://github.com/NibiruChain/py-sdk/actions/workflows/pytests.yml\n\nThe `nibiru` package allows you to index, query, and send transactions on Nibiru Chain using Python. It provides access to market data for analysis, visualization, indicator development, algorithmic trading, strategy backtesting, bot programming, and related software engineering.\n\nThe package is intended to be used by coders, developers, technically-skilled traders and  data-scientists for building trading algorithms.\n\n#### README Contents\n\n- [Python SDK Tutorial](#python-sdk-tutorial)\n- [Installation from `PyPI`](#installation-from-pypi)\n- [Usage](#usage)\n  - [Ex: Creating a wallet and SDK client](#ex-creating-a-wallet-and-sdk-client)\n  - [Ex: Using the faucet](#ex-using-the-faucet)\n  - [Ex: Querying chain state](#ex-querying-chain-state)\n  - [Ex: Submitting transactions](#ex-submitting-transactions)\n- [Documentation Website](#documentation-website)\n- [Contributing](#contributing)\n\n## Python SDK Tutorial\n\n<a href="https://colab.research.google.com/github/NibiruChain/py-sdk/blob/master/examples/collab_notebook.ipynb" target="_blank">\n<p align="center">\n  <img src="https://colab.research.google.com/assets/colab-badge.svg" style="width: 300px;">\n</p>\n</a>\n\n## Installation from `PyPI`\n\n```bash\npip install nibiru  # requires Python 3.7+\n```\n\nYou may need to update `pip` to get this to run:\n\n```bash\npython -m pip install --upgrade pip\n```\n\n## Usage\n\n### Ex: Creating a wallet and SDK client\n\n```python\nfrom nibiru import wallet\n\n# Save the mnemonic for later\nmnemonic, private_key = wallet.PrivateKey.generate()\n```\n\nAfter, creating an account, you can create an `Sdk` instance.\n\n```python\nimport nibiru\n\nnetwork = nibiru.network.Network.testnet(2)\nsdk = nibiru.Sdk.authorize(mnemonic)\n  .with_network(network)\n```\n\nThe `Sdk` class creates an interface to sign and send transactions or execute\nqueries. It is associated with:\n- A transaction signer (wallet), which is configured from existing mnemonic to recover a `PrivateKey`.\n- A `Network`, which specifies the RPC, LCD, and gRPC endpoints for connecting to Nibiru Chain.\n- An optional `TxConfig` for changing gas parameters.\n\n### Ex: Using the faucet\n\n```python\nimport requests\n\nrequests.post(\n    "https://faucet.testnet-2.nibiru.fi/",\n    json={\n        "address": sdk.address,\n        "coins": ["10000000unibi", "100000000000unusd"],\n    },\n)\n```\n\n### Ex: Querying chain state\n\n```python\n# Querying the token balances of the account\nsdk.query.get_bank_balances(sdk.address)\n\n# Querying from the vpool module\nquery_resp = sdk.query.vpool.all_pools()\nprint(query_resp)\n# Queries from other modules can be accessed from "sdk.query.module"\n```\n\n### Ex: Submitting transactions\n\n```python\n# version 0.16.3\nfrom nibiru import Msg\n\ntx_resp = sdk.tx.execute_msgs(\n    Msg.perp.open_position(\n        sender=sdk.address,\n        token_pair="ubtc:unusd",\n        is_long=True,\n        quote_asset_amount=10,\n        leverage=10,\n        base_asset_amount_limit=0,\n    )\n)\n```\n\nYou can broadcast any available transaction by passing its corresponding `Msg` to the `sdk.tx.execute_msgs` function.\n\n## Documentation Website\n\nDocumentation can be found here: [Nibiru-py documentation](https://nibiru-py.readthedocs.io/en/latest/index.html)\n\n- Learn more about opening and managing your spot and perp positions [here](https://nibiru-py.readthedocs.io/en/latest/nibiru.sdks.tx.html#nibiru-sdks-tx-package)\n- Learn about querying the chain using the Sdk [here](https://nibiru-py.readthedocs.io/en/latest/nibiru.clients.html#nibiru-clients-package)\n\n## Contributing\n\nPlease read [HACKING.MD](HACKING.md) for developer environment setup.\n',
    'author': 'Nibiru Chain',
    'author_email': 'dev@nibiru.fi',
    'maintainer': 'NibiruHeisenberg',
    'maintainer_email': 'dev@nibiru.fi',
    'url': 'https://github.com/NibiruChain/sdk-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
