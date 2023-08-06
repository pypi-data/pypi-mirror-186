# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aiomisc_entrypoint', 'aiomisc_entrypoint.processors']

package_data = \
{'': ['*']}

install_requires = \
['aiomisc>=16.2.10,<17.0.0']

setup_kwargs = {
    'name': 'aiomisc-entrypoint',
    'version': '1.0.0',
    'description': '',
    'long_description': "# Aiomisc Entrypoint\n\nAlternative way to run [aiomisc entrypoint](https://aiomisc.readthedocs.io/en/latest/entrypoint.html#entrypoint) with processors\nadded behavior to start and stop events of entrypoint and custom query logger.\n\n\n## Basic usage\n```python\nfrom aiomisc_entrypoint import Entrypoint\n\nep = Entrypoint()\nep.clear_environ()\nep.change_user()\nep.system_signals_listener()\nep.register_services_in_context()\nep.first_start_last_stop()\n\nep.run_forever()\n```\n\n\n## Extended usage\n\n```python\nfrom signal import SIGINT, SIGTERM, SIGKILL\nfrom aiomisc import Service\nfrom aiomisc_entrypoint import Entrypoint\n\nclass TestService(Service):\n    \n    async def start(self):\n        ...\n\n    \nasync def main():\n    ...\n\n\nservices = (\n    TestService(context_name='svc1'),\n    TestService(context_name='svc2'),\n)\n    \nep = Entrypoint(*services)\nep.clear_environ(lambda x: x.startwith('APP_'))\nep.change_user('user')\nep.system_signals_listener(SIGINT, SIGTERM, SIGKILL)\nep.register_services_in_context()\nep.first_start_last_stop()\n\nep.run_until_complete(main())\n```",
    'author': 'Vladislav Vorobyov',
    'author_email': 'vladislav.vorobyov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anysoft-kz/aiomisc-entrypoint',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
