# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['prefect_yaml', 'prefect_yaml.flow']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'prefect>=2.7.1,<3.0.0', 'ruamel-yaml>=0.17.21,<0.18.0']

extras_require = \
{'docs': ['Sphinx>=5.0,<6.0',
          'insipid-sphinx-theme>=0.3.6,<0.4.0',
          'myst-parser>=0.18,<0.19']}

entry_points = \
{'console_scripts': ['prefect-yaml = prefect_yaml.cli:main']}

setup_kwargs = {
    'name': 'prefect-yaml',
    'version': '2023.0.0',
    'description': 'Prefect scheduler for YAML configuration',
    'long_description': '# Prefect YAML\n\n<p align="center">\n  <a href="https://github.com/factorpricingmodel/prefect-yaml/actions?query=workflow%3ACI">\n    <img src="https://github.com/factorpricingmodel/prefect-yaml/actions/workflows/ci.yml/badge.svg" alt="CI Status" >\n  </a>\n  <a href="https://prefect-yaml.readthedocs.io">\n    <img src="https://img.shields.io/readthedocs/prefect-yaml.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">\n  </a>\n  <a href="https://codecov.io/gh/factorpricingmodel/prefect-yaml">\n    <img src="https://img.shields.io/codecov/c/github/factorpricingmodel/prefect-yaml.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">\n  </a>\n</p>\n<p align="center">\n  <a href="https://python-poetry.org/">\n    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">\n  </a>\n  <a href="https://github.com/ambv/black">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">\n  </a>\n  <a href="https://github.com/pre-commit/pre-commit">\n    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">\n  </a>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/prefect-yaml/">\n    <img src="https://img.shields.io/pypi/v/prefect-yaml.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">\n  </a>\n  <img src="https://img.shields.io/pypi/pyversions/prefect-yaml.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">\n  <img src="https://img.shields.io/pypi/l/prefect-yaml.svg?style=flat-square" alt="License">\n</p>\n\nPackage to run prefect with YAML configuration. For further details, please refer\nto the [documentation](https://prefect-yaml.readthedocs.io/en/latest/)\n\n## Installation\n\nInstall this via pip (or your favourite package manager):\n\n`pip install prefect-yaml`\n\n## Usage\n\nRun the command line `prefect-yaml` with the specified configuration\nfile.\n\nFor example, the following YAML configuration is located in [examples/simple_config.yaml](examples/simple_config.yaml).\n\n```\nmetadata:\n  output:\n    directory: .output\n\ntask:\n  task_a:\n    caller: math:fabs\n    parameters:\n      - -9.0\n    output:\n      format: json\n  task_b:\n    caller: math:sqrt\n    parameters:\n      - !data task_a\n    output:\n      directory: null\n  task_c:\n    caller: math:fsum\n    parameters:\n      - [!data task_b, 1]\n```\n\nRun the following command to generate all the task outputs to the\ndirectory `.output` in the running directory.\n\n```shell\nprefect-yaml -c examples/simple_config.yaml\n```\n\nThe output directory contains all the task outputs in the specified\nformat.\n\n```shell\n% tree .output\n.output\n├── task_a.json\n└── task_c.pickle\n\n0 directories, 2 files\n```\n\nThe expected behavior is to\n\n1. run `task_a` to dump the value `fabs(-9.0)` to the output directory in JSON format,\n2. run `task_b` to get the value `sqrt(9.0)` (from the output of `task_a`)\n3. run `task_c` to dump the value `fsum([3.0, 1.0])` to the output directory in pickle format.\n\nAs the output directory in `task_b` is overridden as `null`, the output of `task_b` is passed to `task_c` in memory. Also, the output format in `task_c`\nis not specified so it is dumped in default format (pickle).\n\nFor further details, please see the section [configuration](https://prefect-yaml.readthedocs.io/en/latest/configuration.html) in the documentation.\n\n## Configuration\n\nThe output section defines how the task writes and loads the task return. The section in `metadata` applies for all tasks globally while that in each `task`\noverrides the global parameters.\n\nFor further details, please see the [documentation](https://prefect-yaml.readthedocs.io/en/latest/configuration.html#output) for parameter definitions\nin each section.\n\n## Output\n\nThe default output format is either pickle (default) or JSON, while users\ncan define their own output format.\n\nFor example, if you would like to use `pandas` to load and dump the parquet file\nin pyarrow engine by default, you can define the configuration like below.\n\n```\nmetadata:\n  format: parquet\n  dump-caller: object.to_parquet\n  dump-parameters:\n    engine: pyarrow\n  load-caller: pandas:read_parquet\n  load-parameters:\n    engine: pyarrow\n```\n\nAll the output parameters, like directory, dumper and loaders, can be overridden\nin the task level. You can also specify which tasks to export to the output\ndirectory, while the others to only be passed down to downstream in memory.\n\nFor further details, please see the [output](https://prefect-yaml.readthedocs.io/en/latest/output.html) section in documentation.\n\n## Roadmap\n\nCurrently the project is still under development. The basic features are\nmostly available while the following features are coming soon\n\n- Multi cloud storage support\n- Subtasks supported in each task\n-\n\n## Contributing\n\nAll levels of contributions are welcomed. Please refer to the [contributing](https://prefect-yaml.readthedocs.io/en/latest/contributing.html)\nsection for development and release guidelines.\n',
    'author': 'Factor Pricing Model',
    'author_email': 'factor.pricing.model@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/factorpricingmodel/prefect-yaml',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
