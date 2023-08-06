# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src',
 'flex_ansible': 'src/flex_ansible',
 'flex_ansible.command': 'src/flex_ansible/command',
 'flex_ansible.command.wrapper': 'src/flex_ansible/command/wrapper',
 'flex_cli': 'src/flex_cli',
 'flex_cli.application': 'src/flex_cli/application',
 'flex_cli.command': 'src/flex_cli/command',
 'flex_cli.command.wrapper': 'src/flex_cli/command/wrapper',
 'flex_cli.config': 'src/flex_cli/config',
 'flex_cli.etc': 'src/flex_cli/etc',
 'flex_cli.handler': 'src/flex_cli/handler',
 'flex_framework': 'src/flex_framework',
 'flex_framework.api': 'src/flex_framework/api',
 'flex_framework.api.command': 'src/flex_framework/api/command',
 'flex_framework.application': 'src/flex_framework/application',
 'flex_framework.config': 'src/flex_framework/config',
 'flex_framework.config.deployment': 'src/flex_framework/config/deployment',
 'flex_framework.config.discover': 'src/flex_framework/config/discover',
 'flex_framework.config.reader': 'src/flex_framework/config/reader',
 'flex_framework.console': 'src/flex_framework/console',
 'flex_framework.environment': 'src/flex_framework/environment',
 'flex_framework.shell': 'src/flex_framework/shell'}

packages = \
['flex_ansible',
 'flex_ansible.command',
 'flex_ansible.command.wrapper',
 'flex_cli',
 'flex_cli.application',
 'flex_cli.command',
 'flex_cli.command.wrapper',
 'flex_cli.config',
 'flex_cli.etc',
 'flex_cli.handler',
 'flex_framework',
 'flex_framework.api',
 'flex_framework.api.command',
 'flex_framework.application',
 'flex_framework.config',
 'flex_framework.config.deployment',
 'flex_framework.config.discover',
 'flex_framework.config.reader',
 'flex_framework.console',
 'flex_framework.environment',
 'flex_framework.shell',
 'lcli',
 'lcli.app_mode',
 'lcli.command',
 'lcli.input',
 'lcli.tools']

