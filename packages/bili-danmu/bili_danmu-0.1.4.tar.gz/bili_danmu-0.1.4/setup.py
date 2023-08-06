# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['danmu']

package_data = \
{'': ['*']}

install_requires = \
['websockets>=10.4,<11.0']

setup_kwargs = {
    'name': 'bili-danmu',
    'version': '0.1.4',
    'description': 'A modern library for receiving danmu from bilibili livestream',
    'long_description': "# bili-danmu\n\nA modern library for receiving danmu from bilibili livestream, with full asynchronous support.\n\nNOTICE: It's a simple implement, so IT DOES NOT INCLUDE PARSEING DANMU FEATURES. You need to parse the danmu dict mannually.\n\n# Installation\n\nJust execute `pip install bili-danmu`\n\n# Example\n\n```python\nimport asyncio\nfrom danmu import DanmuClient\n\nloop = asyncio.new_event_loop()\ndmc = DanmuClient(25512465)\n\n@dmc.on_danmu\nasync def on_danmu(danmu: dict):\n    print(danmu)\n\ndmc.run(loop)\n```\n",
    'author': 'WorldObservationLog',
    'author_email': 'wolc@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
