# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['func_hooks']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.6.2,<4.0.0', 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'func-hooks',
    'version': '1.1.1',
    'description': '',
    'long_description': '# Func hooks\n\nHooks for python functions.\n\n## Motivation:\n\nI am developing a system with a microservices architecture and I want to add event hooks to some methods.\n\nHowever, I don\'t want to add unrelated code to the busines logic methods. Because this, I developed this package, to be able to add execution points to a particular function.\n\n## Example usage:\n\n```python\n>>> import func_hooks\n>>> @func_hooks.hooks\n... def my_func():\n...     print("Ran my_func")\n...\n>>> @my_func.on_before\n... def _run_before(invocation):\n...     print("Running before my_func.")\n...\n>>> @my_func.on_after\n... def _run_before(invocation_result):\n...     print("Running after my_func.")\n...\n>>> my_func()\nRunning before my_func.\nRan my_func\nRunning after my_func.\n>>>\n```\n',
    'author': 'Francisco Del Roio',
    'author_email': 'francipvb@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
