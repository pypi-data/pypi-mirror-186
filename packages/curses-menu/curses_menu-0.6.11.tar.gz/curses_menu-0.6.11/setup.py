# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cursesmenu', 'cursesmenu.items']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.13,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.7.0'],
 ':sys_platform == "win32"': ['windows-curses>=2.3.1,<3.0.0']}

setup_kwargs = {
    'name': 'curses-menu',
    'version': '0.6.11',
    'description': 'A simple console menu system using curses',
    'long_description': '|Build Status|\\ |Documentation Status|\\ |Coverage Status|\n\ncurses-menu\n===========\n\nA simple Python menu-based GUI system on the terminal using curses.\nPerfect for those times when you need a GUI, but don’t want the overhead\nor learning curve of a full-fledged GUI framework. However, it\'s also\nflexible enough to do cool stuff like on-the-fly changing of menus and is extensible to\na large variety of uses.\n\nhttp://curses-menu.readthedocs.org/en/latest/\n\n.. image:: ./images/curses-menu_screenshot1.png\n\n\nInstallation\n~~~~~~~~~~~~\n\nTested on Python 3.7+ pypy and pypy3.\n\nThe curses library comes bundled with python on Linux and MacOS. Windows\nusers can visit http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses and\nget a third-party build for your platform and Python version.\n\nThen just run\n\n.. code:: shell\n\n   pip install curses-menu\n\nUsage\n-----\n\nIt’s designed to be pretty simple to use. Here’s an example\n\n.. code:: python\n\n    menu = CursesMenu("Root Menu", "Root Menu Subtitle")\n    item1 = MenuItem("Basic item that does nothing", menu)\n    function_item = FunctionItem("FunctionItem, get input", input, ["Enter an input: "])\n    print(__file__)\n    command_item = CommandItem(\n        "CommandItem that opens another menu",\n        f"python {__file__}",\n    )\n\n    submenu = CursesMenu.make_selection_menu([f"item{x}" for x in range(1, 20)])\n    submenu_item = SubmenuItem("Long Selection SubMenu", submenu=submenu, menu=menu)\n\n    submenu_2 = CursesMenu("Submenu Title", "Submenu subtitle")\n    function_item_2 = FunctionItem("Fun item", input, ["Enter an input"])\n    item2 = MenuItem("Another Item")\n    submenu_2.items.append(function_item_2)\n    submenu_2.items.append(item2)\n    submenu_item_2 = SubmenuItem("Short Submenu", submenu=submenu_2, menu=menu)\n\n    menu.items.append(item1)\n    menu.items.append(function_item)\n    menu.items.append(command_item)\n    menu.items.append(submenu_item)\n    menu.items.append(submenu_item_2)\n\n    menu.start()\n    _ = menu.join()\n\nTesting Information\n-------------------\n\nCurrently the platforms I\'m manually testing on are MacOS in iTerm2 on zsh with and without TMUX and Windows 10\\\nwith both powersehll and cmd.exe in and out of Windows Terminal. If a bug pops up on another configuration, \\\nno promises that I\'ll be able to reproduce it.\n\n.. |Build Status| image:: https://github.com/pmbarrett314/curses-menu/actions/workflows/github-action-tox.yml/badge.svg\n   :target: https://github.com/pmbarrett314/curses-menu/actions/workflows/github-action-tox.yml/badge.svg\n.. |Documentation Status| image:: https://readthedocs.org/projects/curses-menu/badge/?version=latest\n   :target: http://curses-menu.readthedocs.org/en/latest/?badge=latest\n.. |Coverage Status| image:: https://coveralls.io/repos/github/pmbarrett314/curses-menu/badge.svg?branch=develop\n   :target: https://coveralls.io/github/pmbarrett314/curses-menu?branch=develop\n',
    'author': 'Paul Barrett',
    'author_email': 'pmbarrett314@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/pmbarrett314/curses-menu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
