# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rousquille_tools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rousquille-tools',
    'version': '0.1.0',
    'description': 'My personal toolbox',
    'long_description': "# Rousquille's tools\n\nMy personal toolbox 🛠\n\n## Python 🐍\n\n<details><summary>Measurement of the time used by a function</summary>\n<p>\n\n```py\nimport time\nfrom rousquille_tools.decorators import time_def\n\n\n@time_def\ndef func1():\n    time.sleep(5)\n```\nResult:\n```py\n>>> func1()\n[time_def] Function: func1 Time: 5.0s\n```\n\n\n</p>\n</details>\n\n\n",
    'author': 'Fabien ROSSA',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
