# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edubot']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0',
 'pillow>=9.4.0,<10.0.0',
 'sqlalchemy[mypy]>=1.4.45,<1.5.0',
 'stability-sdk>=0.3.1,<0.4.0']

setup_kwargs = {
    'name': 'edubot',
    'version': '0.5.2',
    'description': '',
    'long_description': "# Edubot\n\nA self-improving AI-based chatbot library that is completely platform-agnostic.\n\nEdubot intuitively jumps into conversations to give advice, make jokes, and add to the discussion. Its personality can be completely customised to suit the tone of different rooms.\n\nBy simply reacting to messages with a thumbs up/down, users help Edubot collate feedback. This feedback is used to fine-tune the bot and improve its responses in the future.\n\nEdubot is still under active development and is the first project from [Open EdTech](https://openedtech.global).\n\n## Architecture\n1. Edubot integrations convert messages from external platforms into a standardised format.\n1. The library uses these messages to generate a response from GPT-3.\n1. Users send feedback to the bot's responses.\n1. Using the feedback, the library fine-tunes GPT-3's responses to better suit each thread it partakes in.\n\n![Edubot Architecture Diagram](docs/edubot.png)\n\n## Dev environment quickstart\n1. Install [Poetry](https://python-poetry.org/docs/)\n1. Install dependencies: `poetry install`\n1. Activate the env: `poetry shell`\n1. Install pre-commit hooks: `pre-commit install`\n1. Copy SAMPLE_CONFIG.ini and put your information in\n1. Set the `EDUBOT_CONFIG` env variable to wherever you put your config\n\nFor an example of an integration using this library see: [edubot-matrix](https://github.com/openedtech/edubot-matrix)\n",
    'author': 'exciteabletom',
    'author_email': 'tom@digitalnook.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
