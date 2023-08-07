# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['volunor', 'volunor.core', 'volunor.test']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'volunor',
    'version': '1.0.0rc2',
    'description': 'Command line tools, with ease',
    'long_description': '<p align="center">\n<img src="https://app.codacy.com/project/badge/Coverage/5e8f1e9af0a04477966da5dfaf60c4fc" alt="coverage">\n<img src="https://app.codacy.com/project/badge/Grade/5e8f1e9af0a04477966da5dfaf60c4fc"/>\n<img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/thmahe/volunor/primary.yaml">\n<a href="https://pypi.org/project/volunor/" ><img alt="PyPI" src="https://img.shields.io/pypi/v/volunor"></a>\n</p>\n\n# Völunðr <img src="https://i.postimg.cc/m2M34BGS/logo.png" style="float: right;" alt="Logo" width="150" height="150">\n\n### _Build Command Line Tools with ease_\n\nVolunor offer a standard, dependency free & stable way to implement and maintain command line interface tools in Python.\n\n## Example\n\nBelow a basic example of a greeting command:\n```python\n# greeting.py\nimport volunor\n\n\nclass Hello(volunor.Command):\n    """\n    Simple greeting command.\n    """\n    # Arguments with argparse interface\n    def volunor_args(self, required_args, optional_args):\n        optional_args.add_argument("--count", type=int, default=1, metavar="INT", help="Number of greet")\n        required_args.add_argument("name", type=str, help="Name to greet")\n    \n    # Required method, called by volunor.Cli.big_bang method\n    def __call__(self, *args, **kwargs):\n        for _ in range(kwargs.get(\'count\')):\n            print(f"Hello {kwargs.get(\'name\')}")\n\n\ncli_descriptor = {\n    "greet": Hello,\n    "greet-group": {\n        "greet": Hello\n    }\n}\n\ncli = volunor.Cli(cli_descriptor, prog="greeting-cli")\n\nif __name__ == \'__main__\':\n    cli.big_gang()\n```\n\nRoot level helper:\n```shell\n$ python3 greeting.py -h\nusage: greeting-cli [-h] COMMAND ...\n\noptional arguments:\n  -h, --help   show this help message and exit\n\ncommands:\n  greet .......... Simple greeting command.\n  greet-group .... subcommand group\n```\n\nCommand helper:\n```\n$ python3 greeting.py greet -h\nusage: greeting-cli greet [-h] [--count INT] name\n\nSimple greeting command.\n\noptional arguments:\n  -h, --help   show this help message and exit\n\nrequired arguments:\n  name         Name to greet\n\noptional arguments:\n  --count INT  Number of greet\n```\n\nCommand output:\n```shell\n$ python3 greeting.py greet Thomas --count 2\nHello Thomas\nHello Thomas\n```\n\n## Run tests\n\n### Install dependencies\n\n```shell\nsudo apt install "^python3\\.(7|8|9|10|11)-venv$"\npip install poetry tox\n```\n',
    'author': 'Thomas Mahe',
    'author_email': 'contact@tmahe.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
