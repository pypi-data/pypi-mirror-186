# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fakts',
 'fakts.cli',
 'fakts.discovery',
 'fakts.discovery.beacon',
 'fakts.discovery.qt',
 'fakts.fakt',
 'fakts.grants',
 'fakts.grants.io',
 'fakts.grants.io.qt',
 'fakts.grants.meta',
 'fakts.grants.remote']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.2', 'QtPy>=2.0.1,<3.0.0', 'koil>=0.2.10', 'pydantic>1.8.2']

extras_require = \
{'remote': ['aiohttp>=3.8.2,<4.0.0', 'certifi>2021']}

setup_kwargs = {
    'name': 'fakts',
    'version': '0.3.5',
    'description': 'asynchronous configuration provider ( tailored to support dynamic client-server relations)',
    'long_description': '# fakts\n\n[![codecov](https://codecov.io/gh/jhnnsrs/fakts/branch/master/graph/badge.svg?token=UGXEA2THBV)](https://codecov.io/gh/jhnnsrs/fakts)\n[![PyPI version](https://badge.fury.io/py/fakts.svg)](https://pypi.org/project/fakts/)\n[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://pypi.org/project/fakts/)\n![Maintainer](https://img.shields.io/badge/maintainer-jhnnsrs-blue)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/fakts.svg)](https://pypi.python.org/pypi/fakts/)\n[![PyPI status](https://img.shields.io/pypi/status/fakts.svg)](https://pypi.python.org/pypi/fakts/)\n[![PyPI download day](https://img.shields.io/pypi/dm/fakts.svg)](https://pypi.python.org/pypi/fakts/)\n\n### DEVELOPMENT\n\n## Inspiration\n\nFakts was designed to make configuration of apps compatible with concurrency pattern, it is designed to allow\nfor asynchronous retrieval of configuration from various sources, may it be a config file, environmental variables\nor a remote server.\n\n# Core Design\n\nFakts uses Grants to obtain configuration asynchronously, a grant is a way of retrieving the configuration from a\nspecific source. It can be a local config file (eg. yaml, toml, json), environemnt variables, a remote configuration (eg. from a fakts server), a database.\nThe fakts class then wraps the grant to ensure both a sychronous and asychronous interface that is threadsafe.\n\nGrants are designed to be composable through MetaGrants so by desigining a specifc grant structure, one can\nhighly customize the retrieval logic. Please check out the\n\n# Example:\n\n```python\nasync with Fakts(grant=YamlGrant("config.yaml")) as fakts:\n    config = await fakts.aget("group_name")\n```\n\nor\n\n```python\nwith Fakts(grant=YamlGrant("config.yaml")) as fakts:\n    config = fakts.get("group_name")\n```\n\nFakts should be used as a context manager, and will set the current fakts context variable to itself, letting\nyou access the current fakts instance from anywhere in your code (async or sync) without specifically passing a referece.\nTo understand how the async sync code access work, please check out the documentation for koil.\n\n# Composability\n\nYou can compose grants through meta grants in order to load configuration from multiple sources (eg. a local, file\nthat can be overwritten by a remote configuration, or some envionment variables).\n\nExample:\n\n```python\nasync with Fakts(grant=FailsafeGrant(\n    grants=[\n        EnvGrant(),\n        YamlGrant("config.yaml")\n    ]\n)) as fakts:\n    config = await fakts.get("group_name")\n```\n\nIn this example fakts will load the configuration from the environment variables first, and if that fails,\nit will load it from the yaml file.\n\n## Special Use Case: Dynamic Server Relations\n\nFakts provides the remote grant protocol for retrieval of configuration in dynamic client-server relationships.\nWith these grants you provide a software manifest for a configuration server (fakts-server), that then grants\nthe configuration (either through user approval (similar to device code grant)). These grants are mainly used\nto setup or claim an oauth2 application on the backend securely that then can be used to identify the application in the\nfuture. These grants are at the moment highly specific to the arkitekt platform and subject to change.\n\n# Sister packages\n\nThese packages provide contrib modules to support auto\nconfiguration through a fakts instance\n\n- herre: oauth2 client\n- rath: graphql client (typed through turms)\n',
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
