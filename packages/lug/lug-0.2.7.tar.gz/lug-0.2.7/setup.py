# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lug']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=2.2.0,<3.0.0',
 'docker>=6.0.0,<7.0.0',
 'toolchest-client>=0.11.9,<0.12.0']

setup_kwargs = {
    'name': 'lug',
    'version': '0.2.7',
    'description': 'Run Python functions paired with any Docker container. Run locally or in the cloud.',
    'long_description': '# Lug\n\n<p align="center">\n    <a href="https://pypi.python.org/pypi/lug/" alt="PyPI version">\n        <img alt="PyPI" src="https://img.shields.io/pypi/v/lug?labelColor=212121&color=304FFE"></a>\n    <a href="https://github.com/trytoolchest/lug/" alt="Build">\n        <img src="https://img.shields.io/circleci/build/gh/trytoolchest/lug/main?label=build&token=3eb013dde86ed79996a768ab325cd30ea3a1c993&labelColor=212121&color=304FFE" /></a>\n    <a href="https://discord.gg/zgeJ9Pss" alt="Discord">\n        <img src="https://img.shields.io/discord/1016544715128176721?labelColor=212121&color=304FFE&label=discord" /></a>\n</p>\n\n**Lug** is an open source package that redirects Python calls to `subprocess.run`, `subprocess.Popen`, and `os.system` into \nany Docker container. This makes these system-level Python calls behave the same way on different machines, without \nrequiring any changes to the Docker container.\n\nLug also packages the Python function and Docker container, so you can easily run both in the cloud via Lug if needed. \nThis lets you give more computing power to the functions that need it.\n## Highlights\n\n- 📦 `subprocess.run`, `subprocess.Popen`, and `os.system` run in your container – for the dependencies you can\'t \ninstall with pip\n- 🐍 Use containers as-is, no need to add your Python version\n- ☁️ Run on your computer or in the cloud\n\n## Why use Lug?\n\nSome software – especially in bioinformatics and machine learning – can\'t be installed with `pip install`. Conda works \nin some cases, but for others a Docker container is the best solution. Lug makes the Docker container easier to work \nwith from Python.\n\nThe same software is usually resource intensive. Lug can run on your computer, or it can automatically run the Python \nfunction and Docker container in the cloud with [Toolchest](https://docs.trytoolchest.com/docs/pricing).\n\n## Prerequisites\n\n- macOS or Linux (supporting `POSIX_SPAWN`)\n- [Docker Engine](https://docs.docker.com/engine/install/) and the Docker CLI\n\n## Install\n\n[Install Docker Engine and the CLI](https://docs.docker.com/engine/install/), if you don\'t have it.\n\n### With pip:\n\n`pip install lug`\n\n### With Poetry:\n\n`poetry add lug`\n\n## Get started \n\n### Run a Python function locally in a Docker image\n\nEverything but the `subprocess.run` below runs as-is, with the `echo` command running in the Docker image:\n\n```python\nimport lug\nimport subprocess\n\n@lug.run(image="alpine:3.16.2")\ndef hello_world():\n    result = subprocess.run(\'echo "Hello, `uname`!"\', capture_output=True, text=True, shell=True)\n    return result.stdout\n\nprint(hello_world())\n```\n\nThat\'s it! After it finishes, you\'ll see `Hello, Linux!`.\n\n\n## Docs\n\nFull docs are at [lug.dev](https://lug.dev)\n\n## Open-source roadmap\n\n- [x] Run a Python function in a local container\n- [x] Maintain Python major.version in function and in container\n- [x] Serialize and deserialize Python function and Python dependencies\n- [x] `os.system()`, `subprocess.run()`, and `subprocess.Popen()` redirect to a user-specified container\n- [x] Local files passed to as input go to `./input/` in remote Docker container\n- [x] Remote files written to `./output/` in the container are written to local output Path\n- [x] Runs locally\n- [x] Run in the cloud with [Toolchest](https://github.com/trytoolchest/toolchest-client-python)\n- [ ] Stream live `stdout` during remote execution\n- [ ] `pip`-based environment propagation (help needed)\n- [ ] `conda`-based environment propagation (help needed)\n- [ ] Run in the cloud with AWS (help needed)\n- [ ] Run in the cloud with GCP (help needed)\n\n## License\n\nLug is licensed under the Apache License 2.0',
    'author': 'Justin Herr',
    'author_email': 'justin@trytoolchest.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://lug.dev',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
