# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['koil', 'koil.composition']

package_data = \
{'': ['*']}

install_requires = \
['janus>=1.0.0,<2.0.0']

extras_require = \
{'uvloop': ['uvloop>=0.16.0,<0.17.0']}

setup_kwargs = {
    'name': 'koil',
    'version': '0.2.11',
    'description': 'Async for a sync world',
    'long_description': '# koil\n\n[![codecov](https://codecov.io/gh/jhnnsrs/koil/branch/master/graph/badge.svg?token=UGXEA2THBV)](https://codecov.io/gh/jhnnsrs/koil)\n[![PyPI version](https://badge.fury.io/py/koil.svg)](https://pypi.org/project/koil/)\n![Maintainer](https://img.shields.io/badge/maintainer-jhnnsrs-blue)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/koil.svg)](https://pypi.python.org/pypi/koil/)\n[![PyPI status](https://img.shields.io/pypi/status/koil.svg)](https://pypi.python.org/pypi/koil/)\n[![PyPI download day](https://img.shields.io/pypi/dm/koil.svg)](https://pypi.python.org/pypi/koil/)\n\n### DEVELOPMENT\n\n# Quick Start\n\nLet\'s discover **Koil in less than 5 minutes**.\n\n### Inspiration\n\nkoil is an abstraction layer for threaded asyncio to enable "sensible defaults" for\nprogrammers working with frameworks that are barely compatible with asyncio (originally developped to get around pyqt5)\n\n### Main Concept\n\nAsync libraries are amazing, and its an ecosystem rapidly increasing, however in some contexts it still doesn\'t seem like\nthe way to go and the burden of learning these concepts might be to high. However you developed a wonderful async api\nthat you want to share with the world.\n\n```python\nclass AmazingAsyncAPI:\n    def __init__(self) -> None:\n        pass\n\n    async def sleep(self):\n        await asyncio.sleep(0.01)\n        return "the-glory-of-async"\n\n    async def __aenter__(self):\n        # amazing connection logic\n        return self\n\n    async def __aexit__(self, *args, **kwargs):\n        # amazing tear down logic\n        return self\n\n```\n\nHowever if somebody wants to use this api in sync environment they are in for a good one, as a call to asyncio.run() just wont do the trick.\n\n```python\nfrom koil import koilable, unkoilable\n\n@koilable()\nclass AmazingAsyncAPI:\n    def __init__(self) -> None:\n        pass\n\n    @unkoilable()\n    async def sleep(self):\n        await asyncio.sleep(0.01)\n        return "the-glory-of-async"\n\n    async def __aenter__(self):\n        # amazing connection logic\n        return self\n\n    async def __aexit__(self, *args, **kwargs):\n        # amazing tear down logic\n        return self\n\n```\n\nAnd now it works. Just use your Api with a normal context manager.\n\n```python\nwith AmazingAsyncAPI as e:\n  print(e.sleep())\n```\n\nKoil under the hood spawns a new event loop in another thread, calls functions that are marked with unkoilable\nthreadsafe in that loop and returns the result, when exiting it shuts down the loop in the other thread.\n\nIf you have multiple context managers or tasks that you would just like to run in another thread, you can\nalso create a loop in another thread\n\n```python\n\nasync def task(arg):\n       x = await ...\n       return x\n\nwith Koil(): # creates a threaded loop\n\n    x = unkoil(task, 1)\n\n    with AmazingAsyncAPI as e:\n       print(e.sleep())\n\n```\n\nMoreover koil also is able to be used with generators\n\n```python\nimport asyncio\nfrom koil import unkoil_gen\n\nasync def task(arg):\n    for i in range(0,20)\n      await asyncio.sleep(1)\n      yield arg\n\n\nwith Koil(): # creates a threaded loop\n\n    for x in unkoil_gen(task, 1):\n        print(x)\n\n```\n\nAnd finally koil is able to create task like objects,\n\n```python\nasync def task(arg):\n    await asyncio.sleep(2)\n    return arg\n\nwith Koil():\n\n  x = unkoil(task, 1, as_task=True)\n\n  # do other stuff\n\n  if x.done():\n      print(x)\n\n```\n\n## PyQt Support\n\n... Documentation coming soon...\n\n### Installation\n\n```bash\npip install koil\n```\n',
    'author': 'jhnnsrs',
    'author_email': 'jhnnsrs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
