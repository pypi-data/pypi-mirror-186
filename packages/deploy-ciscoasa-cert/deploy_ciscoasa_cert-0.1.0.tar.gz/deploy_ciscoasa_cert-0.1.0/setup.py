# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deploy_ciscoasa_cert']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0',
 'pyopenssl>=23.0.0,<24.0.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['deploy-ciscoasa-cert = deploy_ciscoasa_cert.main:app']}

setup_kwargs = {
    'name': 'deploy-ciscoasa-cert',
    'version': '0.1.0',
    'description': 'Tool to upload and install a certificate on Cisco ASA',
    'long_description': '# deploy-ciscoasa-cert\n\nDeploy a certificate to a Cisco ASA using the REST API',
    'author': 'Billy Zoellers',
    'author_email': 'billy.zoellers@mac.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
