# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sentry_dynamic_sampling_lib']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.9.4,<6.0.0',
 'pytest>=7.2.0,<8.0.0',
 'requests-cache>=0.9.7,<0.10.0',
 'schedule>=1.1.0,<2.0.0',
 'wrapt>=1.14.1,<2.0.0']

setup_kwargs = {
    'name': 'sentry-dynamic-sampling-lib',
    'version': '1.1.2a1',
    'description': 'This project aims to provide dynamic sampling without relying on Sentry Dynamic Sampling.',
    'long_description': '# Sentry Dynamic Sampling Controller\n\n[![PyPI](https://img.shields.io/pypi/v/sentry-dynamic-sampling-lib?color=blue)](https://pypi.org/project/sentry-dynamic-sampling-lib/)\n![Tests Status](https://github.com/SpikeeLabs/sentry-dynamic-sampling-lib/actions/workflows/.github/workflows/test.yml/badge.svg)\n[![codecov](https://codecov.io/gh/SpikeeLabs/sentry-dynamic-sampling-lib/branch/main/graph/badge.svg?token=NK5V6YMWW0)](https://codecov.io/gh/SpikeeLabs/sentry-dynamic-sampling-lib)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sentry-dynamic-sampling-lib)\n![PyPI - License](https://img.shields.io/pypi/l/sentry-dynamic-sampling-lib)\n\n---\nThis project aims to provide dynamic sampling without relying on Sentry own\'s Dynamic Sampling.\nThis libs works by adding a `traces_sampler` callback to sentry.\nIn the background a thread fetch the data from the [controller](https://github.com/SpikeeLabs/sentry-dynamic-sampling-controller)\nIt\'s also able to ignore WSGI route an Celery task set in controller.\n\n\n\n\n\n## Usage\n```python\nimport sentry_sdk\nfrom sentry_dynamic_sampling_lib import init_wrapper\n\n# init sentry as usual\n# without traces_sampler and sample_rate param\nsentry_sdk.init(  # pylint: disable=E0110\n    dsn=SENTRY_DSN,\n    integrations=[],\n    environment=ENVIRONMENT,\n    release=SENTRY_RELEASE,\n)\n\n# hook sentry_dynamic_sampling_lib into sentry\ninit_wrapper()\n```\n\n\n## Configuration\nThe following environment variables can be used to configure the lib\n\n```bash\nSENTRY_CONTROLLER_HOST=none # (required, no default)\nSENTRY_CONTROLLER_PATH="/sentry/apps/{}/" # (optional, default to example)\nSENTRY_CONTROLLER_METRIC_PATH="/sentry/apps/{}/metrics/{}/" # (optional, default to example)\nSENTRY_CONTROLLER_POLL_INTERVAL=60 # (optional, default to example)\nSENTRY_CONTROLLER_METRIC_INTERVAL=600 # (optional, default to example)\n```\n\n\n\n\n## Development\n```bash\n# install deps\npoetry install\n\n# pre-commit\npoetry run pre-commit install --install-hook\npoetry run pre-commit install --install-hooks --hook-type commit-msg\n```\n',
    'author': 'jeanloup.monnier',
    'author_email': 'jean-loup.monnier@spikeelabs.fr',
    'maintainer': 'jeanloup.monnier',
    'maintainer_email': 'jean-loup.monnier@spikeelabs.fr',
    'url': 'https://github.com/SpikeeLabs/django-admin-action-tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
