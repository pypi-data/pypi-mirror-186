# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tartufo', 'tartufo.commands']

package_data = \
{'': ['*'], 'tartufo': ['data/*']}

install_requires = \
['GitPython>=3.1.29,<4.0.0',
 'cached-property>=1.5.2,<2.0.0',
 'click>=8.1.0,<9.0.0',
 'tomlkit>=0.11.4,<0.12.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['pygit2>=1.10.0,<2.0.0'],
 ':python_version >= "3.8" and python_version < "4.0"': ['pygit2>=1.11.0,<2.0.0'],
 ':sys_platform == "win32"': ['colorama'],
 'docs': ['recommonmark>=0.7,<0.8',
          'sphinx>=5.0.0,<6.0.0',
          'sphinx-autodoc-typehints>=1.12.0,<2.0.0',
          'sphinx-click>=4.0.0,<5.0.0',
          'sphinx-rtd-theme>=1.0.0,<2.0.0',
          'sphinxcontrib-spelling>=7.2.1,<8.0.0']}

entry_points = \
{'console_scripts': ['tartufo = tartufo.cli:main']}

setup_kwargs = {
    'name': 'tartufo',
    'version': '4.0.0',
    'description': 'tartufo is a tool for scanning git repositories for secrets/passwords/high-entropy data',
    'long_description': '# ![tartufo logo](docs/source/_static/img/tartufo.png)\n\n[![Join Slack](https://img.shields.io/badge/Join%20us%20on-Slack-e01563.svg)](https://www.godaddy.com/engineering/slack/)\n[![ci](https://github.com/godaddy/tartufo/workflows/ci/badge.svg)](https://github.com/godaddy/tartufo/actions?query=workflow%3Aci)\n[![Codecov](https://img.shields.io/codecov/c/github/godaddy/tartufo)](https://codecov.io/gh/godaddy/tartufo)\n[![PyPI](https://img.shields.io/pypi/v/tartufo)](https://pypi.org/project/tartufo/)\n[![PyPI - Status](https://img.shields.io/pypi/status/tartufo)](https://pypi.org/project/tartufo/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tartufo)](https://pypi.org/project/tartufo/)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/tartufo)](https://pypi.org/project/tartufo/)\n[![Documentation Status](https://readthedocs.org/projects/tartufo/badge/?version=latest)](https://tartufo.readthedocs.io/en/latest/?badge=latest)\n[![License](https://img.shields.io/github/license/godaddy/tartufo)](https://github.com/godaddy/tartufo/blob/main/LICENSE)\n\n`tartufo` searches through git repositories for secrets, digging deep into\ncommit history and branches. This is effective at finding secrets accidentally\ncommitted. `tartufo` also can be used by git pre-commit scripts to screen\nchanges for secrets before they are committed to the repository.\n\nThis tool will go through the entire commit history of each branch, and check\neach diff from each commit, and check for secrets. This is both by regex and by\nentropy. For entropy checks, tartufo will evaluate the shannon entropy for both\nthe base64 char set and hexidecimal char set for every blob of text greater\nthan 20 characters comprised of those character sets in each diff. If at any\npoint a high entropy string > 20 characters is detected, it will print to the\nscreen.\n\n## Example\n\n![Example Issue](docs/source/_static/img/example_issue.png)\n\n## Documentation\n\nOur main documentation site is hosted by Read The Docs, at\n<https://tartufo.readthedocs.io>.\n\n## Usage\n\n```bash\nUsage: tartufo [OPTIONS] COMMAND [ARGS]...\n\n  Find secrets hidden in the depths of git.\n\n  Tartufo will, by default, scan the entire history of a git repository for\n  any text which looks like a secret, password, credential, etc. It can also\n  be made to work in pre-commit mode, for scanning blobs of text as a pre-\n  commit hook.\n\nOptions:\n  --default-regexes / --no-default-regexes\n                                  Whether to include the default regex list\n                                  when configuring search patterns. Only\n                                  applicable if --rules is also specified.\n                                  [default: default-regexes]\n  --entropy / --no-entropy        Enable entropy checks.  [default: entropy]\n  --regex / --no-regex            Enable high signal regexes checks.\n                                  [default: regex]\n  --scan-filenames / --no-scan-filenames\n                                  Check the names of files being scanned as\n                                  well as their contents.  [default: scan-\n                                  filenames]\n  -of, --output-format [json|compact|text]\n                                  Specify the format in which the output needs\n                                  to be generated `--output-format\n                                  json/compact/text`. Either `json`, `compact`\n                                  or `text` can be specified. If not provided\n                                  (default) the output will be generated in\n                                  `text` format.\n  -od, --output-dir DIRECTORY     If specified, all issues will be written out\n                                  as individual JSON files to a uniquely named\n                                  directory under this one. This will help\n                                  with keeping the results of individual runs\n                                  of tartufo separated.\n  -td, --temp-dir DIRECTORY       If specified, temporary files will be\n                                  written to the specified path\n  --buffer-size INTEGER           Maximum number of issue to buffer in memory\n                                  before shifting to temporary file buffering\n                                  [default: 10000]\n  --git-rules-repo TEXT           A file path, or git URL, pointing to a git\n                                  repository containing regex rules to be used\n                                  for scanning. By default, all .json files\n                                  will be loaded from the root of that\n                                  repository. --git-rules-files can be used to\n                                  override this behavior and load specific\n                                  files.\n  --git-rules-files TEXT          Used in conjunction with --git-rules-repo,\n                                  specify glob-style patterns for files from\n                                  which to load the regex rules. Can be\n                                  specified multiple times.\n  --config FILE                   Read configuration from specified file.\n                                  [default: tartufo.toml]\n  -q, --quiet / --no-quiet        Quiet mode. No outputs are reported if the\n                                  scan is successful and doesn\'t find any\n                                  issues\n  -v, --verbose                   Display more verbose output. Specifying this\n                                  option multiple times will incrementally\n                                  increase the amount of output.\n  --log-timestamps / --no-log-timestamps\n                                  Enable or disable timestamps in logging\n                                  messages.  [default: log-timestamps]\n  --entropy-sensitivity INTEGER RANGE\n                                  Modify entropy detection sensitivity. This\n                                  is expressed as on a scale of 0 to 100,\n                                  where 0 means "totally nonrandom" and 100\n                                  means "totally random". Decreasing the\n                                  scanner\'s sensitivity increases the\n                                  likelihood that a given string will be\n                                  identified as suspicious.  [default: 75;\n                                  0<=x<=100]\n  -V, --version                   Show the version and exit.\n  -h, --help                      Show this message and exit.\n\nCommands:\n  pre-commit        Scan staged changes in a pre-commit hook.\n  scan-remote-repo  Automatically clone and scan a remote git repository.\n  scan-folder       Scan a folder.\n  scan-local-repo   Scan a repository already cloned to your local system.\n```\n\n## Contributing\n\nAll contributors and contributions are welcome! Please see [our contributing\ndocs] for more information.\n\n## Attributions\n\nThis project was inspired by and built off of the work done by Dylan Ayrey on\nthe [truffleHog] project.\n\n[our contributing docs]: https://tartufo.readthedocs.io/en/latest/CONTRIBUTING.html\n[pre-commit]: https://pre-commit.com/\n[truffleHog]: https://github.com/dxa4481/truffleHog\n',
    'author': 'Dylan Ayrey',
    'author_email': 'dxa4481@rit.edu',
    'maintainer': 'GoDaddy',
    'maintainer_email': 'oss@godaddy.com',
    'url': 'https://github.com/godaddy/tartufo/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
