# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['comicon', 'comicon.inputs', 'comicon.outputs']

package_data = \
{'': ['*']}

install_requires = \
['ebooklib>=0.18,<0.19',
 'lxml>=4.9.2,<5.0.0',
 'pillow>=9.4.0,<10.0.0',
 'pypdf[image]>=3.2.1,<4.0.0']

setup_kwargs = {
    'name': 'comicon',
    'version': '0.1.1',
    'description': 'A simple comic conversion library between CBZ/EPUB/PDF',
    'long_description': '# Comicon\n\nComicon is a lightweight comic converter library between CBZ, PDF, and EPUB.\n\n## Usage\n\n```python\nimport comicon\n\ncomicon.convert("comic.cbz", "comic.epub")\n```\n\n## Installation\n\nComicon is available from PyPI:\n\n```\npip install comicon\n```\n\n## Supported conversions\n\n| Format | Convert from? | Convert to? |\n| --- | --- | --- |\n| CBZ | :heavy_check_mark: | :heavy_check_mark: |\n| EPUB | :heavy_check_mark: | :heavy_check_mark: |\n| PDF | :heavy_check_mark: | :heavy_check_mark: |\n',
    'author': 'Daniel Chen',
    'author_email': 'danielchen04@hotmail.ca',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/potatoeggy/comicon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
