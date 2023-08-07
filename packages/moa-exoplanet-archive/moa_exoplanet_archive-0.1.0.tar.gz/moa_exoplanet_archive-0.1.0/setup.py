# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moa_exoplanet_archive']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=5.2.1,<6.0.0',
 'backports-strenum>=1.1.1,<2.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'pysftp>=0.2.9,<0.3.0',
 'tabulate>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['moa_exoplanet_archive_merge_transfer = '
                     'moa_exoplanet_archive.merge_transfer_cli:merge_transfer']}

setup_kwargs = {
    'name': 'moa-exoplanet-archive',
    'version': '0.1.0',
    'description': '',
    'long_description': 'MOA Exoplanet Archive',
    'author': 'Greg Olmschenk',
    'author_email': 'greg@olmschenk.com',
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
