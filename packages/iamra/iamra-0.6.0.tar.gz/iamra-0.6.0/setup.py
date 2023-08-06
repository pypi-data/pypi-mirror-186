# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['iamra']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.50,<2.0.0',
 'cryptography>=39.0.0,<40.0.0',
 'requests>=2.28.1,<3.0.0',
 'urllib3>=1.26.13,<2.0.0']

setup_kwargs = {
    'name': 'iamra',
    'version': '0.6.0',
    'description': 'IAM Roles Anywhere credentials helper',
    'long_description': '<!-- cSpell:ignore Codecov, FLYQEXXXXXXZ, Pqss, Xdlc, cjolowicz\n}] -->\n\n# Iamra\n\n[![PyPI](https://img.shields.io/pypi/v/iamra.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/iamra.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/iamra)][python version]\n[![License](https://img.shields.io/pypi/l/iamra)][license]\n\n[![Read the documentation at https://iamra.readthedocs.io/](https://img.shields.io/readthedocs/iamra/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/gadams999/iamra/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/gadams999/iamra/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/iamra/\n[status]: https://pypi.org/project/iamra/\n[python version]: https://pypi.org/project/iamra\n[read the docs]: https://iamra.readthedocs.io/\n[tests]: https://github.com/gadams999/iamra/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/gadams999/iamra\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\nIAM Roles Anywhere credentials helper.\n\nIamra (ahy-em-rah) is a helper library to abstract and make obtaining temporary AWS IAM credentials easy through using [AWS Identity and Access Management Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html). Once configured in the cloud, Iamra sessions can be created, and then when credentials are needed, a single call will update the AWS credentials, that can be directly used via [boto3 session or client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html).\n\n## Features\n\n- Single object per session, allowing for different scoped credentials\n- RSA and EC certificate / private key support\n- Certificate chain support for X.509 certificated signed by an intermediate Certificate Authority\n- Cached credentials within the expiration time to reduce unneeded calls to IAM Roles Anywhere, but can be force-refreshed as needed\n\n## Requirements\n\n- Python 3.9 or later support\n- Creation of a trust anchor and profile [in the cloud](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/getting-started.html)\n- Valid X.509 certificate, private key, and optionally a certificate chain file\n\n## Installation\n\nYou can install _Iamra_ via [pip] from [PyPI]:\n\n<!-- markdownlint-disable -->\n\n```console\n$ pip install iamra\n```\n\n<!-- markdownlint-restore -->\n\n## Usage\n\nBasic usage with local private key and X.509 certificate:\n\n```python\n>>> import iamra\n>>> # Create a session object\n>>> iamra_session = iamra.Credentials(\n       region="us-east-1",\n       certificate_filename="client.pem",\n       private_key_filename="client.key",\n       duration=3600,\n       profile_arn="arn:aws:rolesanywhere:us-west-2:1234567890:profile/3d203fc0-7bba-4ec1-a6ef-697504ce1c72",\n       role_arn="arn:aws:iam::1234567890:role/IamRoleWithPermissionsToUse",\n       session_name="my_client_test_session",\n       trust_anchor_arn="arn:aws:rolesanywhere:us-west-2:1234567890:trust-anchor/29efd0b1-1b66-4df4-8ae7-e935716efd8e",\n)\n>>> # Invoke getting credentials from Roles Anywhere\n>>> iamra_session.get_credentials()\n>>> # Directly access credentials\n>>> iamra_session.access_key_id\n\'ASIA5FLYQEXXXXXXZ27N\'\n>>> iamra_session.secret_access_key\n\'HhAViXXXXqIZrq/qENC4ahPqssXXXX9DEfx3mTv\'\n>>> iamra_session.session_token\n\'IQoJb3JpZ2luX2VjEMf//////////wEaCXVzLXdlc3QtMiJ...fARzrFrr0VEpiqFY42NWjFdFUhdLkPiuhsLoTYH+OnaGl92OxAho3j0=\'\n```\n\n## Documentation\n\n[Here](https://iamra.readthedocs.io/en/latest/) is the documentation that covers additional usage and module reference.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Iamra_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]\'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/gadams999/iamra/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/gadams999/iamra/blob/main/LICENSE\n[contributor guide]: https://github.com/gadams999/iamra/blob/main/CONTRIBUTING.md\n',
    'author': 'Gavin Adams',
    'author_email': 'me@gavinadams.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gadams999/iamra',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
