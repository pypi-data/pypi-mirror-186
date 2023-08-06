# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fennel',
 'fennel.client',
 'fennel.client_tests',
 'fennel.datasets',
 'fennel.featuresets',
 'fennel.gen',
 'fennel.lib',
 'fennel.lib.aggregate',
 'fennel.lib.ascii_visualizer',
 'fennel.lib.duration',
 'fennel.lib.graph_algorithms',
 'fennel.lib.metadata',
 'fennel.lib.schema',
 'fennel.lib.to_proto',
 'fennel.lib.window',
 'fennel.sources',
 'fennel.test_lib']

package_data = \
{'': ['*']}

install_requires = \
['astunparse>=1.6.3,<2.0.0',
 'cloudpickle>=2.2.0,<3.0.0',
 'grandalf>=0.7,<0.8',
 'grpcio-tools>=1.49.1,<2.0.0',
 'grpcio>=1.49.1,<2.0.0',
 'jsondiff>=2.0.0,<3.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pytest-mock>=3.9.0,<4.0.0',
 'pytest>=7.1.3,<8.0.0',
 'requests>=2.28.1,<3.0.0',
 'types-requests>=2.28.11,<3.0.0']

setup_kwargs = {
    'name': 'fennel-ai',
    'version': '0.3.6',
    'description': '',
    'long_description': "# Welcome to Fennel\n\n## The modern realtime feature engineering platform\n\n---\n\nFennel is a modern realtime feature engineering platform and has been architected from the ground up in service of three design goals.\n\n## Fennel's Three Design Goals\n1. Easy to install, learn & use - using familiar Python instead of special DSLs, simple but powerful abstractions, zero dependency installation, fully managed with zero ops, same code working for both realtime and non-realtime cases and more to make using Fennel as easy as possible\n2. Reduce cloud costs - being significantly lower on cloud costs compared to other alternatives by squeezing as much out of cloud hardware as possible [See  for how Fennel does this]\n3. Encourage best practices - native support for testing, CI/CD, versioned & immutable features, lineage tracking, enforcement of code ownership, data expectations, read/write compute separation and more to help you bring best engineering practices to feature engineering too\n\nAs a result of the architectural philosophy, Fennel ends up unlocking the following benefits:\n\n## Benefits of Fennel\n\n1. Higher development velocity: more iterations can be done in the same time leading to higher business value\n2. Lower total costs of ownership: Fennel saves costs across the board - cloud spend, bandwidth of engineers that would have gone in ops, and bandwidth of data scientists by making them more productive\n3. Higher business value via realtime features: unlocking realtime and other sophisticated features leads to better models with higher business gains\n4. Healthier codebase & more reliable features: engineering best practices like testing, immutability, code ownership etc improve code maintainability leading to more reliable data & feature\n\n## Getting Started With Fennel\n\n[Start](https://docs.fennel.ai/getting-started/quickstart) here if you want to directly dive deep into an end-to-end example.\n\nOr if you are not in a hurry, read about the main [concepts](https://docs.fennel.ai/overview/concepts) first followed by some more details about the [datasets](https://docs.fennel.ai/datasets/overview)  and [featuresets](https://docs.fennel.ai/featuresets/overview-wip) . And if you run into any issues or have any questions/feedback, you're welcome to jump into our slack channel to directly chat with the engineers building it.\nWe, the team behind Fennel, have thoroughly enjoyed building Fennel and hope learning and using Fennel brings as much delight to you as well!",
    'author': 'Fennel AI',
    'author_email': 'developers@fennel.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
