# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['kkpyutil']
setup_kwargs = {
    'name': 'kkpyutil',
    'version': '0.114.0',
    'description': 'zero-dependency utility functions and classes',
    'long_description': '# kkpyutil\nSmall utility frequently used by myself for daily Python work.\n- No dependency on third-party Python modules, so it alwyas run\n- Some functions use system builtin executable or essential programs, so runs will fail if those are not installed separately\n\n## INSTALL\n\n```shell\npip3 install kkpyutil\n```\n',
    'author': 'Beinan Li',
    'author_email': 'li.beinan@gmail.com',
    'maintainer': 'Beinan Li',
    'maintainer_email': 'li.beinan@gmail.com',
    'url': 'https://github.com/kakyoism/kkpyutil/',
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
