# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vastai_client']

package_data = \
{'': ['*']}

install_requires = \
['dacite>=1.7.0,<2.0.0', 'loguru>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'vastai-client',
    'version': '0.1.1',
    'description': 'Python client for the Vast.ai cloud rent service.',
    'long_description': "# vastai-client\n\n[![Build Status](https://github.com/Barahlush/vastai-client/workflows/test/badge.svg?branch=master&event=push)](https://github.com/Barahlush/vastai-client/actions?query=workflow%3Atest)\n[![Python Version](https://img.shields.io/pypi/pyversions/vastai-client.svg)](https://pypi.org/project/vastai-client/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\nPython client for the Vast.ai cloud rent service. This package provides a Python client, that allows to list, create, destroy GPU instances programmaticaly, using Python.\n\nThere is an official Vast.ai [CLI](https://github.com/vast-ai/vast-python), however it can only be used through the command line.\n\n\n## Installation\n\n```bash\npip install vastai-client\n```\n\n\n## Example\n\nWith the package you can list offers and run selected machines:\n\n```python\nfrom vastai_client import VastClient\n\nclient = VastClient(api_key=<your_api_key>)\navailable_machines = client.search_offers(search_query='reliability > 0.98 num_gpus=1 gpu_name=RTX_3090', sort_order='dph-')\nprint(available_machines)\n\nselected_machine = available_machines[0]\nclient.create_instance(id=selected_machine.id, image='pytorch/pytorch', ssh=True)\n```\n\nFor more details, watch documentation.\n\n## License\n\n[MIT](https://github.com/Barahlush/vastai-client/blob/master/LICENSE)\n\n\n## Credits\n\nThis project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [9899cb192f754a566da703614227e6d63227b933](https://github.com/wemake-services/wemake-python-package/tree/9899cb192f754a566da703614227e6d63227b933). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/9899cb192f754a566da703614227e6d63227b933...master) since then.\n",
    'author': 'Georgiy Kozhevnikov',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Barahlush/vastai-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
