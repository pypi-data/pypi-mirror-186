# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ampel',
 'ampel.lsst.alert',
 'ampel.lsst.alert.load',
 'ampel.lsst.aux',
 'ampel.lsst.ingest',
 'ampel.lsst.t0',
 'ampel.lsst.t1',
 'ampel.lsst.t2',
 'ampel.lsst.template',
 'ampel.lsst.view']

package_data = \
{'': ['*']}

install_requires = \
['ampel-ztf[kafka]>=0.8.3a2,<0.8.4',
 'astropy>=5.0.2,<6.0.0',
 'fastavro>=1.3.2,<2.0.0']

setup_kwargs = {
    'name': 'ampel-lsst',
    'version': '0.8.3a1',
    'description': 'Legacy Survey of Space and Time support for the Ampel system',
    'long_description': '\n\n<img align="left" src="https://desycloud.desy.de/index.php/s/25EwEzgpyFMd2bC/preview" width="150" height="150"/>  \n<br>\n\n# LSST plugin for AMPEL\n\n<br><br>\nLSST-specific implementations for Ampel such as:\n\n- An _AlertSupplier_ compatible with plasticc generated alerts\n- Shaper classes for ingestion\n',
    'author': 'Marcus Fenner',
    'author_email': 'mf@physik.hu-berlinn.de',
    'maintainer': 'Marcus Fenner',
    'maintainer_email': 'mf@physik.hu-berlinn.de',
    'url': 'https://ampelproject.github.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
