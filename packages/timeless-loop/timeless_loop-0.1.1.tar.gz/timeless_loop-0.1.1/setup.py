# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timeless_loop']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'timeless-loop',
    'version': '0.1.1',
    'description': '',
    'long_description': "# timeless_loop\n\ntimeless_loop is a Python library that provides a custom asyncio event loop, allowing you to freeze time and avoid pesky delays while writing or testing async code. It does so by defining a subclass of the built-in `SelectorEventLoop`, which behaves nearly identically to the real one. It differs in that it does not actually wait for any time to pass; instead, it simply advances the loop's internal clock to the exact time of execution of the next scheduled callback when there are no immediately ready loop callbacks available. \n\nIn addition, timeless_loop has the ability to detect and raise an exception when deadlocks occur in asyncio code. This helps to prevent your program from getting stuck in an infinite loop and allows you to easily track down and fix any issues. This is experimental, and thus subject to bugs. It is disabled by default.\n\n## Installation\n\ntimeless_loop is available on PyPI and can be installed with `poetry`, `pip`, or your favorite package manager.\n\n```bash\npip install timeless_loop\n```\n\n## Usage\n\nThe recommended way of setting the TimelessEventLoop is through setring the loop policy with `asyncio.set_event_loop_policy`. It can be used as follows:\n\n```python\nimport asyncio\nfrom timeless_loop import TimelessEventLoopPolicy\n\nasync def main():\n    # code here will run on the TimelessEventLoop\n    pass\n\nasyncio.set_event_loop_policy(TimelessEventLoopPolicy(raise_on_deadlock=False))\nasyncio.run(main())\n\n```\n\nAlternatively, you can directly create and use a `TimelessEventLoop` instance:\n\n```python\nimport asyncio\nfrom timeless_loop import TimelessEventLoop\n\nasync def main():\n    # code here will run on the TimelessEventLoop\n    pass\n\nloop = TimelessEventLoop(raise_on_deadlock=False)\nloop.run_until_complete(main())\n```\n\nIf a deadlock is detected by the TimelessEventLoop, a `DeadlockError` will be raised if the loop was created with the raise_on_deadlock flag set to True.\n\n## License\n\ntimeless_loop is licensed under the MIT License. See the LICENSE file for more details.\n",
    'author': 'Pedro Batista',
    'author_email': 'pedrovhb@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
