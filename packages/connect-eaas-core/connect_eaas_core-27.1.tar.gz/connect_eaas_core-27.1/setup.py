# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['connect',
 'connect.eaas.core',
 'connect.eaas.core.inject',
 'connect.eaas.core.testing',
 'connect.eaas.core.validation',
 'connect.eaas.core.validation.validators']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'anvil-uplink>=0.4.0,<0.5.0',
 'connect-openapi-client>=25.15',
 'fastapi-utils>=0.2.1,<0.3.0',
 'fastapi>=0.78.0,<0.79.0',
 'logzio-python-handler>=3.1.1,<4.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'pytest11': ['pytest_eaas_core = connect.eaas.core.testing.fixtures']}

setup_kwargs = {
    'name': 'connect-eaas-core',
    'version': '27.1',
    'description': 'Connect Eaas Core',
    'long_description': '# Connect Extension as a Service Core Library\n\n![pyversions](https://img.shields.io/pypi/pyversions/connect-eaas-core.svg) [![PyPi Status](https://img.shields.io/pypi/v/connect-eaas-core.svg)](https://pypi.org/project/connect-eaas-core/) [![Build Status](https://github.com/cloudblue/connect-eaas-core/workflows/Build%20Connect%20EaaS%20Core/badge.svg)](https://github.com/cloudblue/connect-eaas-core/actions) [![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=connect-eaas-core&metric=alert_status)](https://sonarcloud.io/dashboard?id=connect-eaas-core) \n [![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=connect-eaas-core&metric=coverage)](https://sonarcloud.io/component_measures/metric/coverage/list?id=connect-eaas-core)\n [![SonarCloud Bugs](https://sonarcloud.io/api/project_badges/measure?project=connect-eaas-core&metric=bugs)](https://sonarcloud.io/component_measures/metric/reliability_rating/list?id=connect-eaas-core)\n [![SonarCloud Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=connect-eaas-core&metric=vulnerabilities)](https://sonarcloud.io/component_measures/metric/security_rating/list?id=connect-eaas-core)\n\n\n\n\n## Introduction\n\n`Connect EaaS Core` is a library that contains the base building blocks to develop extensions for the CloudBlue Connect platform.\n\n\n## Install\n\n`Connect EaaS Core` requires python 3.8 or later.\n\n\n`Connect EaaS Core` can be installed from [pypi.org](https://pypi.org/project/connect-eaas-core/) using pip:\n\n```\n$ pip install connect-eaas-core\n```\n\n\n## Documentation\n\n[`Connect EaaS Core` documentation](https://connect-eaas-core.readthedocs.io/en/latest/) is hosted on the _Read the Docs_ service.\n\n\n## License\n\n`Connect EaaS Core` is released under the [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).\n',
    'author': 'CloudBlue LLC',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://connect.cloudblue.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
