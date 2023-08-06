# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rath',
 'rath.contrib.fakts',
 'rath.contrib.fakts.links',
 'rath.contrib.herre.links',
 'rath.links',
 'rath.links.testing',
 'rath.qt',
 'rath.turms',
 'rath.turms.plugins']

package_data = \
{'': ['*']}

install_requires = \
['graphql-core>=3.2.0,<4.0.0', 'koil>=0.2.10', 'pydantic>=1.9.0,<2.0.0']

extras_require = \
{'aiohttp': ['aiohttp>=3.8.2,<4.0.0', 'certifi>2021'],
 'httpx': ['httpx>=0.23.0,<0.24.0'],
 'websockets': ['websockets>=10.2,<11.0']}

setup_kwargs = {
    'name': 'rath',
    'version': '0.3.5',
    'description': 'async transport-agnostic graphql client',
    'long_description': '# rath\n\n[![codecov](https://codecov.io/gh/jhnnsrs/rath/branch/master/graph/badge.svg?token=UGXEA2THBV)](https://codecov.io/gh/jhnnsrs/rath)\n[![PyPI version](https://badge.fury.io/py/rath.svg)](https://pypi.org/project/rath/)\n[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://pypi.org/project/rath/)\n![Maintainer](https://img.shields.io/badge/maintainer-jhnnsrs-blue)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/rath.svg)](https://pypi.python.org/pypi/rath/)\n[![PyPI status](https://img.shields.io/pypi/status/rath.svg)](https://pypi.python.org/pypi/rath/)\n[![PyPI download month](https://img.shields.io/pypi/dm/rath.svg)](https://pypi.python.org/pypi/rath/)\n\n### BETA\n\n## Inspiration\n\nRath is a transportation agnostic graphql client for python focused on composability. It utilizes Links to\ncompose GraphQL request logic, similar to the apollo client in typescript. It comes with predefined links to\nenable transports like aiohttp, websockets and httpx, as well as links to retrieve auth tokens, enable retry logic\nor validating requests on a schema.\n\n## Supported Transports\n\n- aiohttp\n- httpx\n- websockets\n\n## Installation\n\n```bash\npip install rath\n```\n\n## Usage Example\n\n```python\nfrom rath.links.auth import AuthTokenLink\nfrom rath.links.aiohttp import AIOHttpLink\nfrom rath.links import compose, split\nfrom rath.gql import gql\n\nasync def aload_token():\n    return "SERVER_TOKEN"\n\n\nauth = AuthTokenLink(token_loader=aload_token)\nlink = AIOHttpLink(endpoint_url="https://api.spacex.land/graphql/")\n\n\nwith Rath(links=compose(auth,link)) as rath:\n    query = """query TestQuery {\n      capsules {\n        id\n        missions {\n          flight\n        }\n      }\n    }\n    """\n\n    result = rath.query(query)\n```\n\nThis example composes both the AuthToken and AioHttp link: During each query the Bearer headers are set to the retrieved token, on authentication fail (for example if Token Expired) the AuthToken automatically refetches the token and retries the query.\n\n## Async Usage\n\nRath is build for async usage but uses koil, for async/sync compatibility\n\n```python\nfrom rath.links.auth import AuthTokenLink\nfrom rath.links.aiohttp import AIOHttpLink\nfrom rath.links import compose, split\nfrom rath.gql import gql\n\nasync def aload_token():\n    return "SERVER_TOKEN"\n\n\nauth = AuthTokenLink(token_loader=aload_token)\nlink = AIOHttpLink(endpoint_url="https://api.spacex.land/graphql/")\n\n\nasync def main():\n\n  async with Rath(links=compose(auth,link)) as rath:\n      query = """query TestQuery {\n        capsules {\n          id\n          missions {\n            flight\n          }\n        }\n      }\n      """\n\n      result = await rath.query(query)\n\nasyncio.run(main())\n```\n\n## Example Transport Switch\n\nLinks allow the composition of additional logic based on your graphql operation. For example you might want\nto use different grapqhl transports for different kind of operations (e.g using websockets for subscriptions,\nbut using standard http requests for potential caching on queries and mutations). This can be easily\naccomplished by providing a split link.\n\n```python\nlink = SplitLink(\n  AioHttpLink(url="https://api.spacex.land/graphql/"),\n  WebsocketLink(url="ws://api.spacex.land/graphql/",\n  lambda o: o.node.operation == OperationType.SUBSCRIPTION\n)\n\nrath = Rath(link=link)\n\n```\n\n## Included Links\n\n- Validating Link (validate query against local schema (or introspect the schema))\n- Reconnecting WebsocketLink\n- AioHttpLink (supports multipart uploads)\n- SplitLink (allows to split the terminating link - Subscription into WebsocketLink, Query, Mutation into Aiohttp)\n- AuthTokenLink (Token insertion with automatic refres\n\n## Authentication\n\nIf you want to use rath with herre for getting access_tokens in oauth2/openid-connect scenarios, there is also a herre link\nin this repository\n\n### Why Rath\n\nWell "apollo" is already taken as a name, and rath (according to wikipedia) is an etruscan deity identified with Apollo.\n\n## Rath + Turms\n\nRath works especially well with turms generated typed operations:\n\n```python\nimport asyncio\nfrom examples.api.schema import aget_capsules\nfrom rath.rath import Rath\nfrom rath.links.aiohttp import AIOHttpLink\nfrom rath.links.auth import AuthTokenLink\nfrom rath.links.compose import compose\n\n\nasync def token_loader():\n    return ""\n\n\nlink = compose(\n    AuthTokenLink(token_loader), AIOHttpLink("https://api.spacex.land/graphql/")\n)\n\n\nrath = Rath(\n    link=link,\n    register=True, # allows global access (singleton-antipattern, but rath has no state)\n)\n\n\nasync def main():\n\n    async with rath:\n        capsules = await aget_capsules() # fully typed pydantic powered dataclasses generated through turms\n        print(capsules)\n\n\nasyncio.run(main())\n\n```\n\n## Examples\n\nThis github repository also contains an example client with a turms generated query with the public SpaceX api, as well as a sample of the generated api.\n',
    'author': 'jhnnsrs',
    'author_email': 'jhnnsrs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
