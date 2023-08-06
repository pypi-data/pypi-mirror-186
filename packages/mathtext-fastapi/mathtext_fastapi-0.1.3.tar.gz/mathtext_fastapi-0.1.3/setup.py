# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.mathtext-fastapi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mathtext-fastapi',
    'version': '0.1.3',
    'description': '',
    'long_description': '---\ntitle: Mathtext Fastapi\nemoji: 🐨\ncolorFrom: blue\ncolorTo: red\nsdk: docker\npinned: false\nlicense: agpl-3.0\n---\n\nCheck out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference\n',
    'author': 'Cetin CAKIR',
    'author_email': 'cetincakirtr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
