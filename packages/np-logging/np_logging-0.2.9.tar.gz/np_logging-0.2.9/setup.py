# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['np_logging']

package_data = \
{'': ['*']}

install_requires = \
['importlib_resources>1.4', 'np_config>=0.2.2,<0.3.0']

extras_require = \
{'dev': ['pip-tools', 'isort', 'mypy', 'black', 'pytest', 'poetry']}

setup_kwargs = {
    'name': 'np-logging',
    'version': '0.2.9',
    'description': 'Pre-configured file, web, and email logging for Mindscope neuropixels projects, repackaging code from AIBS mpeconfig.',
    'long_description': "**For use on internal Allen Institute network**\n\nQuick start:\n```python\nimport logging\nimport np_logging\n\nnp_logging.setup()\n```\n\n`np_logging.setup()` with no arguments uses a default config, providing the loggers `web` and `email`, in addition to the default\n`root` which includes file handlers for `logging.INFO` and `logging.DEBUG`  levels, plus\nconsole logging. \n\nThe built-in python `logging` module can then be used as normal.\n\nUsage example:\n```python\nlogging.getLogger('web').info('test: web server')\nlogging.getLogger('email').info('test: email logger')\nlogging.debug('test: root logger')\n```\n\n- user configs should be specified according to the python logging [library dict schema](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema)\n\n- the default config is fetched from the\nZooKeeper server `eng-mindscope:2181`\n- configs can be added via ZooNavigator webview:\n  [http://eng-mindscope:8081](http://eng-mindscope:8081)\n- or more conveniently, via an extension for VSCode such as [gaoliang.visual-zookeeper](https://marketplace.visualstudio.com/items?itemName=gaoliang.visual-zookeeper)\n\nZooKeeper configs or config files can be used by supplying their path to `setup()`:\n```python\nnp_logging.setup(\n    '/projects/np_logging_test/defaults/logging'\n)\n```\n\n\nOther input arguments to `np_logging.setup()`:\n\n- `project_name` (default current working directory name) \n  \n    - sets the `channel` value for the web logger\n    - the web log can be viewed at [http://eng-mindscope:8080](http://eng-mindscope:8080)\n\n- `email_address` (default `None`)\n      \n    - if one or more addresses are supplied, an email is sent at program exit reporting the\n      elapsed time and cause of termination. If an exception was raised, the\n      traceback is included.\n\n- `log_at_exit` (default `True`)\n\n    - If `True`, a message is logged when the program terminates, reporting total\n      elapsed time.\n\n- `email_at_exit` (default `False` or `True` if `email_address` is not `None`)\n\n    - If `True`, an email is sent when the program terminates.\n      \n    - If `logging.ERROR`, the email is only sent if the program terminates via an exception.\n\n",
    'author': 'Ben Hardcastle',
    'author_email': 'ben.hardcastle@alleninstitute.org',
    'maintainer': 'Ben Hardcastle',
    'maintainer_email': 'ben.hardcastle@alleninstitute.org',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