package_data = \
{'': ['*'],
 'lcli': ['config/*',
          'config/samples/*',
          'config/samples/ansible/*',
          'config/samples/ansible/inventory/*',
          'config/samples/ansible/playbooks/*',
          'config/samples/ansible/playbooks/roles/webservers.performance/tasks/*',
          'config/samples/ansible/playbooks/roles/webservers.security/tasks/*',
          'config/samples/commands/*',
          'config/samples/commands/opdocker/*',
          'config/samples/prototypes/*',
          'config/schema/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'blessings>=1.7,<2.0',
 'fire>=0.4,<0.6',
 'jsonschema>=4.5,<5.0',
 'pinject>=0.14,<0.15',
 'prompt-toolkit>=3.0,<4.0',
 'pyfiglet>=0.8,<0.9',
 'types-PyYAML']

extras_require = \
{'ansible': ['ansible>=6.4,<7.0']}

entry_points = \
{'console_scripts': ['fcli = lcli.__main__:main',
                     'flex-cli = flex_cli.__main__:main',
                     'lcli = lcli.__main__:main']}

setup_kwargs = {
    'name': 'flex-cli',
    'version': '0.1.35',
    'description': "Local CLI is an extendable interactive command line tool built in mind with the objective to make the interaction with day to day scripts more user friendly. The scripts you use daily should be easy to maintain, develop and document so you don't need to worry to write long documents on how to use them.",
    'long_description': '# Introduction\n\n[![PyPI version](https://img.shields.io/pypi/v/flex-cli.svg)](https://pypi.org/project/flex-cli)\n[![Build Status](https://github.com/a42ss/flex-cli/actions/workflows/python-package.yml/badge.svg)](https://github.com/a42ss/flex-cli/actions/workflows/python-package.yml)\n[![Coverage badge](https://raw.githubusercontent.com/a42ss/flex-cli/python-coverage-comment-action-data/badge.svg)](https://github.com/a42ss/flex-cli/tree/python-coverage-comment-action-data)\n[![CodeQL](https://github.com/a42ss/flex-cli/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/a42ss/flex-cli/actions/workflows/codeql-analysis.yml)\n[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6480/badge)](https://bestpractices.coreinfrastructure.org/projects/6480)\n[![Docs badge](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://flex-cli.readthedocs.io/en/latest)\n[![Chat badge](https://img.shields.io/badge/chat-IRC-brightgreen.svg)](https://github.com/a42ss/flex-cli/discussions)\n[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://flex-cli.readthedocs.io/en/latest)\n\n   \n\nLocal development productivity tools meant to smooth and ease developers day to day work. \nIt is meant to be cross-platform but for now is tested using MacOs and Ubuntu\n\n## This are few examples\n\n* unified command line interfaces for multiple cli tools\n* interactive command line mode\n\n  - this act as an interactive wrapper on top of existing cli tools\n  - also allow extending the existing cli tools with auto-completion, input enhanced wizard or description\n  - allow switching between command namespaces in the same terminal\n\n* Implement custom CLI tools using Python, fully integrate with all LCLI tool features:\n  - just write some code class or function and configure them to be wired in application\n\n* use Fire to auto document Python objects, so all you should do is to focus on business logic\n   \n# Features\n\n## Fire mode\n\nIn fire mode the application allow user to configure a hierarchy of objects that fit its needs for various project.\nThe user can navigate and execute the hierarchy using Fire library by Google. \n"Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object."\nhttps://github.com/google/python-fire\n\n## Interactive mode\n\nMost often during the development process developers are using various tools for various projects.\nThe interactive mode purpose is to improve productivity by offering auto-completion details on the spot.\nThis is implemented on top of python cmd package: https://docs.python.org/3/library/cmd.html\n\n# Getting Started\n\n## Installation process\n\nInstall from source\n\n```bash\n# Using invoke\ninvoke install\n#from project root directory\n./install\n#or \npython3 -m pip install -r requirements.txt\npython3 -m pip install . --user\n```\n\n## Software dependencies\n\nThis is a Python package available as MIT License and is depending on following packages:\n \n* fire https://github.com/google/python-fire/releases\n* pinject https://github.com/google/pinject/releases\n* PyYAML\n* prompt_toolkit\n* pyfiglet\n* blessings\n* tk\n* appJar\n* jsonschema\n\n## Latest releases\n\n- V-0.2.2 - First released version. \n\n## API references\n\n# Build and Test\n\n## Build\n\n```bash\n# Using invoke\ninvoke build\n```\n\n## Test\n\n```bash\n# Using invoke\ninvoke test\ninvoke coverage\n# Using pytest\npy.test\npytest --cov=src/lcli/ .\n```\n\n# Use cases\n\n[<img src="https://img.youtube.com/vi/L9orYXE1nlU/hqdefault.jpg" width="50%">](https://youtu.be/L9orYXE1nlU)\n\n# Usage\n\n\n## Configuration\n\n# Author\n\n[George Babarus](https://github.com/georgebabarus)\n\n# Contribute\n\nFeel free to contribute to this project and make developer life essayer:\n- by submitting new ideas as a github issue [here](https://github.com/georgebabarus/lcli/issues/new)\n- by making pull request with specific bug fixes\n- for new features or architectural change please contact [George Babarus](https://github.com/georgebabarus) to avoid double work on any way.\n\n# Useful links\n\n* https://mypy.readthedocs.io/en/latest/generics.html#generics\n* https://code-maven.com/interactive-shell-with-cmd-in-python\n* https://www.journaldev.com/16140/python-system-command-os-subprocess-call\n* https://stackoverflow.com/questions/3262569/validating-a-yaml-document-in-python\n* https://github.com/oclif/oclif#-cli-types\n* https://medium.com/the-z/getting-started-with-oclif-by-creating-a-todo-cli-app-b3a2649adbcf\n* https://opensource.com/article/17/5/4-practical-python-libraries\n\n',
    'author': 'George Babarus',
    'author_email': 'george.babarus@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/a42ss/lcli',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
