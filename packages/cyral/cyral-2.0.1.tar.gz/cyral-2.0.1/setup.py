# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cyral', 'cyral.cli', 'cyral.sdk', 'cyral.sdk.api']

package_data = \
{'': ['*']}

install_requires = \
['awscli>=1.25,<2.0',
 'click>=8.1,<9.0',
 'columnar>=1.4,<2.0',
 'oauthlib>=3.2,<4.0',
 'requests>=2.28,<3.0']

entry_points = \
{'console_scripts': ['cyral = cyral.cli.__main__:main']}

setup_kwargs = {
    'name': 'cyral',
    'version': '2.0.1',
    'description': 'The Cyral CLI tool',
    'long_description': '# The Cyral CLI Tool\n\nUse this tool to obtain credentials for accessing a data repo via the Cyral sidecar.\n\n**Note 1** This tool does not work with Cyral versions before 3.0. If you are using an\nolder version of Cyral, please use the [gimme-db-token](https://pypi.org/project/cyral-gimme-db-token/)\ntool instead.\n\n**Note 2** Use version 1.x of this tool for Cyral version 3.X and version 2.x for Cyral version 4.X and greater.\n\n## Usage\n\n```\ncyral <global options> <command> <subcommand> <command options>\n```\n\nFor detailed usage instructions:\n\n```bash\ncyral --help\n```\n\n### Global Options\n\n- `--cp-address <control plane address>` Cyral Control Plane Address, e.g., `mycompany.app.cyral.com` (the address may need a :8000 suffix in some cases).\n- `--idp <idp alias>` The identity provider to use for authentication.\n- `--offline-access` Obtain a long-lived offline access token for authentication to the control plane.\n- `--no-stored-creds` Do not store or use a stored refresh token.\n- `--version` Show package version and exit.\n- `--help` Show command help.\n\n### Top Level Commands\n\nThe only top level command currently supported is `access`. It has the following subcommands.\n\n- `token` Print a token for authenticating to a repo using your email address as user name.\n- `repo` Show list of accessible data repos and print connection information for the selected repo.\n  + Use `--type`, `--tag`, `--name` options to specify repo filters.\n- `s3` Write configuration needed to access S3 to AWS config files.\n- `pg` Write configuration needed to access selected postgres database to `.pgpass` file.\n\n',
    'author': 'Deepak Gupta',
    'author_email': 'deepak@cyral.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
