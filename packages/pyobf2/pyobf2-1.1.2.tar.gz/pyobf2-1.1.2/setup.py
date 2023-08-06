# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyobf2', 'pyobf2.lib', 'pyobf2.lib.transformers']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.6,<0.5.0',
 'pycryptodome>=3.16.0,<4.0.0',
 'rich>=13.1.0,<14.0.0',
 'tomlkit>=0.11.6,<0.12.0']

entry_points = \
{'console_scripts': ['pyobf2 = pyobf2:main']}

setup_kwargs = {
    'name': 'pyobf2',
    'version': '1.1.2',
    'description': 'An in-place obfuscator for python 3.11',
    'long_description': '# PyObf 2\n\nA "continuation" of sorts of the old, private pyobf.\n\n## Installing\nThe package now has a pypi! https://pypi.org/project/pyobf2/\n\nInstall with `python3 -m pip install pyobf2`\n\n## Usage\n\nThis is the **api** section of the obfuscator. You won\'t find the executable here.\n\nThe obfuscator has an API, to allow you to integrate it into your own projects. For example, it can be used to obfuscate the output of a code generator automatically. An example of this API being used can be seen in `api_example.py`. If you end up using the API, please credit this repository.\n\n## API usage\nAs previously mentioned, the `api_example.py` file contains examples on how the api works. Some notes are required, though:\n- When obfuscating multiple files that depend on each other, use `do_obfuscation_batch_ast`, instead of calling `do_obfuscation_single_ast` on all of them separately. This will allow the obfuscator to draw conclusions on which file depends on which other file, and allows it to understand the structure between them.\n- `do_obfuscation_batch_ast` is a generator. It will progressively yield each step it does, to allow for progress bar rendering. It will do nothing when not iterated through.\n- Some transformers (eg. `packInPyz`, `compileFinalFiles`) only act on the **output files** of the obfuscation process, and do nothing in the standard run. To invoke them, use `do_post_run`. This will require you to write the obfuscated AST into a file, though.\n\n## Feedback & bugs\n\nThe obfuscator is in no way perfect as of now, so feedback is encouraged. Please tell me how bad my code is in the\nissues tab.',
    'author': '0x150',
    'author_email': '99053360+0x3C50@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
