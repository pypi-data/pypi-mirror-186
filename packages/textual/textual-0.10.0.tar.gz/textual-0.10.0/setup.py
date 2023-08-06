# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['textual',
 'textual.cli',
 'textual.cli.previews',
 'textual.cli.tools',
 'textual.css',
 'textual.devtools',
 'textual.drivers',
 'textual.layouts',
 'textual.renderables',
 'textual.widgets']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.11.3,<5.0.0', 'nanoid>=2.0.0', 'rich>12.6.0']

extras_require = \
{':python_version < "3.10"': ['typing-extensions>=4.0.0,<5.0.0'],
 'dev': ['aiohttp>=3.8.1', 'click>=8.1.2', 'msgpack>=1.0.3']}

entry_points = \
{'console_scripts': ['textual = textual.cli.cli:run']}

setup_kwargs = {
    'name': 'textual',
    'version': '0.10.0',
    'description': 'Modern Text User Interface framework',
    'long_description': '# Textual\n\n![Textual splash image](https://raw.githubusercontent.com/Textualize/textual/main/imgs/textual.png)\n\nTextual is a Python framework for creating interactive applications that run in your terminal.\n\n<details>  \n  <summary> 🎬 Demonstration </summary>\n  <hr>\n  \nA quick run through of some Textual features.\n  \n\n\nhttps://user-images.githubusercontent.com/554369/197355913-65d3c125-493d-4c05-a590-5311f16c40ff.mov\n\n\n\n </details>\n\n\n\n## About\n\nTextual adds interactivity to [Rich](https://github.com/Textualize/rich) with a Python API inspired by modern web development.\n\nOn modern terminal software (installed by default on most systems), Textual apps can use **16.7 million** colors with mouse support and smooth flicker-free animation. A powerful layout engine and re-usable components makes it possible to build apps that rival the desktop and web experience. \n\n## Compatibility\n\nTextual runs on Linux, macOS, and Windows. Textual requires Python 3.7 or above.\n\n## Installing\n\nInstall Textual via pip:\n\n```\npip install "textual[dev]"\n```\n\nThe addition of `[dev]` installs Textual development tools. See the [docs](https://textual.textualize.io/getting_started/) if you need help getting started.\n\n## Demo\n\nRun the following command to see a little of what Textual can do:\n\n```\npython -m textual\n```\n\n![Textual demo](https://raw.githubusercontent.com/Textualize/textual/main/imgs/demo.png)\n\n## Documentation\n\nHead over to the [Textual documentation](http://textual.textualize.io/) to start building!\n\n## Examples\n\nThe Textual repository comes with a number of examples you can experiment with or use as a template for your own projects.\n\n\n<details>\n  <summary> 🎬 Code browser </summary>\n  <hr>\n\n  This is the [code_browser.py](https://github.com/Textualize/textual/blob/main/examples/code_browser.py) example which clocks in at 61 lines (*including* docstrings and blank lines).\n\nhttps://user-images.githubusercontent.com/554369/197188237-88d3f7e4-4e5f-40b5-b996-c47b19ee2f49.mov\n\n </details>\n\n\n<details>  \n  <summary> 📷 Calculator </summary>\n  <hr>\n  \nThis is [calculator.py](https://github.com/Textualize/textual/blob/main/examples/calculator.py) which demonstrates Textual grid layouts.\n  \n![calculator screenshot](https://raw.githubusercontent.com/Textualize/textual/main/imgs/calculator.png)\n</details>\n\n\n<details>\n  <summary> 🎬 Stopwatch </summary>\n  <hr>\n\n  This is the Stopwatch example from the [tutorial](https://textual.textualize.io/tutorial/).\n  \n\n\nhttps://user-images.githubusercontent.com/554369/197360718-0c834ef5-6285-4d37-85cf-23eed4aa56c5.mov\n\n\n\n</details>\n\n\n\n## Reference commands\n\nThe `textual` command has a few sub-commands to preview Textual styles.\n\n<details>  \n  <summary> 🎬 Easing reference </summary>\n  <hr>\n  \nThis is the *easing* reference which demonstrates the easing parameter on animation, with both movement and opacity. You can run it with the following command:\n  \n```bash\ntextual easing\n```\n\n\nhttps://user-images.githubusercontent.com/554369/196157100-352852a6-2b09-4dc8-a888-55b53570aff9.mov\n\n\n </details>\n\n<details>  \n  <summary> 🎬 Borders reference </summary>\n  <hr>\n  \nThis is the borders reference which demonstrates some of the borders styles in Textual. You can run it with the following command:\n  \n```bash\ntextual borders\n```\n\n\nhttps://user-images.githubusercontent.com/554369/196158235-4b45fb78-053d-4fd5-b285-e09b4f1c67a8.mov\n\n  \n</details>\n\n\n<details>  \n  <summary> 🎬 Colors reference </summary>\n  <hr>\n  \nThis is a reference for Textual\'s color design system.\n  \n```bash\ntextual colors\n```\n\n\n\nhttps://user-images.githubusercontent.com/554369/197357417-2d407aac-8969-44d3-8250-eea45df79d57.mov\n\n\n\n  \n</details>\n\n',
    'author': 'Will McGugan',
    'author_email': 'will@textualize.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Textualize/textual',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
