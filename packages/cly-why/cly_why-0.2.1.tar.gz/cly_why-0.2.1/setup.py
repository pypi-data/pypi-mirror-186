# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cly_why']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cly-why',
    'version': '0.2.1',
    'description': 'A super simple functional cli helper lib',
    'long_description': '# Why?\nI wanted a simple library to write small to moderate cli programs.\nIt only uses the standard library.\n\n# Why not X?\n## X = argparse\nIts way more then what I need 99% of the time.\n\n## X = click\nI don\'t particularly like decorators.\n\n## X = rich\nI like pprint, but it always seems like to much\n\n## X = typer\nI\'ve used typer a bit, but it never clicked with me.\n\n# Core Functions\n## Text-Decorate and Colorize \nTake a string and color/text-decoration name and returns the string wrapped in its ansi code\n## Cly\nEntrypoint function\nBy default ignores functions that start with \'_\'/underscore\n\n# Feature List\n- [X] Colorize and Text Decorate\n- [ ] Tests\n- [ ] Automatic Fish Shell Completions\n- [ ] Prompts\n  - [ ] Text Prompt\n  - [ ] Multiline Prompt\n  - [ ] Fzf Selector\n  - [ ] Date Selector\n- [ ] 2 line functionality\n```python\nimport cly_why\n\nif __name__ == "__main__":\n\tcly_why.cly()\n```\n',
    'author': '00il',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
