# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfallback']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyfallback',
    'version': '0.1.0',
    'description': 'Provides fallback for operations in python',
    'long_description': '# pyfallback\n\n## Install\n> pip install fallback\n\n## Usage\n\n```python\nfrom pyfallback import Fallback\n\njson = {\n    \'attr-1\': \'value-1\',\n}\njson = Fallback(json, fallback="default")\n\n# fallback\njson["attr-1"].get()  # "value1"\njson["attr-2"].get()  # "default"\n\n# chaining\njson["attr-1"].split(\'-\')[0].get()  # "value"\n\n# see tests/test_fallback.py for more example \n```\n\n## Contributing\nJust submit a pull request :D <br />\nNote: this project uses poetry and pyenv\n',
    'author': 'Weilue Luo',
    'author_email': 'luoweilue@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/weilueluo/pyfallback',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
