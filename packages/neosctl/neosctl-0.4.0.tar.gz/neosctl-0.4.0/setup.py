# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neosctl']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.13.0,<3.0.0',
 'httpx>=0.23.0,<0.24.0',
 'pydantic>=1.9.2,<2.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['neosctl = neosctl.cli:app']}

setup_kwargs = {
    'name': 'neosctl',
    'version': '0.4.0',
    'description': 'Nortal Core CLI',
    'long_description': '# Core CLI v0.4.0\n\n## Prerequisites\n\nThe following packages are used across python repositories. A global install of them all is _highly_ recommended.\n\n- [Poetry](https://python-poetry.org/docs/#installation)\n- [Invoke](https://www.pyinvoke.org/installing.html)\n- [Kubefwd](https://kubefwd.com)\n\nA running cluster from [Local\nHelm](https://github.com/NEOM-KSA/neos-core-platform/tree/main/demo/helm) with\n`gateway` service port forwarded. Details on port forwarding below.\n\n### WSL\n\nIf running on Windows, you may need to install `distutils` to install the service.\n\n```bash\n$ sudo apt-get install python3.10-distutils\n```\n\n## Initial setup\n\n```bash\n$ invoke install-dev\n```\n\n## Code Quality\n\n### Tests\n\n```bash\ninvoke tests\ninvoke tests-coverage\n```\n\n## Linting\n\n```bash\ninvoke check-style\ninvoke isort\n```\n\n## Running locally\n\n### Port forwarding\n\nTo access the gateway api locally, you will need to connect to the pod inside\nthe cluster using `kubefwd`.\n\n```bash\n$ sudo kubefwd svc -n core -c ~/.kube/config\n```\n\n## Neosctl\n\nWhen running locally, if you do not manage your own virtual environments, you\ncan use poetry to put you in a shell with access to the installed code.\n\n```bash\n$ poetry shell\n```\n\n### Initialize profile\n\n```bash\n$ neosctl -p my-profile profile init\nInitialising [default] profile.\nGateway API url [http://core-gateway.core-gateway:9000/api/gateway]: <http://gateway_api_url:port>\nRegistry API url [http://neos-registry.registry:80/api/registry]: <http://registry_api_url:port>\nIAM API url [http://core-iam.core-iam:80/api/iam]: <http://iam_api_url:port>\nStorage API url [http://core-storage.core-storage:9000/api/storage]: <http://storage_api_url:port>\nUsername: <username>\n```\n\n```bash\n$ cat ~/.neosctl\n```\n\nTo work with the same profile across multiple commands you can export the\nprofile name as an environment variable.\n\n```bash\n$ neosctl -p my-profile product list\n...\n$ export NEOSCTL_PROFILE=my-profile\n$ neosctl product list\n```\n\n### Login\n\n```bash\n$ neosctl -p=<my-profile> auth login\n```\n\n### Commands to work with data products\n\n```bash\n$ neosctl --help\n$ neosctl product --help\n$ neosctl metadata --help\n```\n\nTo work with the same product across multiple commands you can export the\nproduct name as an environment variable.\n\n```bash\n$ neosctl product get my-data-product\n...\n$ export NEOSCTL_PRODUCT=my-data-product\n$ neosctl product get\n```\n\n## Releases\n\nRelease management is handled using `bump2version`. The below commands will tag\na new release. This will also update the helm chart version, this should not be\nmanually changed.\n\n```bash\n$ invoke bump-patch\n$ invoke bump-minor\n$ invoke bump-major\n> vX.Y.Z\n```\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NEOM-KSA/neos-core-platform-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
