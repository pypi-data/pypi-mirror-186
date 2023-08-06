# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mypydot', 'mypydot.src', 'mypydot.src.view']

package_data = \
{'': ['*'],
 'mypydot': ['template/*',
             'template/config/docker/*',
             'template/config/editors/*',
             'template/config/editors/vim/*',
             'template/config/git/*',
             'template/language/*',
             'template/language/go/*',
             'template/language/java/*',
             'template/language/python/*',
             'template/os/*',
             'template/shell/*']}

install_requires = \
['PyTermGUI>=7.3.0,<8.0.0', 'PyYAML==6.0', 'emoji>=2.2.0,<3.0.0']

entry_points = \
{'console_scripts': ['mypydot = mypydot.src.main:entry_point']}

setup_kwargs = {
    'name': 'mypydot',
    'version': '2023.0.1',
    'description': 'Python package to manage your dotfiles',
    'long_description': '[![PyPI version](https://badge.fury.io/py/mypydot.svg)](https://badge.fury.io/py/mypydot)\n![CI](https://github.com/andres-ortizl/mypydot/actions/workflows/main.yml/badge.svg)\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=mypydot&metric=coverage)](https://sonarcloud.io/summary/new_code?id=mypydot)\n[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mypydot&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mypydot)\n\n## Mypydot\n\nMypydot is a tool created for managing your dotfiles using a Python application\n\n## Showcase\n\nsmall screenshots of the application\n\n|                                           |                                         |\n|-------------------------------------------|-----------------------------------------|\n| ![Home](screenshots/home.png)             | ![selection](screenshots/selection.png) |\n| ![Installing](screenshots/installing.png) | ![Bye](screenshots/bye.png)             |\n\n# Motivation\n\nI just wanted the basic functionality to manage my own dotfiles. I decided to do it in Python because It seems more\nnatural\nto me rather than do It using shell scripting.\n\n## Install\n\n```pip install mypydot```\n\n## Instructions\n\n### Create new dotfiles\n\nUsing it for the first time : ```mypydot``` . This command will create a new folder called .mypydotfiles\nin your $HOME directory. In this folder you will find the following folder structure :\n\n| Folder     |                                                                                                                               |\n|------------|-------------------------------------------------------------------------------------------------------------------------------|\n| `language` | In case you want to save some dotfiles related with your favourite programming languages                                      |\n| `os`       | Operating system dotfiles                                                                                                     |\n| `shell`    | Small setup of aliases and exports that can be accessed from everywhere                                                       |\n| `config`   | Docker, Git, Editors, etc. You can also find here a few almost empty scripts for storing your aliases, exports and functions. |\n| `conf.yml` | This file contains every file that you want to track in your dotfiles repository, feel free to add & remove symlinks !        |\n\nOnce you run this process you will notice that you have a few new lines your .bashrc and in your .zshrc\n\n```\nexport MYPYDOTFILES=/Users/username/.mypydotfiles\nsource $MYPYDOTFILES/shell/main.sh\n```\n\nThis lines will be used to source yours aliases, exports and functions to be available in your terminal.\nBesides that, nothing else is edited.\n\n### Resync dotfiles\n\nSelect your existing conf file and the modules you want to resync / install\n\n# References\n\nhttps://github.com/mathiasbynens/dotfiles\n\nhttps://github.com/CodelyTV/dotly\n\nhttps://github.com/denisidoro/dotfiles\n\nhttps://github.com/webpro/awesome-dotfiles\n\nThank you!\n',
    'author': 'Andrés Ortiz',
    'author_email': 'andrs.ortizl@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/andres-ortizl/mypydot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11.1,<4.0.0',
}


setup(**setup_kwargs)
