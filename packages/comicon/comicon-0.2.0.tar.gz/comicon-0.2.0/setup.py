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
    'version': '0.2.0',
    'description': 'A simple comic conversion library between CBZ/EPUB/PDF',
    'long_description': '# Comicon\n\nComicon is a lightweight comic converter library between CBZ, PDF, and EPUB that preserves metadata. Once Comicon has converted a comic, it is **guaranteed** that the reverse conversion will restore the original comic with all of its original metadata.\n\n## Usage\n\n```python\nimport comicon\n\ncomicon.convert("comic.cbz", "comic.epub")\n```\n\n## Installation\n\nComicon is available from PyPI:\n\n```\npip install comicon\n```\n\n## Supported conversions\n\n| Format | Convert from? | Convert to? |\n| --- | --- | --- |\n| CBZ | :heavy_check_mark: | :heavy_check_mark: |\n| EPUB | :heavy_check_mark: | :heavy_check_mark: |\n| PDF | :heavy_check_mark: | :heavy_check_mark: |\n\n### Format discrepancies\n\n- Only EPUB supports a table of contents. CBZ and PDF will encode the table of contents so that it is restored upon converting to EPUB.\n- PDF does not support importing genre data due to a lack of library support. This may be worked around in the future.\n\n## Notes\n\nUnder the hood, Comicon converts each format into the **Comicon Intermediate Representation (CIR)** — more or less a strictly structured folder, which allows for many guarantees to be made for each input and output plugin. See `comicon.cirtools` for more information.\n\nFor new input and output formats to be added, they should be added in `comicon.inputs` or `comicon.outputs` respectively as a new module and in the `__init__.py` file(s).\n',
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
