# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yarndevtools',
 'yarndevtools.cdsw',
 'yarndevtools.cdsw.job_configs',
 'yarndevtools.cdsw.libreloader',
 'yarndevtools.cdsw.scripts.experiments',
 'yarndevtools.commands',
 'yarndevtools.commands.branchcomparator',
 'yarndevtools.commands.reviewsheetbackportupdater',
 'yarndevtools.commands.reviewsync',
 'yarndevtools.commands.unittestresultaggregator',
 'yarndevtools.commands.unittestresultaggregator.common',
 'yarndevtools.commands.unittestresultaggregator.db',
 'yarndevtools.commands.unittestresultaggregator.email',
 'yarndevtools.commands.unittestresultfetcher',
 'yarndevtools.commands.upstreamumbrellafetcher',
 'yarndevtools.common']

package_data = \
{'': ['*'],
 'yarndevtools.cdsw': ['resources/*',
                       'scripts/*',
                       'unit-test-result-aggregator/*']}

install_requires = \
['bs4',
 'dacite',
 'dataclasses-json',
 'gitpython',
 'google-api-wrapper2==1.0.5',
 'humanize',
 'jira',
 'marshmallow',
 'pymongo',
 'python-common-lib==1.0.6']

entry_points = \
{'console_scripts': ['exec-yarndevtools = yarndevtools.yarn_dev_tools:run']}

