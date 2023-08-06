# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xwordlist']

package_data = \
{'': ['*']}

install_requires = \
['anyascii>=0.3.1,<0.4.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'configargparse>=1.5.3,<2.0.0',
 'prompt-toolkit>=3.0.20,<4.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['xwl = xwordlist.xwordlist:main',
                     'xwordlist = xwordlist.xwordlist:main']}

setup_kwargs = {
    'name': 'xwordlist',
    'version': '23.0.0',
    'description': 'Software to help create, build and organize crossword puzzle word lists',
    'long_description': '# xwordlist\n\n`xwordlist` is a command line Python program designed to help you create, build and organize crossword puzzle word lists. As I started to think about constructing crossword puzzles with heavy themes — trying to make the entire puzzle themed, not just three or four long entries — I realized that I would need the ability to acquire and organize large amounts of text on very specific topics. After hacking around with a combination of search-and-replace text editors and Excel, I realized I needed to build someting more custom and thus `xwordlist` was born. \n\nBesides helping with basic text functions such as deduping, alphabetizing and changing case, this program is able to pull content out of structured web pages and parse large blocks of text, including lists of web pages with similarly structured content. Although I first started using the software to grab the lyrics of songs, I have added regex and better html parsing functionality to make it easier to get data from Wikipedia and less structured sites.\n\nFor more information, see the project’s main website hosted at [xwl.ist](https://xwl.ist). For an example of a themed 5x5 mini puzzle built with a word list assembled using this software, see [my personal website](https://quid.pro/xwords/tom-petty-mini/). For one of the original inspirations for this project, see Malaika Handa’s [Crosswift](https://www.7xwords.com/daily/01/01-13.html) puzzle using only Taylor Swift’s lyrics.\n\n## Installation\n\nIt helps to have some familiarity with Python and terminal programs to install `xwordlist` but it is not a requirement. If your environment is all set up and you know `pip` is both installed and up-to-date, skip down to the `pip` instructions below. Most Macs and Linux users will find that `pip` is installed but probably needs to be updated. Most Windows users will need to install `pip` first (see [Windows Special Instructions](#windows-special-instructions) below). In other words, unless you really know what you are doing, you probably need to continue to follow the next paragraph or the special Windows instructions.\n\nSearch for `terminal` and your operating system should show you the name and how to launch your default terminal program. The first thing you will need to do is make sure your Python is up-to-date (required) and that you have activated a virtual environment (recommended). See [Installing Python Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/) for helpful instructions on how to do both as well as how to install and upgrade `pip`. Follow the instructions on that page down to the section labeled *Installing from PyPI*.\n\nFrom there, you can install `xwordlist` by typing\n\n```\npip install xwordlist\n```\nBe sure to type `xwordlist` as there is other software called `wordlist` (without the “x”) which is not what you want. To see if your installation was successful, type\n```\nxwordlist --version\n```\nIf properly installed, the software should respond with its name and the installed version.\n\n### Windows Special Instructions\n\nRegardless of whether Python is already installed on your Windows computer, I would highly recommend a fresh install of an up-to-date version from [Python.org’s Windows downloads page](https://www.python.org/downloads/windows/). In the *Stable Releases* column are a number of Windows installers that are compatible with versions of Windows going back to XP and compatible with 32-bit and 64-bit Intel machines or 64-bit ARM. Find the most recent version of Python that is compatbile with your version of Windows and the type of processor you have and download that.\n\nWhen you launch the installer, select “Customize Installation” and make sure the boxes next to “Pip” and “Py launcher” are selected. Hit the “Next” button and make sure the boxes next to both “Create shortcuts for installed applications” and “Add Python to environment variables” are selected. Finally, hit the “Install” button.\n\nFrom there, you should be able to follow the original instructions above by typing\n\n`pip install xwordlist`\n\n### Manual Installation\n\nTo install the software manually, copy the `xwordlist` code to your local working environment by either cloning this repository or downloading and unpacking the [zip archive](https://github.com/aanker/xwordlist/archive/refs/heads/main.zip) into a new directory. To install the dependencies required to make `xwordlist` work, use your terminal program to find the directory in which you have copied the files and type\n\n```\npython3 -m pip install -r requirements.txt\n```\nTo see if your installation was successful, type\n```\npython3 xwordlist.py --version\n```\nIf properly installed, the software should respond with its name and the installed version.\n\n## Usage\n\nIf you have installed the software using `pip`, you should be able to run the program by simply typing `xwordlist` or `xwl`. For manual installs, you will need to type `python3 xwordlist.py`. The rest of the documentation assumes you have installed via `pip` and uses the short form.\n\nFor quick help instructions on the command line, type\n```\nxwordlist --help\n```\nPlease see the [project’s main website](https://xwl.ist) for more information about using the software including a [basic example](https://xwl.ist/help/#basic-example), [recipes for common patterns](https://xwl.ist/resources/#recipes) and a [reference](https://xwl.ist/help/#list-of-available-options) to all options.\n\nFind a bug? Please let us know [here](https://github.com/aanker/xwordlist/issues).\n\n## License\n\nThis software is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).\n',
    'author': 'Andrew Anker',
    'author_email': 'aa@quid.pro',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://xwl.ist',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
