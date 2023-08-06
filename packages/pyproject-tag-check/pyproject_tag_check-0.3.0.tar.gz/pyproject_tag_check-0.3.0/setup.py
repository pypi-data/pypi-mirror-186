# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyproject_tag_check']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0', 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['pyproject-tag-check = pyproject_tag_check.__init__:main']}

setup_kwargs = {
    'name': 'pyproject-tag-check',
    'version': '0.3.0',
    'description': 'Verify version in pyproject.toml is not already used',
    'long_description': '## pyproject-tag-check\n\nI always forget to bump poetry version in pyproject.toml files. That\'s why I build this simple package. It is pre-commit hook which check that version in pyproject.toml is not used as a tag for given repo URL.\n\n## Usage:\n\n\nPut it in `.pre-commit.config.yaml` repos and argument must be URL to repo on GH (for example this repo itself https://github.com/rafsaf/pyproject-tag-check).\n\n```yml\nrepos:\n  - repo: https://github.com/rafsaf/pyproject-tag-check\n    rev: "0.2.0"\n    hooks:\n      - id: pyproject-tag-check\n        always_run: true\n        args:\n          - https://github.com/rafsaf/pyproject-tag-check\n\n```\n\nUse `always_run: true` if check should be performed always, otherwise it will run only when `pyproject.toml` is changed.\n\n\n`pyproject.toml` usually looks like \n\n```toml\n[tool.poetry]\nname = "some-name..."\nversion = "0.1.0"\n```\nIf tag 0.1.0 already exists like it does for https://github.com/rafsaf/pyproject-tag-check, the check will not pass.',
    'author': 'rafsaf',
    'author_email': 'rafal.safin12@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
