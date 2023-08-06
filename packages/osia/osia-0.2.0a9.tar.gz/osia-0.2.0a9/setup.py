# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['osia',
 'osia.config',
 'osia.installer',
 'osia.installer.clouds',
 'osia.installer.dns',
 'osia.installer.downloader',
 'osia.installer.templates',
 'osia.installer.webhooks']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4',
 'boto3',
 'coloredlogs',
 'dynaconf[yaml]',
 'gitpython',
 'jinja2',
 'openstacksdk<=0.61']

entry_points = \
{'console_scripts': ['osia = osia.cli:main_cli']}

setup_kwargs = {
    'name': 'osia',
    'version': '0.2.0a9',
    'description': 'OpenShift infra automation',
    'long_description': "# OSIA\n\nOpenShift infra automation.\n\n## Goal\n\nThe tool aims to unified installer of OpenShift to various clouds which is\neasy to automate and use within CI.\n\nTo see necessary steps for OpenShift installation please see [OpenShift documentation](https://docs.openshift.com).\n\nTo see full documentation of `osia` please follow to [Official documentation](https://redhat-cop.github.io/osia).\n\n## Installation\n\nTo get started with osia, just install available package from [pypi](pypi.org):\n\n```bash\n$ pip install osia\n```\n\n\n__Main features__\n\n* Find empty region in aws to install opneshift on.\n* Find feasible network in OpenStack and allocate FIPs before installation happens.\n* Generate `install-config.yaml` from predefined defaults.\n* Store generated files for deletion to git repository and push changes right after the cluster is installed.\n* Manage DNS entries based on the installation properties and results.\n* Clean everything once the cluster is not needed.\n\n\n\n\n## Usage\n\nThe tool operates over directory which is expected to be git repository and where the service will\nstore generated configuration and push it to the upstream repository of currently working branch.\n\n### Common configuration\n\nThe common configuraiton is done by yaml file called `settings.yaml` that should be located at\n`CWD` (root of the repository in most cases).\n\nThe configuration has following structure:\n\n```\ndefault:\n  cloud:\n    openstack:\n      cloud_env: env1\n      environments:\n      - name: env1\n        base_domain: ''\n        certificate_bundle_file: ''\n        pull_secret_file: ''\n        ssh_key_file: ''\n        osp_cloud: ''\n        osp_base_flavor: ''\n        network_list: []\n      - name: env2\n        base_domain: ''\n        certificate_bundle_file: ''\n        pull_secret_file: ''\n        ssh_key_file: ''\n        osp_cloud: ''\n        osp_base_flavor: ''\n        network_list: []\n    aws:\n      cloud_env: default\n      environments:\n      - name: default\n        base_domain: ''\n        pull_secret_file: ''\n        certificate_bundle_file: ''\n        ssh_key_file: ''\n        worker_flavor: '' \n        list_of_regions: []\n  dns:\n    route53:\n      ttl: 0\n    nsupdate:\n      server: ''\n      zone: ''\n      key_file: ''\n      ttl: 0 \n      use_ipv4: false\n```\n\nEvery key here is overridible by the argument passed to the installer.\nFor explanation of any key, please check he documentation below.\n\n",
    'author': 'Miroslav Jaros',
    'author_email': 'mirek@mijaros.cz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
