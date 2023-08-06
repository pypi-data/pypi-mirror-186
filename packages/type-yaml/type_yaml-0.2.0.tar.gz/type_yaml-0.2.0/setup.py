# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['type_yaml']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'type-yaml',
    'version': '0.2.0',
    'description': '',
    'long_description': '# type-yaml\n\nDescribes a yaml schema using Python types.\n\nSimple Python types such as `list[str]` or `dict[int, list[str]]` that allow yaml to verify that the type fits and parse values based on it.\n\n## Requirements\n- Python 3.8+\n- PyYAML\n\n## Install\n```commandline\npip install type-yaml\n```\n\n## Features:\n- `int`\n- `float`\n- `str`\n- `bool`\n- `list` / `typing.List`\n- `dict` / `typing.Dict`\n- `set` / `typing.Set`\n- `tuple` / `typing.Tuple`\n- `dataclass`\n  - default values and default-factory\n  - special notation in yaml with metadata\n- `operator |`/ `typing.Union`\n- `typing.Any`\n- lazy evaluation by string representation of type\n\n## Examples\n\n```python\nfrom dataclasses import dataclass\n\nfrom type_yaml import load\n\n\n@dataclass\nclass Point:\n    x: int\n    y: int\n\n\nprint(load(list[Point], open("points.yaml")))\n# >>> [Point(x=1, y=2), Point(x=3, y=4)]\n```\n\n```yaml\n# points.yaml\n-\n  x: 1\n  y: 2\n-\n  x: 3\n  y: 4\n```\n\n## Usage\n\nFunctions such as `load`, `loads`, `dump`, and `dumps` can be imported from type_yaml. The details of each are as follows.\n\n- `load(type, stream, **kwargs)`\n  - Load a yaml file and parse it into a Python object.\n  - `type` is a type that can be parsed by type_yaml.\n  - `stream` is a text stream. e.g. `open("file.yaml")`\n  - options\n    - `loader`: yaml loader of PyYAML. default: `yaml.SafeLoader`\n    - `true_strings`: list of strings that are parsed as `True`. default: `("true", "yes", "on", "1")`\n    - `false_strings`: list of strings that are parsed as `False`. default: `("false", "no", "off", "0")`\n    - `type_name_map`, `globalns`, `localns`: a dictionary or namespace of variable names is given to allow interpretation of the string representation of the type\n- `loads(type, string, **kwargs)`\n  - Load a yaml string and parse it into a Python object.\n  - `type` is a type that can be parsed by type_yaml.\n  - `string` is a yaml string.\n  - options is same as `load`\n- `dump(value, stream, **kwargs)`\n  - Dump a Python object to a yaml file.\n  - `value` is a Python object that can be parsed by type_yaml.\n  - `stream` is a text stream. e.g. `open("file.yaml")`\n  - options\n    - `dumper`: yaml dumper of PyYAML. default: `type_yaml.yaml_interpreter.RealYamlDumper\n- `dumps(value, **kwargs)`\n  - Dump a Python object to a yaml string.\n  - `value` is a Python object that can be parsed by type_yaml.\n  - options is same as `dump`\n\n## Other\n\nThe license is the MIT License.\n\nIf you have any bugs, mistakes, feature suggestions, etc., issues and pull requests are welcome.\n',
    'author': 'nahco314',
    'author_email': 'nahco3_ta@yahoo.co.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
