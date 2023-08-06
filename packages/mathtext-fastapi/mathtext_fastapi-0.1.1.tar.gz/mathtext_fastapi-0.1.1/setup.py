# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.mathtext-fastapi']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.74.1,<0.75.0',
 'httpx>=0.23.3,<0.24.0',
 'matplotlib>=3.6.3,<4.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pytest>=7.2.1,<8.0.0',
 'requests>=2.28.2,<3.0.0',
 'sentencepiece>=0.1.97,<0.2.0',
 'spacy>=3.4.4,<4.0.0',
 'torch>=1.13.1,<2.0.0',
 'transformers>=4.25.1,<5.0.0',
 'uvicorn>=0.17.6,<0.18.0']

setup_kwargs = {
    'name': 'mathtext-fastapi',
    'version': '0.1.1',
    'description': '',
    'long_description': '---\ntitle: Mathtext Fastapi\nemoji: 🐨\ncolorFrom: blue\ncolorTo: red\nsdk: docker\npinned: false\nlicense: agpl-3.0\n---\n\nCheck out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference\n',
    'author': 'Cetin CAKIR',
    'author_email': 'cetincakirtr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
