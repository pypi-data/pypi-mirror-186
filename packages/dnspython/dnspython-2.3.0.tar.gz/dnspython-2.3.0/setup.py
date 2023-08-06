# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dns',
 'dns.quic',
 'dns.rdtypes',
 'dns.rdtypes.ANY',
 'dns.rdtypes.CH',
 'dns.rdtypes.IN']

package_data = \
{'': ['*']}

extras_require = \
{'curio': ['curio>=1.2,<2.0', 'sniffio>=1.1,<2.0'],
 'dnssec': ['cryptography>=2.6,<40.0'],
 'doh': ['requests-toolbelt>=0.9.1,<0.11.0', 'requests>=2.23.0,<3.0.0'],
 'doh:python_full_version >= "3.6.2"': ['httpx>=0.21.1', 'h2>=4.1.0'],
 'doq': ['aioquic>=0.9.20'],
 'idna': ['idna>=2.1,<4.0'],
 'trio': ['trio>=0.14,<0.23'],
 'wmi': ['wmi>=1.5.1,<2.0.0']}

setup_kwargs = {
    'name': 'dnspython',
    'version': '2.3.0',
    'description': 'DNS toolkit',
    'long_description': "# dnspython\n\n[![Build Status](https://github.com/rthalley/dnspython/actions/workflows/python-package.yml/badge.svg)](https://github.com/rthalley/dnspython/actions/)\n[![Documentation Status](https://readthedocs.org/projects/dnspython/badge/?version=latest)](https://dnspython.readthedocs.io/en/latest/?badge=latest)\n[![PyPI version](https://badge.fury.io/py/dnspython.svg)](https://badge.fury.io/py/dnspython)\n[![License: ISC](https://img.shields.io/badge/License-ISC-brightgreen.svg)](https://opensource.org/licenses/ISC)\n[![Coverage](https://codecov.io/github/rthalley/dnspython/coverage.svg?branch=master)](https://codecov.io/github/rthalley/dnspython)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## INTRODUCTION\n\ndnspython is a DNS toolkit for Python. It supports almost all record types. It\ncan be used for queries, zone transfers, and dynamic updates. It supports TSIG\nauthenticated messages and EDNS0.\n\ndnspython provides both high and low level access to DNS. The high level classes\nperform queries for data of a given name, type, and class, and return an answer\nset. The low level classes allow direct manipulation of DNS zones, messages,\nnames, and records.\n\nTo see a few of the ways dnspython can be used, look in the `examples/`\ndirectory.\n\ndnspython is a utility to work with DNS, `/etc/hosts` is thus not used. For\nsimple forward DNS lookups, it's better to use `socket.getaddrinfo()` or\n`socket.gethostbyname()`.\n\ndnspython originated at Nominum where it was developed\nto facilitate the testing of DNS software.\n\n## ABOUT THIS RELEASE\n\nThis is dnspython 2.3.0.\nPlease read\n[What's New](https://dnspython.readthedocs.io/en/stable/whatsnew.html) for\ninformation about the changes in this release.\n\n## INSTALLATION\n\n* Many distributions have dnspython packaged for you, so you should\n  check there first.\n* If you have pip installed, you can do `pip install dnspython`\n* If not just download the source file and unzip it, then run\n  `sudo python setup.py install`\n* To install the latest from the master branch, run `pip install git+https://github.com/rthalley/dnspython.git`\n\nDnspython's default installation does not depend on any modules other than\nthose in the Python standard library.  To use some features, additional modules\nmust be installed.  For convenience, pip options are defined for the\nrequirements.\n\nIf you want to use DNS-over-HTTPS, run\n`pip install dnspython[doh]`.\n\nIf you want to use DNSSEC functionality, run\n`pip install dnspython[dnssec]`.\n\nIf you want to use internationalized domain names (IDNA)\nfunctionality, you must run\n`pip install dnspython[idna]`\n\nIf you want to use the Trio asynchronous I/O package, run\n`pip install dnspython[trio]`.\n\nIf you want to use the Curio asynchronous I/O package, run\n`pip install dnspython[curio]`.\n\nIf you want to use WMI on Windows to determine the active DNS settings\ninstead of the default registry scanning method, run\n`pip install dnspython[wmi]`.\n\nIf you want to try the experimental DNS-over-QUIC code, run\n`pip install dnspython[doq]`.\n\nNote that you can install any combination of the above, e.g.:\n`pip install dnspython[doh,dnssec,idna]`\n\n### Notices\n\nPython 2.x support ended with the release of 1.16.0.  Dnspython 2.0.0 through\n2.2.x support Python 3.6 and later.  As of dnspython 2.3.0, the minimum\nsupported Python version will be 3.7.  We plan to align future support with the\nlifetime of the Python 3 versions.\n\nDocumentation has moved to\n[dnspython.readthedocs.io](https://dnspython.readthedocs.io).\n",
    'author': 'Bob Halley',
    'author_email': 'halley@dnspython.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.dnspython.org',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
