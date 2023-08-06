# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chatsonic']

package_data = \
{'': ['*']}

install_requires = \
['bumpver>=2022.1120,<2023.0', 'twine>=4.0.2,<5.0.0']

setup_kwargs = {
    'name': 'chatsonic',
    'version': '0.1.1',
    'description': 'ChatGPT Alternative API with real time superpowers',
    'long_description': '\n# ChatSonic API, (Scalable ChatGPT Alternative with real time data) \n\n\n\nChatSonic\'s Python SDK is the perfect solution for anyone looking to integrate an AI-powered Chatbot into their Python-based codebase. With real-time Google data support and a powerful engine that surpasses ChatGPT, ChatSonic\'s Python SDK is the perfect AI assistant and conversation partner. Easily access the power of ChatGPT API with this SDK and make your codebases smarter than ever. With ChatSonic\'s Python SDK, you can take your project to the next level.\n\n\n\n## License\n\n\n[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)\n## Installation \n\n``` pip install chatsonic-py ```\n\n\n## Usage :\n\n\n```Python\nfrom chatsonic import Conversation\n\nchatsonic = Conversation(api_key="your-key-here",enable_memory=True)\nreply = chatsonic.send_message(message="Hello")\nprint(reply)\n\n```\n\n\n\n## Documentation\n\n[Documentation](https://linktodocumentation)\n\n\n## Feedback\n\nIf you have any feedback, please reach out to us at support@writesonic.com\n\n',
    'author': 'Gupta-Anubhav12',
    'author_email': 'anubhavgupta2260@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
