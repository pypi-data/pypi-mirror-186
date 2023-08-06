# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tkutils',
 'tkutils.helpers',
 'tkutils.menu_builder',
 'tkutils.two_way_binding',
 'tkutils.two_way_binding.configuration',
 'tkutils.utilities']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0', 'typing-extensions>=4.4.0,<5.0.0']

entry_points = \
{'console_scripts': ['essai = project_debug:routing',
                     'main = tkutils.__main__:main']}

setup_kwargs = {
    'name': 'tkutils',
    'version': '1.0.0',
    'description': 'Python tkinter utilities.',
    'long_description': '# Welcome to TkUtils\n\n`tkutils` is a package offering some additional logic and syntactic sugar when using tkinter.\nThe main goal is to fill some gaps of tkinter, which might make it very annoying to use.\n\nOnline version of the help documentation: http://frederic.zinelli.gitlab.io/tkutils/\n\n\n\n## Features\n\n\n### Additional logic: two-way binding with [`Binder`](http://frederic.zinelli.gitlab.io/tkutils/binder/binder_overview/)\n\nThe [`Binder`](http://frederic.zinelli.gitlab.io/tkutils/binder/binder_overview/) class is an utility to setup a transparent two-way\nbinding reactivity between widgets and underlying object properties from the model/logic layer\nof the application.\n\nSeveral advantages come with this:\n\n* Changes of bound properties in the model layer are cascading in the GUI automatically.\n* The model layer of the application becomes (finally) totally independent from the presentation\n  layer. This means it becomes very easy to build and test the model layer, without any need to\n  think about its integration with `tkinter` itself.\n\n\n\n### Syntactic sugar\n\n\n#### [`GridLayout`](http://frederic.zinelli.gitlab.io/tkutils/grid_layout/grid_layout/)\n\nA grid layout manager which is abstracting away all the naughty `widget.grid(...)` calls and\nrows/columns grid configuration. Positioning widgets in the grid and controlling their "spanning"\nbecomes very easy, without extra typing.\n\n\n#### [`MenuBuilder`](http://frederic.zinelli.gitlab.io/tkutils/menu_builder/menu_builder/)\n\nA helper to build menus and to abstract away all the technicalities, when creating menus through\n`tkinter`, which quickly make the declarations very unclear. Using the [`MenuBuilder`](http://frederic.zinelli.gitlab.io/tkutils/menu_builder/menu_builder/),\nthe actual Menu hierarchy becomes very obvious: "what you see is what you get".\n\n\n#### [`Event`](http://frederic.zinelli.gitlab.io/tkutils/event/)\n\nAn utility to build event strings with autocompletion/IDE suggestions support.\n\n\n#### [`KeySym`](http://frederic.zinelli.gitlab.io/tkutils/key_sym/)\n\nAn utility to get all keysym informations with autocompletion/IDE suggestions (providing string,\nkeycode and keysym_num values).\n\n\n#### [`images`](http://frederic.zinelli.gitlab.io/tkutils/images/images/)\n\nVarious factories related to images to:\n\n* Simplify and reduce the syntaxes/typing needed,\n* Handle file conversions automatically,\n* Register automatically the image object on the host for the user (to avoid garbage collection).\n\n\n\n\n## Requirements\n\n- python 3.8+\n- Pillow\n\n\n\n## Installation\n\n* Through [PyPi](https://pypi.org/project/tkutils/):\n\n```bash\npip install tkutils\n```\n\n* Using an archive file (with the appropriate version number):\n\n```bash\npip install tkutils.1.0.2.tar.gz\n```\n\n* Cloning the [GitLab repository](https://gitlab.com/frederic.zinelli/tkutils).\n\n',
    'author': 'Frédéric Zinelli',
    'author_email': 'frederic.zinelli@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://frederic.zinelli.gitlab.io/tkutils/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
