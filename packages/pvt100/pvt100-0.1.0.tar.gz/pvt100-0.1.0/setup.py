# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pvt100']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pvt100',
    'version': '0.1.0',
    'description': 'VT100 terminal escape codes for Python',
    'long_description': '# pvt100\n\nA fistful of ANSI terminal escape codes for your terminal. \n\nThey\'re actually just ANSI escape codes, but I like to call them pvt100 because it sounds cooler.\n\nThese are all grouped under the name "ANSI escape codes", which is a bit\nmisleading, as ANSI is a standards body, and these are not all standards.\n\n## Usage\n\nEasiest to just read pvt100.py to see what constants are available, as well as `example.py` in this repo.\n\n```python\nimport pvt100\nprint(f"{pvt100.color_bg_blue} Hello, world! {pvt100.style_reset}")\n```\n\n\nSee also:\n- https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797\n- https://bluesock.org/~willg/dev/ansi.html#ansicodes\n\nFor fun:\n- https://xn--rpa.cc/irl/term.html\n- https://github.com/jart/cosmopolitan/blob/master/tool/build/lib/pty.c',
    'author': 'sina',
    'author_email': 'khalili@sfu.ca',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
