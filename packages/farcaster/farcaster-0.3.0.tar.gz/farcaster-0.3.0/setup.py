# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['farcaster']

package_data = \
{'': ['*']}

install_requires = \
['canonicaljson>=1.6.4,<2.0.0',
 'eth-account>=0.8.0,<0.9.0',
 'pydantic>=1.9.2,<2.0.0',
 'pyhumps>=3.7.2,<4.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=4.5.0,<5.0.0']}

setup_kwargs = {
    'name': 'farcaster',
    'version': '0.3.0',
    'description': 'farcaster-py is a Python SDK for the Farcaster Protocol',
    'long_description': '# farcaster-py\n\n<div align="center">\n\n[![Build status](https://github.com/a16z/farcaster-py/workflows/build/badge.svg?branch=master&event=push)](https://github.com/fmhall/farcaster/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/farcaster.svg)](https://pypi.org/project/farcaster/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/a16z/farcaster-py/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/a16z/farcaster-py/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/a16z/farcaster-py/releases)\n[![License](https://img.shields.io/github/license/fmhall/farcaster)](https://github.com/a16z/farcaster-py/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\nfarcaster-py is a modern Python SDK for the Farcaster protocol<br></br>\n\nFull documentation can be found [here](https://a16z.github.io/farcaster-py)\n\n</div>\n\n## Installation\n\n```bash\npip install -U farcaster\n```\n\nor install with [Poetry](https://python-poetry.org/):\n\n```bash\npoetry add farcaster\n```\n\n\n## Usage\nTo use the Farcaster API you need to generate an access token. Here is one way to do that:\n\nFirst install eth-account and dotenv:\n```bash\npip install eth-account python-dotenv # Or \'poetry add eth-account python-dotenv\'\n```\n\nThen you can use a script like this to generate the access token. Note that you can increase the expiration date of the token if you don\'t want to worry about rotation.\n\n```python\nimport time\nimport os\n\nfrom farcaster import MerkleApiClient\nfrom eth_account.account import Account\nfrom dotenv import load_dotenv\n\nload_dotenv()\nAccount.enable_unaudited_hdwallet_features()\nETH_ACCOUNT_SIGNER = Account.from_mnemonic(os.environ.get("<MNEMONIC_ENV_VAR>"))\n\nclient = MerkleApiClient(wallet=ETH_ACCOUNT_SIGNER)\n\nexpiry_ms = int(time.time() + 600)*1000 # This auth token will be valid for 10 minutes. You can increase this up to 1 year\n\naccess_token = client.create_new_auth_token(expires_at=expiry_ms)\n\nprint(access_token) # "MK-...."\n```\n\nSave the auth token somewhere like a `.env` file in your working directory.\n\nFrom now on you can initialize your client like this:\n\n```python\nfrom farcaster import MerkleApiClient\nfrom dotenv import load_dotenv\n\nload_dotenv()\n\nclient = MerkleApiClient(access_token=os.environ.get("<AUTH_ENV_VAR>"))\n\nprint(client.get_healthcheck())\n```\n\n\n## Examples\n\nGet a cast\n\n```python\nresponse = fcc.get_cast("0x321712dc8eccc5d2be38e38c1ef0c8916c49949a80ffe20ec5752bb23ea4d86f")\nprint(response.cast.author.username) # "dwr"\n```\n\nPublish a cast\n\n```python\nfrom farcaster.models import CastsPostRequest\n\ncast_body = CastsPostRequest(text="Hello world!")\nresponse = fcc.post_cast(cast_body)\nprint(response.cast.hash) # "0x...."\n```\n\nGet a user by username\n\n```python\nresponse = fcc.get_user_by_username("mason")\nprint(response.user.username) # "mason"\n```\n\nGet a user\'s followers using a fid (farcaster ID)\n\n```python\nresponse = fcc.get_followers(fid=50)\nprint(response.users) # [user1, user2, user3]\n```\n\nGet users who recently joined Farcaster\n\n```python\nresponse = fcc.get_recent_users()\nprint(response.users) # [user1, user2, user3]\n```\n\nGet your own user object\n\n```python\nresponse = fcc.get_me()\nprint(response.user.username) # "you"\n```\n\nRecast a cast\n\n```python\nresponse = fcc.recast("0x....")\nprint(response.cast.hash) # "0x...."\n```\n\nand many, many more things. The full specification can be found on the [Reference page](https://a16z.github.io/farcaster-py/reference).\n\n\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/fmhall/farcaster)](https://github.com/fmhall/farcaster/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/fmhall/farcaster/blob/master/LICENSE) for more details.\n',
    'author': 'Andreessen Horowitz',
    'author_email': 'crypto-engineering@a16z.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/a16z/farcaster-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>3.7.1,<4.0.0',
}


setup(**setup_kwargs)
