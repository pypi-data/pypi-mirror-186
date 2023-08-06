# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hopprcop',
 'hopprcop.combined',
 'hopprcop.gemnasium',
 'hopprcop.grype',
 'hopprcop.hoppr_plugin',
 'hopprcop.ossindex',
 'hopprcop.ossindex.api',
 'hopprcop.trivy']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'coverage>=6.5.0,<7.0.0',
 'cvss>=2.5,<3.0',
 'hoppr-cyclonedx-models>=0.2.1,<0.3.0',
 'hoppr-security-commons>=0.0.6,<0.0.7',
 'hoppr>=1.6.2,<2.0.0',
 'mkdocs-mermaid2-plugin>=0.6.0,<0.7.0',
 'mkdocs>=1.3.1,<2.0.0',
 'packageurl-python>=0.10.1,<0.11.0',
 'pytest==7.2.0',
 'rich>=12.5.1,<13.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'tinydb>=4.7.0,<5.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['hoppr-cop = hopprcop.combined.cli:app']}

setup_kwargs = {
    'name': 'hoppr-cop',
    'version': '1.0.18',
    'description': '',
    'long_description': 'None',
    'author': 'kganger',
    'author_email': 'keith.e.ganger@lmco.com',
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
