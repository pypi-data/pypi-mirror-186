# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linthell',
 'linthell.commands',
 'linthell.commands.pre_commit',
 'linthell.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'typing-extensions>=4.4.0,<5.0.0']

entry_points = \
{'console_scripts': ['linthell = linthell:cli',
                     'linthell-pre-commit = '
                     'linthell.commands.lint_pre_commit:lint_pre_commit']}

setup_kwargs = {
    'name': 'linthell',
    'version': '1.0.0',
    'description': 'Universal flakehell replacement for almost any linter you like',
    'long_description': '# linthell 🔥\nUniversal flakehell alternative that works with almost any linter you like.\n\n## How it works\nlinthell identifies each linter error as \n`(<file path>, <code at specific line>, <error message>)`, so it keep track\nof old errors even you add/delete some line from the same file. linthell\nstores there triplets inside baseline file.\n\nAt setup phase, you generate baseline file which identifies old errors.\nAfter that, linthell filters such errors and shows new only.\n\nIf you modify old code, then you should either fix these errors (refactor)\nor regenerate baseline. The tool\'s philosophy is that baseline should \nbe sharnk only, but how to deal with it is up to you.\n\n## Usage\nAll examples are shown with `flake8`, edit them for you case.\n\nAt first generate baseline file for every linter you use:\n```bash\nflake8 . | linthell baseline -b baseline-flake8.txt -f <linter regex>\n```\n\nThen lint your project via `linthell`:\n```bash\nflake8 . | linthell lint -b baseline-flake8.txt -f <linter regex>\n```\n\n## Custom linter format\nIf you use another linter then you must provide custom regex string\nstring to parse it\'s output. Default format is `flake8` default format.\nSome premade formats for linters:\n- `flake8`: `(?P<path>[a-zA-Z0-9\\._-]+(?:[\\\\/][a-zA-Z0-9\\._-]+)*):(?P<line>\\d+):\\d+: (?P<message>[^\\n]+)`\n- `pydocstyle`: `(?P<path>[a-zA-Z0-9\\._-]+(?:[\\\\/][a-zA-Z0-9\\._-]+)*):(?P<line>\\d+).+\\n\\s+(?P<message>[^\\n]+)`\n- `pylint`: `(?P<path>[a-zA-Z0-9\\._-]+(?:[\\\\/][a-zA-Z0-9\\._-]+)*):(?P<line>\\d+):\\d+: (?P<message>[^\\n]+)`\n\n### Create your own format regex\nYou can use your custom format regex. Suitable regex must\ncontains 3 named [python-like](https://docs.python.org/3/howto/regex.html#:~:text=The%20syntax%20for%20a%20named%20group%20is%20one%20of%20the%20Python%2Dspecific%20extensions%3A%20(%3FP%3Cname%3E...).%20name%20is%2C%20obviously%2C%20the%20name%20of%20the%20group) capturing groups: \n- `path` - relative file path \n- `line` - line number\n- `message` - linter message\n\nYour regex should matches all message related to an issue because \nunfiltered issues are printed by the whole match.\n\nYou can test your regex against linter output with [regexr](https://regexr.com/).\n\n## pre-commit support\nlinthell can be used as [pre-commit](https://pre-commit.com/) hook. Tested with\nflake8, pydocstyle, pylint, black linters.\n\n## Config file\n`linthell` can inject params from config file (`linthell --config path/to/config.ini`). \n`common` section applies for all commands, command specific config \nare specified by their name section, for example `[lint]`.\nNested commands are specified via dot. For example `linthell pre-commit lint`\nreads config from `[pre-commit.lint]` section.\n\nKeys must have same name as argument name of their command function. \nFor example, `baseline_file` and `lint_format`.\n\n\n## How to adapt linthell in project with pre-commit\n1. Create linthell config:\n```ini\n[common]\nbaseline_file=baseline.txt\nlint_format=(?P<path>[a-zA-Z0-9\\._-]+(?:[\\\\/][a-zA-Z0-9\\._-]+)*):(?P<line>\\d+):\\d+: (?P<message>[^\\n]+)\n\n[pre-commit.lint]\nlinter_command=flake8\n\n[pre-commit.baseline]\nlinter_command=flake8\n```\n2. Create a linthell hook inside `.pre-commit-config.yaml` file:\n```yaml\nrepos:\n  - repo: local\n    hooks:\n      - id: linthell\n        name: linthell flake8\n        entry: linthell --config linthell.ini pre-commit lint\n        language: system\n        types: [python]\n```\n3. Generate baseline file based on pre-commit hook definition and linthell config:\n```shell\nlinthell --config linthell.ini pre-commit baseline --hook-name "linthell flake8"\n```\n4. Validate new hook against generated baseline file\n```shell\npre-commit run --all linthell\n```',
    'author': 'Alexander Bespalov',
    'author_email': 'discrimy.off@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitea.discrimy.ru/discrimy/linthell',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
