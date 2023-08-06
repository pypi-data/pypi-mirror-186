# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['apibara',
 'apibara.indexer',
 'apibara.protocol',
 'apibara.protocol.proto',
 'apibara.starknet',
 'apibara.starknet.proto']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.50,<2.0', 'protobuf>=4.20,<5']

extras_require = \
{':extra == "indexer"': ['pymongo>=4.3.3,<5.0.0']}

setup_kwargs = {
    'name': 'apibara',
    'version': '0.6.1',
    'description': 'Apibara cliend SDK. Stream and transform on-chain data with Python.',
    'long_description': 'Apibara Python SDK\n==================\n\n.. warning::\n    This SDK is alpha software. The API will change drastically until the beta.\n\n    `Open an issue on GitHub <https://github.com/apibara/python-sdk>`_ to report bugs or provide feedback.\n\n\nBuild web3-powered applications in Python. \n\nDevelopment\n-----------\n\nInstall all dependencies with:\n\n.. code::\n\n    poetry install\n\nRun tests with:\n\n.. code::\n\n    poetry run pytest tests\n\nFormat code with:\n\n.. code::\n\n    poetry run black src examples test\n    poetry run isort src examples test\n\nTo update the protobuf definitions:\n\n.. code::\n\n    protoc -I=protos/starknet/ \\\n        --python_out=src/apibara/starknet/proto/ \\\n        --pyi_out=src/apibara/starknet/proto protos/starknet/*\n\n\nLicense\n-------\n\n   Copyright 2022 GNC Labs Limited\n\n   Licensed under the Apache License, Version 2.0 (the "License");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an "AS IS" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n',
    'author': 'Francesco Ceccon',
    'author_email': 'francesco@apibara.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.apibara.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
