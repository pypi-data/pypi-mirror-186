# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'lib'}

packages = \
['fastapiccache']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fastapiccache',
    'version': '0.1.0',
    'description': '',
    'long_description': '\n# fastapicache\nfastapicache is a package that privde simple and fast caching system for the fastapi package\n\n\n## usage\n\n### fast and simple\n\n```py\nimport time \nfrom fastapi import FastAPI\nfrom fastapicache import fastapicache\n\n\napp = FastAPI()\n\n\n@app.get(\'/\')\n@fastapicache(revalidate=0)\nasync def index(name: str = "unknown"):\n    time.sleep(4)\n    return f"{name}: hello world"\n```\n\n',
    'author': 'Daniel Sonbolian',
    'author_email': 'dsal3389@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
