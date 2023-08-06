# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kohi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'kohi',
    'version': '0.2.0',
    'description': 'A powerfull schema validator',
    'long_description': '\n# kohi\n\n<p align="center">A powerfull schema validator</p>\n\n![GitHub Repo stars](https://img.shields.io/github/stars/natanfeitosa/kohi)\n![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/natanfeitosa/kohi/pytest.yml?label=Pytest&logo=github)\n![GitHub](https://img.shields.io/github/license/natanfeitosa/kohi)\n![PyPI - Format](https://img.shields.io/pypi/format/kohi)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kohi)\n![PyPI - Package Version](https://img.shields.io/pypi/v/kohi)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/kohi)\n\n## Instalation\n\nVia Poetry:\n```sh\npoetry add kohi\n```\n\nVia PIP:\n```sh\npip install kohi\n```\n\nVia GitHub (recommended only in dev env):\n```sh\ngit clone https://github.com/natanfeitosa/kohi.git && cd kohi && pip install .\n```\n\n## Quickstart\n\nTo validate a type you can import your schema validator from `kohi` or `from kohi.<type> import <type>Schema`\n\ne.g.\n\nLet\'s check if a person\'s date of birth is a positive integer less than the current date — 2023 — and greater than or equal to 2005\n\n```python\nfrom kohi import NumberSchema\n# from kohi.number import NumberSchema\n\nn = NumberSchema().int().positive().lt(2023).gte(2005)\n\nprint(n.validate(2005)) # True\nprint(n.validate(2022)) # True\nprint(n.validate(2004)) # False\nprint(n.validate(2023)) # False\n\n# You can see the errors generated in the last `validate` call just by accessing the `errors` property\n# print(n.errors) # [\'number must be less than 2022\']\n```\n\n## Validators\n\n* [`kohi.base.BaseSchema`](#baseschema)\n> Only one base class for all schema validators\n* [`kohi.number.NumberSchema`](#numberschema)\n> or `kohi.NumberSchema`\n* [`kohi.string.StringSchema`](#stringschema)\n> or `kohi.StringSchema`\n\n## Methods\n\n### `BaseSchema`\n* `add_validator(name, func): Self`\n  > Add a custom data validator\n* `validate(data): bool`\n  > The method to be called when we validate the schema\n* `reset(): None`\n  > Reset error list\n* `throw(): Self`\n  > By default no errors are thrown, but when this method is chained a `ValidationError` will be thrown\n\n### `NumberSchema`\ninherits from [`BaseSchema`](#baseschema)\n> By default validates int and float \n\n* `float(): Self`\n  > Validate only `float`\n* `int(): Self`\n  > Validate only `int`\n* `lt(num): Self`\n  > Validates if the data is less than `num`\n* `gt(num): Self`\n  > Validates if the data is greater than `num`\n* `lte(num): Self`\n  > Validates if the data is less than or equal to `num`\n* `gte(num): Self`\n  > Validates if the data is greater than or equal to `num`\n* `min(num): Self`\n  > Just an alias for `gte(num)`\n* `max(num): Self`\n  > Just an alias for `lte(nun)`\n* `positive(): Self`\n  > Just an alias for `gt(0)`\n* `negative(): Self`\n  > Just an alias for `lt(0)`\n* `nonpositive(): Self`\n  > Just an alias for `lte(0)`\n* `nonnegative(): Self`\n  > Just an alias for `gte(0)`\n\n### StringSchema\ninherits from [`BaseSchema`](#baseschema)\n\n* `min(min_length): Self`\n  > Validate if the data len is greater than or equal to min_length\n* `length(length): Self`\n  > Validate if the data len equal to length\n* `max(max_length): Self`\n  > Validate if the data len is less than or equal to max_length\n* `url(): Self`\n  > Validate if the data is an url\n* `uuid(): Self`\n  > Validate if the data is a valid uuid\n* `starts_with(text): Self`\n  > Validate if the data starts with text\n* `ends_with(text): Self`\n  > Validate if the data ends with text\n\n## Dev env\n\n* install development dependencies\n* check types using `mypy`\n* run all tests using `pytest`\n',
    'author': 'Natan Santos',
    'author_email': 'natansantosapps@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/natanfeitosa/kohi#readme',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
