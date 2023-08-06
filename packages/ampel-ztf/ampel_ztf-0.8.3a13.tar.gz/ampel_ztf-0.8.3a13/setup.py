# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ampel',
 'ampel.template',
 'ampel.util',
 'ampel.ztf',
 'ampel.ztf.alert',
 'ampel.ztf.alert.load',
 'ampel.ztf.base',
 'ampel.ztf.dev',
 'ampel.ztf.ingest',
 'ampel.ztf.t0',
 'ampel.ztf.t0.load',
 'ampel.ztf.t1',
 'ampel.ztf.t2',
 'ampel.ztf.t3',
 'ampel.ztf.t3.complement',
 'ampel.ztf.t3.resource',
 'ampel.ztf.t3.select',
 'ampel.ztf.t3.skyportal',
 'ampel.ztf.util',
 'ampel.ztf.view']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.3,<4.0.0',
 'ampel-alerts>=0.8.3-beta.5,<0.9.0',
 'ampel-core>=0.8.3-beta.21,<0.9.0',
 'ampel-interface>=0.8.3-beta.14,<0.9.0',
 'ampel-photometry>=0.8.3-alpha.3,<0.9.0',
 'astropy>=5.0,<6.0',
 'backoff>=2.0.0,<3.0.0',
 'fastavro>=1.6.0,<1.7.0',
 'matplotlib>=3.3.4,<4.0.0',
 'nest-asyncio>=1.4.3,<2.0.0',
 'requests-toolbelt>=0.10.0,<0.11.0',
 'requests>=2.25.1,<3.0.0',
 'scipy>=1.9.3,<2.0.0']

extras_require = \
{'archive': ['ampel-ztf-archive>=0.8.0-alpha.0,<0.9.0'],
 'fp': ['pandas>=1.5.2,<2.0.0', 'planobs>=0.6.1,<0.7.0'],
 'healpix': ['healpy>=1.15,<2.0'],
 'kafka': ['confluent-kafka>=1.5.0,<2.0.0'],
 'light-curve': ['light-curve>=0.6,<0.7'],
 'plot': ['ampel-plot>=0.8.3,<0.9.0']}

setup_kwargs = {
    'name': 'ampel-ztf',
    'version': '0.8.3a13',
    'description': 'Zwicky Transient Facility support for the Ampel system',
    'long_description': '\n\n<img align="left" src="https://desycloud.desy.de/index.php/s/6gJs9bYBG3tWFDz/preview" width="150" height="150"/>  \n<br>\n\n# ZTF support for AMPEL\n\n<br><br>\nZTF-specific implementations for Ampel such as:\n\n- An _AlertSupplier_ compatible with IPAC generated alerts\n- Shaper classes for ingestion\n- Encoding utilities for ZTF names (AMPEL requires integer ids)\n- Classes for archiving alerts\n',
    'author': 'Valery Brinnel',
    'author_email': 'None',
    'maintainer': 'Jakob van Santen',
    'maintainer_email': 'jakob.van.santen@desy.de',
    'url': 'https://ampelproject.github.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
