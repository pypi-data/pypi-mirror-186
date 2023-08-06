# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyldb']

package_data = \
{'': ['*'], 'pyldb': ['extra/css/*', 'templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'suds-py3>=1.4.5.0,<2.0.0.0']

setup_kwargs = {
    'name': 'pyldb',
    'version': '0.6.0',
    'description': 'Python interface to the Live Departure Boards',
    'long_description': "# pyLDB - Python interface to the Live Departure Boards\n\n[![PyPI](https://img.shields.io/pypi/v/pyldb.svg)](https://pypi.python.org/pypi/pyldb)\n[![PyPI](https://img.shields.io/pypi/dm/pyldb.svg)](https://pypi.python.org/pypi/pyldb)\n[![PyPI](https://img.shields.io/pypi/l/pyldb.svg)](https://pypi.python.org/pypi/pyldb)\n[![Build Status](https://travis-ci.org/jwg4/pyldb.svg?branch=master)](https://travis-ci.org/jwg4/pyldb)\n\nA simple library for getting live departure boards from the National Rail Enquiries Darwin service (via OpenLDBWS). Designed to wrap the SOAP code with a simple interface.\n\nThis library is currently minimal but functional. See `sample/get_board.py` for an example of how to retrieve the current departure board for a station and render it to an HTML page.\n\nTo run this code you will need your own access token which you have to get from National Rail Enquiries.\n\nIf you're not in the UK or not interested in train data from the UK, this code probably won't help you.\n\n## Technical\nThis library relies on two others: suds to do a SOAP call into the LDBWS service, and jinja2 for the HTML templating.\n\nSOAP is a framework for remote APIs, typically over HTTP but other transport layers are supported, which predates REST. It uses XML, and relies on XML documents in a WSDL language to define the specifics of the API, including function signatures and all the custom types used by the API. It's usually a bit more complicated to setup a SOAP connection than to hit a REST api, but the use of strong types can make them very powerful. The code in this library provides a minimal proof of concept of how to retrieve live departure board data from the SOAP service using Python. For some peope that might be all you need.\n\nDue to the choice of a port of suds to Python 3, this library does not currently work at all with Python 2. It is testing with Python versions 3.4, 3.5 and 3.6.\n\nJinja2 is an awesome templating library for Python which is used in Flask and Ansible among many other projects. Its use here is straightforward, and if you look at the basic HTML template, you can probably figure out how to write a template for either a differently structured HTML document, or a different document type altogether.\n\nNational Rail Enquiries is a UK organization which provides information about train times and fares on the National Rail system. The Live Departure Board service is a web API which shows trains scheduled to depart from a given station, along with information about their expected departure times, etc. This is the same data, updated live, which is used in mapping apps - since 2015 it is also the same data shown on departure boards in train stations, since these boards also rely on the same API.\n\n## See also\nThis code is libre software and might help you get your own project working. There are several other projects which get train departure boards using Python:\n - [helenst/train-times-display](https://github.com/helenst/train-times-display) Scrapes the NRE website and writes to a LCD display.\n - [grundleborg/nrewebservices](https://github.com/grundleborg/nrewebservices) A library which works with Python 2 and 3. Uses `suds-jurko`.\n - [robert-b-clarke/nre-darwin-py](https://github.com/robert-b-clarke/nre-darwin-py) An 'abstraction layer` for LDBWS. Also uses `suds-jurko`, also Python 2 and 3.\n - [Diaolou/PiTrains](https://github.com/Diaolou/PiTrains) Uses `nre-darwin-py` (above) to display train departures on a Raspberry Pi using LEDs.\n\n## Important\nNational Rail Enquiries is the data provider for the API which this code wraps. However, this library is not approved, endorsed or supported by National Rail Enquiries. Information about Darwin Data Feeds provided by NRE (of which LDBWS is one) is at (https://www.nationalrail.co.uk/100296.aspx).",
    'author': 'Jack Grahl',
    'author_email': 'jack.grahl@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