setup_kwargs = {
    'name': 'yarn-dev-tools',
    'version': '1.1.4',
    'description': '',
    'long_description': '[![CI for YARN dev tools (pip)](https://github.com/szilard-nemeth/yarn-dev-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/szilard-nemeth/yarn-dev-tools/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/szilard-nemeth/yarn-dev-tools/branch/master/graph/badge.svg?token=OQD6FIFF7I)](https://codecov.io/gh/szilard-nemeth/yarn-dev-tools)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n![GitHub language count](https://img.shields.io/github/languages/count/szilard-nemeth/yarn-dev-tools)\n\n\n# YARN-dev-tools\n\nThis project contains various developer helper scripts in order to simplify every day tasks related to Apache Hadoop YARN development.\n\n## Main dependencies\n\n* [gitpython](https://gitpython.readthedocs.io/en/stable/) - GitPython is a python library used to interact with git repositories, high-level like git-porcelain, or low-level like git-plumbing.\n* [tabulate](https://pypi.org/project/tabulate/) - python-tabulate: Pretty-print tabular data in Python, a library and a command-line utility.\n* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Beautiful Soup is a Python library for pulling data out of HTML and XML files.\n\n* TODO: Missing dependencies\n\n## Contributing\n\nTODO \n\n## Authors\n\n* **Szilard Nemeth** - *Initial work* - [Szilard Nemeth](https://github.com/szilard-nemeth)\n\n## License\n\nTODO \n\n## Acknowledgments\n\nTODO\n\n# Getting started\n\nIn order to use this tool, you need to have at least Python 3.8 installed.\n\n## Use yarn-dev-tools from package (Recommended)\nIf you don\'t want to tinker with the source code, you can download [yarn-dev-tools](https://pypi.org/project/yarn-dev-tools/#history) from PyPi as well.\nThis is probably the easiest way to use it.\nYou don\'t need to install anything manually as I created a [script](initial_setup.sh) that performs the installation automatically.\nThe script has a `setup-vars` function at the beginning that defines some environment variables:\n\nThese are the following:\n- `YARNDEVTOOLS_ROOT`: Specifies the directory where the Python virtualenv will be created and yarn-dev-tools will be installed to this virtualenv.\n- `HADOOP_DEV_DIR` Should be set to the upstream Hadoop repository root, e.g.: "~/development/apache/hadoop/"\n- `CLOUDERA_HADOOP_ROOT` Should be set to the downstream Hadoop repository root, e.g.: "~/development/cloudera/hadoop/"\n\nThe latter two environment variables is better to be added to your bashrc / zshrc file (depending on what shell you are using) to keep them between the shells.\n\n## Use yarn-dev-tools from source\nIf you want to use yarn-dev-tools from source, first you need to install its dependencies.\nThe project root contains a pyproject.toml file that has all the dependencies listed.\nThe project uses Poetry to resolve the dependencies so you need to [install poetry](https://python-poetry.org/docs/#installation) as well.\nSimply go to the root of this project and execute `poetry install --without localdev`.\nAlternatively, you can run `make` from the root of the project.\n\n## Setting up handy aliases to use yarn-dev-tools\nIf you completed the installation (either by source or by package), you may want to define some shell aliases to use the tool more easily.\nIn my system, I have [these](\nhttps://github.com/szilard-nemeth/linux-env/blob/master/workplace-specific/cloudera/scripts/yarn/setup-yarn-dev-tools-aliases.sh).\nPlease make sure to source this script so that the command \'yarndevtools\' will be available since it\'s defined as a function.\nIt is important to specify `HADOOP_DEV_DIR` and `CLOUDERA_HADOOP_ROOT` as mentioned above, before sourcing the script.\n\nAfter these steps, you will have a basic set of aliases that is enough to get you started.\n\n\n# Setting up yarn-dev-tools with Cloudera CDSW\n\n## Initial setup\n1. Upload the initial setup scripts to the CDSW files, to the root directory (/home/cdsw)\n- [initial-cdsw-setup.sh](yarndevtools/cdsw/scripts/initial-cdsw-setup.sh)\n- [install-requirements.sh](yarndevtools/cdsw/scripts/install-requirements.sh)\n\n2. Create a new CDSW session.\nWait for the session to be launched and open up a terminal by Clicking "Terminal access" on the top menu bar.\n\n\n3. Execute this command:\n```\n~/initial-cdsw-setup.sh user cloudera\n```\n\n\nThe script performs the following actions: \n1. Downloads the scripts that are cloning the upstream and downstream Hadoop repositories + installing yarndevtools itself as a python module.\nThe download location is: `/home/cdsw/scripts`<br>\nPlease note that the files will be downloaded from the GitHub master branch of this repository!\n- [clone_downstream_repos.sh](yarndevtools/cdsw/scripts/clone_downstream_repos.sh)\n- [clone_upstream_repos.sh](yarndevtools/cdsw/scripts/clone_upstream_repos.sh)\n\n2. Executes the script described in step 2. \nThis can take some time, especially cloning Hadoop.\nNote: The individual CDSW jobs should make sure for themselves to clone the repositories.\n\n3. Copies the [python-based job configs](yarndevtools/cdsw/job_configs) for all jobs to `/home/cdsw/jobs`\n\n4. All you have to do in CDSW is to set up the projects and their starter scripts like this:\n\n| Project                                                                | Starter script location         | Arguments for script          |\n|------------------------------------------------------------------------|---------------------------------|-------------------------------|\n| Jira umbrella data fetcher (Formerly: Jira umbrella checker reporting) | scripts/start_job.py            | jira-umbrella-data-fetcher    |\n| Unit test result aggregator                                            | scripts/start_job.py            | unit-test-result-aggregator   |\n| Unit test result fetcher (Formerly: Unit test result reporting)        | scripts/start_job.py            | unit-test-result-fetcher      |\n| Branch comparator (Formerly: Downstream branchdiff reporting)          | scripts/start_job.py            | branch-comparator             |\n| Review sheet backport updater                                          | scripts/start_job.py | review-sheet-backport-updater |\n| Reviewsync                                                             | scripts/start_job.py | reviewsync                    |\n\n# Use-cases\n\n\n### Examples for YARN backporter\nTo backport YARN-6221 to 2 branches, run these commands:\n```\nyarn-backport YARN-6221 COMPX-6664 cdpd-master\nyarn-backport YARN-6221 COMPX-6664 CDH-7.1-maint --no-fetch\n```\nThe first argument is the upstream Jira ID<br>\nThe second argument is the downstream Jira ID.<br>\nThe third argument is the downstream branch.<br>\nThe `--no-fetch` option is a means to skip git fetch on both repos.\n\n### How to backport to an already existing relation chain?\n1. Go to Gerrit UI and download the patch.\nFor example: \n```\ngit fetch "https://gerrit.sjc.cloudera.com/cdh/hadoop" refs/changes/29/156429/5 && git checkout FETCH_HEAD\n```\n2. Checkout a new branch\n```\ngit checkout -b my-relation-chain \n```\n\n3. Run backporter with: \n```\nyarn-backport YARN-10314 COMPX-7855 CDH-7.1.7.1000 --no-fetch --downstream_base_ref my-relation-chain\n```\nwhere:<br>\nThe first argument is the upstream Jira ID<br>\nThe second argument is the downstream Jira ID.<br>\nThe third argument is the downstream branch.<br>\nThe `--no-fetch` option is a means to skip git fetch on both repos.<br>\nThe `--downstream_base_ref <local-branch` is a way to use a local branch to base the backport on so the Git remote name won\'t be prepended.\n\n\nFinally, I set up two aliases for pushing the changes to the downstream repo:\n```\nalias git-push-to-cdpdmaster="git push <REMOTE> HEAD:refs/for/cdpd-master%<REVIEWER_LIST>"\nalias git-push-to-cdh71maint="git push <REMOTE> HEAD:refs/for/CDH-7.1-maint%<REVIEWER_LIST>"\n```\nwhere REVIEWER_LIST is in this format: "r=user1,r=user2,r=user3,..."\n\n\n# Contributing\n\n## Setup of pre-commit\n\nConfigure precommit as described in [this blogpost](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/).\n\nCommands:\n1. Install precommit: `pip install pre-commit`\n2. Make sure to add pre-commit to your path. For example, on a Mac system, pre-commit is installed here: \n   `$HOME/Library/Python/3.8/bin/pre-commit`.\n2. Execute `pre-commit install` to install git hooks in your `.git/` directory.\n\n## Running the tests\n\nTODO\n\n## Troubleshooting\n\n### Installation issues\nIn case you\'re facing a similar issue:\n```\nAn error has occurred: InvalidManifestError: \n=====> /<userhome>/.cache/pre-commit/repoBP08UH/.pre-commit-hooks.yaml does not exist\nCheck the log at /<userhome>/.cache/pre-commit/pre-commit.log\n```\n, please run: `pre-commit autoupdate`\n\nMore info can be found [here](https://github.com/pre-commit/pre-commit/issues/577).',
    'author': 'Szilard Nemeth',
    'author_email': 'szilard.nemeth88@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/szilard-nemeth/yarn-dev-tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.12,<4.0.0',
}


setup(**setup_kwargs)
