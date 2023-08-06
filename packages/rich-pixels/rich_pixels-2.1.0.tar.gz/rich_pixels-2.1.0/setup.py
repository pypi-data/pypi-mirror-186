# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich_pixels']

package_data = \
{'': ['*']}

install_requires = \
['pillow>=9.0.0,<10.0.0', 'rich>=12.0.0']

setup_kwargs = {
    'name': 'rich-pixels',
    'version': '2.1.0',
    'description': 'A Rich-compatible library for writing pixel images and ASCII art to the terminal.',
    'long_description': '# Rich Pixels\n\nA Rich-compatible library for writing pixel images and other colourful grids to the\nterminal.\n\n<p align="center">\n<img width="700" src="https://user-images.githubusercontent.com/5740731/200676207-8e9c9465-628b-40de-ba0b-410612f2bd7c.svg" />\n</p>\n\n## Installation\n\nGet `rich-pixels` from PyPI.\n\n```\npip install rich-pixels\n```\n\n## Basic Usage\n\n### Images\n\n#### Image from a file\n\nYou can load an image file from a path using `from_image_path`:\n\n```python\nfrom rich_pixels import Pixels\nfrom rich.console import Console\n\nconsole = Console()\npixels = Pixels.from_image_path("pokemon/bulbasaur.png")\nconsole.print(pixels)\n```\n\n#### Pillow image object\n\nYou can create a PIL image object yourself and pass it in to `from_image`.\n\n```python\nfrom rich_pixels import Pixels\nfrom rich.console import Console\nfrom PIL import Image\n\nconsole = Console()\n\nwith Image.open("path/to/image.png") as image:\n    pixels = Pixels.from_image(image)\n\nconsole.print(pixels)\n```\n\nUsing this approach means you can modify your PIL `Image` beforehard.\n\n#### ASCII Art\n\nYou can quickly build shapes using a tool like [asciiflow](https://asciiflow.com), and\napply styles the ASCII characters. This provides a quick way of sketching out shapes.\n\n```python\nfrom rich_pixels import Pixels\nfrom rich.console import Console\n\nconsole = Console()\n\n# Draw your shapes using any character you want\ngrid = """\\\n     xx   xx\n     ox   ox\n     Ox   Ox\nxx             xx\nxxxxxxxxxxxxxxxxx\n"""\n\n# Map characters to different characters/styles\nmapping = {\n    "x": Segment(" ", Style.parse("yellow on yellow")),\n    "o": Segment(" ", Style.parse("on white")),\n    "O": Segment(" ", Style.parse("on blue")),\n}\n\npixels = Pixels.from_ascii(grid, mapping)\nconsole.print(pixels)\n```\n\n### Using with Textual\n\n`Pixels` can be integrated into [Textual](https://github.com/Textualize/textual)\napplications just like any other Rich renderable.\n',
    'author': 'Darren Burns',
    'author_email': 'darrenb900@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
