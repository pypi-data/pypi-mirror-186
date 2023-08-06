# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['confspawn']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=3.1.0,<4.0.0', 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['confenv = confspawn.cli:config_value',
                     'confrecipe = confspawn.cli:recipizer',
                     'confspawn = confspawn.cli:spawner']}

setup_kwargs = {
    'name': 'confspawn',
    'version': '0.4.1',
    'description': 'Easily build configuration files from templates.',
    'long_description': "Installation\n------------\n\n```shell\npip install confspawn\n```\n\n\nUsage\n-----\nTwo CLI commands are available, `confspawn` and `confenv`.\n\n```\nusage: confenv [-h] -c CONFIG -v VARIABLE\n\nRetrieve configuration value from TOML file.\n\nexamples:\nconfenv -c ./confs/sample_config.toml -v test.coolenv\nexport TEST_VAR=$(poetry run confenv -c ./confs/sample_config.toml -v test.coolenv)\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -c CONFIG, --config CONFIG\n                        File path for your TOML configuration file.\n  -v VARIABLE, --variable VARIABLE\n                        Variable name to print. For nested keys, use e.g.\n                        'toplevel.secondlevel.varname'.\n  -e ENV, --env ENV     Useful to specify environment-related modes, i.e.\n                        production or development. 'confspawn_env.value' will\n                        refer to 'confspawn_env.env.value'. Defaults to\n                        'less'.\n```\n\n```\nusage: confspawn [-h] -c CONFIG -s TEMPLATE -t TARGET [-r] [-p PREFIX]\n\nEasily build configuration files from templates.\n\nexamples:\nconfspawn -c ./config.toml -s ./foo/templates -t /home/me/target\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -c CONFIG, --config CONFIG\n                        File path for your TOML configuration file.\n  -s TEMPLATE, --template TEMPLATE\n                        Template directory path where your configuration\n                        templates are. Other files not indicated by prefix\n                        will also be copied over. Does not traverse\n                        subdirectories bt default.\n  -t TARGET, --target TARGET\n                        Target directory path where your files will end up\n                        (will be created if none exists, also overwrites\n                        previous directory).\n  -r, --recurse         Go through template directory recursively.\n  -p PREFIX, --prefix PREFIX\n                        Prefix that indicates file is a configuration\n                        template. Defaults to 'confspawn_' or the value of the\n                        CONFSPAWN_PREFIX env var, if set.\n  -e ENV, --env ENV     Useful to specify environment-related modes, i.e.\n                        production or development. 'confspawn_env.value' will\n                        refer to 'confspawn_env.env.value'. Defaults to\n                        'less'.\n```\n\n```\nusage: confrecipe [-h] -r RECIPE [-p PREFIX] [-e ENV]\n\nBuild multiple confspawn configurations using a recipe.\n\nexamples:\nconfrecipe -c ./config.toml -s ./foo/templates -t /home/me/target\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -r RECIPE, --recipe RECIPE\n                        File path for your TOML recipe file.\n  -p PREFIX, --prefix PREFIX\n                        Prefix that indicates file is a configuration\n                        template. Defaults to 'confspawn_' or the value of the\n                        CONFSPAWN_PREFIX env var, if set.\n  -e ENV, --env ENV     Overwrite env set in recipe. Defaults to 'None'.\n\n```\n\nThe main entrypoints to use `confspawn` programmatically are `spawn_write()` (corresponds to the `confspawn` command) and `load_config_value()` (corresponds to the `confenv` command). See the documentation for more details.",
    'author': 'Tip ten Brink',
    'author_email': '75669206+tiptenbrink@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
