# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oneshot_channel']

package_data = \
{'': ['*']}

install_requires = \
['babichjacob-option-and-result>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'babichjacob-oneshot-channel',
    'version': '0.1.0',
    'description': 'TODO',
    'long_description': '<h1 align="center">1️⃣ One-Shot Channel</h1>\n\nThis library uses documentation copied and pasted from [Tokio\'s `sync::oneshot` library](https://docs.rs/tokio/latest/tokio/sync/oneshot/index.html), which they have generously published under the MIT license. 🙏\n\nThis is a Python implementation of [their one-shot channel](https://docs.rs/tokio/latest/tokio/sync/oneshot/fn.channel.html).\n\n## 💻 Installation\n\nThis package is [published to PyPI as `babichjacob-oneshot-channel`](https://pypi.org/project/babichjacob-oneshot-channel/).\n\n## 🛠 Usage\n\n```py\nfrom asyncio import create_task, gather, run, sleep\nfrom itertools import count\n\nfrom oneshot_channel import oneshot_channel, Receiver, Sender\n\n# TODO: write usage guidance\n```\n\n## 😵 Help! I have a question\n\nCreate an issue and I\'ll try to help.\n\n## 😡 Fix! There is something that needs improvement\n\nCreate an issue or pull request and I\'ll try to fix.\n\n## 📄 License\n\nMIT\n\n## 🙏 Attribution\n\n_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_\n',
    'author': 'J or Jacob Babich',
    'author_email': 'jacobbabichpublic+git@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/babichjacob/python-oneshot-channel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
