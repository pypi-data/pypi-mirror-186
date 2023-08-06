# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rumex', 'rumex.parsing', 'rumex.parsing.state_machine']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rumex',
    'version': '0.2.0',
    'description': '',
    'long_description': "=====\nRumex\n=====\n\n`Behaviour Driven Development`_ (BDD) testing library.\n\nRumex is a lightweight library alternative to the `behave`_ framework.\n\n\nBasic example\n-------------\n\n.. code:: python\n\n    import rumex\n\n    example_file = rumex.InputFile(\n        text='''\n            Name: Basic example\n\n            Scenario: Simple arithmetics\n\n                Given an integer 1\n                And an integer 2\n                When addition is performed\n                Then the result is 3\n        ''',\n        uri='in place file, just an example',\n    )\n\n    steps = rumex.StepMapper()\n\n\n    class Context:\n\n        def __init__(self):\n            self.integers = []\n            self.sum = None\n\n\n    @steps(r'an integer (\\d+)')\n    def store_integer(integer: int, *, context: Context):\n        context.integers.append(integer)\n\n\n    @steps(r'addition is performed')\n    def add(*, context: Context):\n        context.sum = sum(context.integers)\n\n\n    @steps(r'the result is (\\d+)')\n    def check_result(expected_result: int, *, context: Context):\n        assert expected_result == context.sum\n\n\n    rumex.run(\n        files=[example_file],\n        steps=steps,\n        context_maker=Context,\n    )\n\n\n.. _`Behaviour Driven Development`:\n  https://en.wikipedia.org/wiki/Behavior-driven_development\n\n.. _`behave`: https://github.com/behave/behave\n",
    'author': 'uigctaw',
    'author_email': 'uigctaw@metadata.social',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
