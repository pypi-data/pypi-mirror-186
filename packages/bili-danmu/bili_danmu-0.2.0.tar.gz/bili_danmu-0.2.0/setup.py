# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['danmu']

package_data = \
{'': ['*']}

install_requires = \
['brotlipy>=0.7.0,<0.8.0', 'websockets>=10.4,<11.0']

setup_kwargs = {
    'name': 'bili-danmu',
    'version': '0.2.0',
    'description': 'A modern library for receiving danmu from bilibili livestream',
    'long_description': "# bili-danmu\n\nA modern library for receiving danmu from bilibili livestream, with full asynchronous support.\n\nNOTICE: It's a simple implement, so IT DOES NOT INCLUDE PARSEING DANMU FEATURES. You need to parse the danmu dict mannually.\n\n# Installation\n\nJust execute `pip install bili-danmu`\n\n# Example\n\n```python\nimport asyncio\nfrom danmu import DanmuClient\n\nloop = asyncio.new_event_loop()\ndmc = DanmuClient(25512465)\n\n@dmc.on_danmu\nasync def on_danmu(danmu: dict):\n    print(danmu)\n\ndmc.run(loop)\n```\n\n# Special Thanks\n\nThis project refers to some other projects. Sincerely appreciate their developers.\n\n- [Code4Epoch/Bolaris](https://github.com/Code4Epoch/Bolaris) Give me the infomation of v3 protocol\n\n- [qydysky/bili_danmu](https://github.com/qydysky/bili_danmu) A full list of CMD in danmu pack's body\n\n- [littlecodersh/danmu](https://github.com/littlecodersh/danmu) A very old danmu library. Inspire me to use callback design\n\n- [yjqiang/danmu](https://github.com/yjqiang/danmu) Main reference \n\n- [yangjunlong/barrager.js](https://github.com/yangjunlong/barrager.js) A protocol document and code implement\n",
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
