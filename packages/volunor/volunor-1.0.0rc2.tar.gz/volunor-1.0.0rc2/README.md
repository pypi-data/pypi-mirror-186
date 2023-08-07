<p align="center">
<img src="https://app.codacy.com/project/badge/Coverage/5e8f1e9af0a04477966da5dfaf60c4fc" alt="coverage">
<img src="https://app.codacy.com/project/badge/Grade/5e8f1e9af0a04477966da5dfaf60c4fc"/>
<img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/thmahe/volunor/primary.yaml">
<a href="https://pypi.org/project/volunor/" ><img alt="PyPI" src="https://img.shields.io/pypi/v/volunor"></a>
</p>

# Völunðr <img src="https://i.postimg.cc/m2M34BGS/logo.png" style="float: right;" alt="Logo" width="150" height="150">

### _Build Command Line Tools with ease_

Volunor offer a standard, dependency free & stable way to implement and maintain command line interface tools in Python.

## Example

Below a basic example of a greeting command:
```python
# greeting.py
import volunor


class Hello(volunor.Command):
    """
    Simple greeting command.
    """
    # Arguments with argparse interface
    def volunor_args(self, required_args, optional_args):
        optional_args.add_argument("--count", type=int, default=1, metavar="INT", help="Number of greet")
        required_args.add_argument("name", type=str, help="Name to greet")
    
    # Required method, called by volunor.Cli.big_bang method
    def __call__(self, *args, **kwargs):
        for _ in range(kwargs.get('count')):
            print(f"Hello {kwargs.get('name')}")


cli_descriptor = {
    "greet": Hello,
    "greet-group": {
        "greet": Hello
    }
}

cli = volunor.Cli(cli_descriptor, prog="greeting-cli")

if __name__ == '__main__':
    cli.big_gang()
```

Root level helper:
```shell
$ python3 greeting.py -h
usage: greeting-cli [-h] COMMAND ...

optional arguments:
  -h, --help   show this help message and exit

commands:
  greet .......... Simple greeting command.
  greet-group .... subcommand group
```

Command helper:
```
$ python3 greeting.py greet -h
usage: greeting-cli greet [-h] [--count INT] name

Simple greeting command.

optional arguments:
  -h, --help   show this help message and exit

required arguments:
  name         Name to greet

optional arguments:
  --count INT  Number of greet
```

Command output:
```shell
$ python3 greeting.py greet Thomas --count 2
Hello Thomas
Hello Thomas
```

## Run tests

### Install dependencies

```shell
sudo apt install "^python3\.(7|8|9|10|11)-venv$"
pip install poetry tox
```
