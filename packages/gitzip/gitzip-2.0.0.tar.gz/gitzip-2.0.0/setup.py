# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gitzip']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gitzip',
    'version': '2.0.0',
    'description': 'A small python program to export files changed between git commits or branches to a zip file retaining the directory structure.',
    'long_description': '# gitzip\n\nExport all the changed files between two git commits or branches to a zip file including\nthe directory structure.\n\n## gitzip usage\n\nNavigate into your repositorys base directory. Then execute the following command.\n\n```\npython -m gitzip export.zip 0c321f2 master\n```\n\nThis will create a `export.zip` file containing all files that changed between commit\n`0c321f2` and the current `master` branch. The files will have the contents of the\ncurrent branch/commit that is checked out in your current repository. If the changed\nfiles are in a subdirectory, this subdirectory is created in the zip file.\n\n## Installation\n\n### Via `pip`\n\n```bash\npip install gitzip\n```\n\n### From source\nTo run this program from the code directly, [`python`](https://www.python.org/) and\n[`poetry`](https://python-poetry.org/) (`pip install poetry`) are required. Clone or\ndownload the repository.\n\nTo install all the dependencies, use your command line and navigate to the directory\nwhere this `README` file is located in. Then run\n\n```bash\npoetry install\n```\n\n### For development\n\nFor development installation perform the [From source](#from-source) installation.\n\nFor installing new packages, always run\n```\npoetry add <pip-package-name>\n```\ninstead of `pip install <pip-package-name>`.\n\nLaunch the program either check out the [Execution](#execution) section or use the\n*Run and Debug*-side panel of VSCode.\n\nIf the interpreter of the virtual environment does not show up in VSCode, add it manually. The virtual environments are located in `{cache-dir}/virtualenvs/<venv-name>/Scripts/python.exe` where the [`{cache-dir}`](https://python-poetry.org/docs/configuration/#cache-dir) depends on the operating system (`~/.cache/pypoetry`, `~/Library/Caches/pypoetry` or `C.\\Users\\%USERNAME%\\AppData\\Local\\pypoetry\\Cache`).\n\n## Execution\n\nTo execute the program use\n```bash\npoetry run python -m gitzip\n```\n',
    'author': 'miile7',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
