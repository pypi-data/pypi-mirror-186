# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spiel', 'spiel.demo', 'spiel.renderables', 'spiel.screens', 'spiel.widgets']

package_data = \
{'': ['*']}

install_requires = \
['more-itertools>=9',
 'pillow>=8',
 'rich>=13.2',
 'textual>=0.10.0',
 'typer>=0.6',
 'watchfiles>=0.18']

entry_points = \
{'console_scripts': ['spiel = spiel.cli:cli']}

setup_kwargs = {
    'name': 'spiel',
    'version': '0.4.6',
    'description': 'A framework for building and presenting richly-styled presentations in your terminal using Python.',
    'long_description': '# Spiel\n\n[![PyPI](https://img.shields.io/pypi/v/spiel)](https://pypi.org/project/spiel)\n[![PyPI - License](https://img.shields.io/pypi/l/spiel)](https://pypi.org/project/spiel)\n[![Docs](https://img.shields.io/badge/docs-exist-brightgreen)](https://www.spiel.how)\n\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/JoshKarpel/spiel/main.svg)](https://results.pre-commit.ci/latest/github/JoshKarpel/spiel/main)\n[![codecov](https://codecov.io/gh/JoshKarpel/spiel/branch/main/graph/badge.svg?token=2sjP4V0AfY)](https://codecov.io/gh/JoshKarpel/spiel)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n[![GitHub issues](https://img.shields.io/github/issues/JoshKarpel/spiel)](https://github.com/JoshKarpel/spiel/issues)\n[![GitHub pull requests](https://img.shields.io/github/issues-pr/JoshKarpel/spiel)](https://github.com/JoshKarpel/spiel/pulls)\n\n[Spiel](https://dictionary.cambridge.org/us/dictionary/english/spiel) is a framework for building and presenting\n[richly-styled](https://github.com/Textualize/rich) presentations in your terminal using Python.\n\nTo see what Spiel can do without installing it, you can view the demonstration deck in a container:\n```bash\n$ docker run -it --rm ghcr.io/joshkarpel/spiel\n```\nAlternatively, install Spiel (`pip install spiel`) and run this command to view the demonstration deck:\n```bash\n$ spiel demo present\n```\n\n![The first slide of the demo deck](https://raw.githubusercontent.com/JoshKarpel/spiel/main/docs/assets/demo.svg)\n![The demo deck in "deck view"](https://raw.githubusercontent.com/JoshKarpel/spiel/main/docs/assets/deck.svg)\n\n## Quick Start\n\nIf you want to jump right in,\ninstall Spiel (`pip install spiel`),\ncreate a file called `deck.py`,\nand copy this code into it:\n```python\nfrom rich.console import RenderableType\n\nfrom spiel import Deck, present\n\ndeck = Deck(name="Your Deck Name")\n\n\n@deck.slide(title="Slide 1 Title")\ndef slide_1() -> RenderableType:\n    return "Your content here!"\n\n\nif __name__ == "__main__":\n    present(__file__)\n```\n\nThat is the most basic Spiel presentation you can make.\nTo present the deck, run `python deck.py`.\nYou should see:\n\n![Barebones slide](https://raw.githubusercontent.com/JoshKarpel/spiel/main/docs/assets/quickstart_basic.svg)\n\nCheck out the [Quick Start tutorial](https://www.spiel.how/quickstart) to continue!\n\n## Documentation\n\nTo learn more about Spiel, take a look at the [documentation](https://www.spiel.how).\n\n## Contributing\n\nIf you\'re interested in contributing to Spiel, check out the [Contributing Guide](https://www.spiel.how/contributing/).\n',
    'author': 'JoshKarpel',
    'author_email': 'josh.karpel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JoshKarpel/spiel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4',
}


setup(**setup_kwargs)
