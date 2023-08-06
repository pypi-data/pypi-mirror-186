# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meeseeks', 'meeseeks.src', 'meeseeks.src.hash']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'meeseeks-singleton',
    'version': '0.4.0',
    'description': 'A Singleton python project',
    'long_description': '# A Singleton python project\n![Alt text](https://ih1.redbubble.net/image.1140492877.4744/mp,504x516,gloss,f8f8f8,t-pad,600x600,f8f8f8.jpg "Title")\n\nDid you need help? Call meeseeks from a single box from anywhere\n\nThis is meeseeks a single class to do singletons. In the core meeseeks is a class decorator that allows you to have a global singleton scope or a specialized one, some configurations can be used to give more flexibility to your code.\n\n\n# Scopes\n\nEach class with his decorator has a specialized scope, that is otherwise you create meeseeks object (OnlyOne) and this object will have your configuration and singletons\n\n### Specialized\n\n```python\nimport meeseeks\n\n@meeseeks.OnlyOne()\nclass A:\n    def __int__(self, a):\n        pass\n\na1a = A(10)\na1b = A(10)\na1c = A(20)\n\nassert a1a == a1b == a1c\n```\n\nor\n\n```python\nimport meeseeks\n\nonly_one = meeseeks.OnlyOne()\n\n@only_one\nclass A:\n    def __int__(self, a):\n        pass\n\na1a = A(10)\na1b = A(10)\na1c = A(20)\n\nassert a1a == a1b == a1c\n```\n\nOn this example we register the class reference in the meeseeks class instance scope\n\n# Configuration\n\nWe provide two configuration options:\n- `tll: int` (time to live) in seconds. Setting a value greater than 0, the singleton reference will have a time to live in seconds (default 0). Obs: the expired time validation will be made only when you create a new instance of the registered class _ie_ your object will still be in memory\n-  `by_args_hash: bool` ( a hash will be made of all args and kwargs ). Setting True, a singleton reference will be created for each arg + kwargs hash (default False). Obs:  The kwargs`s order doesn\'t have influence\n        \n\n### TTL \n\n```python\nimport meeseeks\nimport time\n\n@meeseeks.OnlyOne(ttl=1)\nclass A:\n    def __int__(self, *args, **kwargs):\n        pass\n\na1a = A(1, var_a="a")\na1b = A(1, var_a="a")\n\ntime.sleep(1)\n\na1c = A(1, var_a="a")\n\nassert a1a == a1b\nassert a1b != a1c\n```\n\nIn this example, we set the `ttl` to `1` second and validate if the first two calls result in the same object and after 1 second we validate if the object is different from the first two\n\n### BY_ARGS_HASH\n\n\n```python\nimport meeseeks\nimport time\n\n@meeseeks.OnlyOne(by_args_hash=True)\nclass A:\n    def __int__(self, *args, **kwargs):\n        pass\n\na1a = A(1, var_a="a", var_b="b")\na1b = A(1, var_b="b", var_a="a")\na1c = A(10, var_b="b", var_a="a")\n\n\n\nassert a1a == a1b\nassert a1c != a1b\n```\nIn this example, we set  `by_args_hash` variable to `True` and validate if the first two calls result in the same object despite the kwargs order being different. The last validation shows us that different args and kwargs result in different objects.\n',
    'author': 'Ximit Gaia',
    'author_email': 'im.ximit@gamil.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
