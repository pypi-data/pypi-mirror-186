# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boostbuild', 'boostbuild.cmd']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.6,<0.5.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['boost = boostbuild.main:main']}

setup_kwargs = {
    'name': 'boostbuild',
    'version': '0.1.13',
    'description': 'Boost is a simple build system that aims to create an interface for shell command substitution across different operative systems.',
    'long_description': '# Boost\nBoost is a simple build system that aims to create an interface for shell command substitution across different operative systems. Boost tries to centralize build steps on different development environments.\n\nBoost adds a simple way to add custom commands with different behaviours for different platforms.\n\n## Commands\nA command is a group of functions which determines the behaviour of an action on different environments. A command needs to implement these functions:\n- `generic_exec(args: List[str]) -> dict`: function if the code is the same across multiple platforms or\n- `win_exec(args: List[str]) -> dict`: for Windows commands.\n- `posix_exec(args: List[str]) -> dict`: for Posix commands.\n\nCurrently, commands files under cmd package which implement above deffined functions can be automatically used by its file name. For example, `boost.cmd.delete` can be used inside any `boost.yaml` `boost` targets by using the keyword `delete`.\n\n## Using Boost\nTo use Boost, first, create a `boost.yaml` file in your project directory. This is an example of a simple boost file.\n\n```yaml\nvars:\n  file: example.txt\n  current_dir: exec pwd\nboost:\n  dev: |\n    delete {file}\n    asd {current_dir}\n```\n- `vars`: Define key-value pairs representing variables that needs to be used inside boost targets. If a variable needs to store the output from a command, use `exec` followed by the commands that needs to be captured.\n- `boost`: Define key-value pairs named boost targets. Target key will be used to call that specific target. Value contains a list of commands separated by `\\n` that will be triggered when calling a specific target.\nIf a value needs to use a variable, use `$` followed by the variable name that was previously declared on `vars` section.\n\nTo call a boost target, run `boost <TARGET>`. If no boost target was specified, boost will use the first defined target.\n\n## Developing boost\nRequirements:\n  - poetry\n\nRun `poetry install`. Whit the previous command, you can run `poetry run boost` to test boost, boost command does automatically trigger `boostbuild.main:main` function.\n',
    'author': 'David Lopez',
    'author_email': 'davidlopez.hellin@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
