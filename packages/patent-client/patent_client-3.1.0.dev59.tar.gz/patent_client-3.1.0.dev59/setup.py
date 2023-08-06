# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['patent_client',
 'patent_client.epo',
 'patent_client.epo.ops',
 'patent_client.epo.ops.family',
 'patent_client.epo.ops.legal',
 'patent_client.epo.ops.number_service',
 'patent_client.epo.ops.published',
 'patent_client.epo.ops.published.model',
 'patent_client.epo.ops.published.schema',
 'patent_client.uspto',
 'patent_client.uspto.assignment',
 'patent_client.uspto.peds',
 'patent_client.uspto.ptab',
 'patent_client.uspto.public_search',
 'patent_client.util',
 'patent_client.util.base',
 'patent_client.util.claims',
 'patent_client.util.datetime']

package_data = \
{'': ['*'],
 'patent_client.epo.ops.family': ['fixtures/examples/*', 'fixtures/expected/*'],
 'patent_client.epo.ops.legal': ['test/*', 'test/expected/*'],
 'patent_client.epo.ops.published': ['test/*', 'test/expected/*'],
 'patent_client.uspto.assignment': ['test/*'],
 'patent_client.uspto.peds': ['test/*'],
 'patent_client.uspto.public_search': ['test/*'],
 'patent_client.util.claims': ['examples/*']}

install_requires = \
['PyPDF2>=2.2.0,<3.0.0',
 'PyYAML>=6.0,<7.0',
 'colorlog>=6.6.0,<7.0.0',
 'inflection>=0.5.1,<0.6.0',
 'lxml>=4.9.0,<5.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pyparsing>=3.0.9,<4.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests-cache>=0.9.4,<0.10.0',
 'requests>=2.28.0,<3.0.0',
 'ujson>=5.4.0,<6.0.0',
 'yankee>=0.1.40,<0.2.0',
 'zipp>=3.8.1,<4.0.0']

extras_require = \
{'docs': ['furo>=2022.6,<2023.0',
          'linkify-it-py>=2.0,<3.0',
          'myst-parser>=0.17',
          'sphinx>=5.0.2,<6.0.0',
          'sphinx-autodoc-typehints>=1.19,<2.0',
          'sphinx-automodapi>=0.14',
          'sphinx-copybutton>=0.5',
          'sphinx-design>=0.2',
          'sphinx-notfound-page>=0.8',
          'sphinxcontrib-apidoc>=0.3,<0.4',
          'sphinxcontrib-mermaid>=0.7.1,<0.8.0',
          'nbsphinx>=0.8.9,<0.9.0',
          'IPython>=7.17.0,<8.0.0']}

setup_kwargs = {
    'name': 'patent-client',
    'version': '3.1.0.dev59',
    'description': 'A set of ORM-style clients for publicly available intellectual property data',
    'long_description': '[![patent_client_logo](https://raw.githubusercontent.com/parkerhancock/patent_client/master/docs/_static/patent_client_logo.svg)](https://patent-client.readthedocs.io)\n\n[![Build](https://github.com/parkerhancock/patent_client/actions/workflows/build.yaml/badge.svg)](https://github.com/parkerhancock/patent_client/actions/workflows/build.yaml)\n[![codecov](https://codecov.io/gh/parkerhancock/patent_client/branch/master/graph/badge.svg?token=pWsiQLHi6r)](https://codecov.io/gh/parkerhancock/patent_client)\n[![Documentation](https://img.shields.io/readthedocs/patent-client/stable)](https://patent-client.readthedocs.io/en/stable/)\n\n\n[![PyPI](https://img.shields.io/pypi/v/patent-client?color=blue)](https://pypi.org/project/patent-client)\n[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/patent-client)](https://pypi.org/project/patent-client)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/patent-client?color=blue)](https://pypi.org/project/patent-client)\n\n# Summary\n\nA powerful library for accessing intellectual property, featuring:\n\n- 🍰 **Ease of use:** All sources use a simple unified API inspired by [Django-ORM][DORM].\n- 🐼 **Pandas Integration:** Results are easily castable to [Pandas Dataframes and Series][PANDAS].\n- 🚀 **Performance:** Fetched data is cached using the excellent [requests-cache][requests-cache] library for super-fast queries.\n\nDocs, including a fulsome Getting Started and User Guide are available on [Read the Docs](http://patent-client.readthedocs.io). The Examples folder includes examples of using `patent_client` for\nmany common IP tasks\n\n## Coverage\n\n- [United States Patent & Trademark Office][USPTO]\n\n  - [Patent Public Search][PPS] - Full Support\n  - [Patent Examination Data][PEDS] - Full Support\n  - [Patent Assignment Data][Assignment] - Lookup Support\n  - [Patent Trial & Appeal Board API v2][PTAB] - Supports Proceedings, Decisions, and Documents\n\n\n- [European Patent Office - Open Patent Services][OPS]\n\n  - Inpadoc - Full Support\n  - EPO Register - No Support (in progress)\n  - Classification - No Support\n\n* Free software: Apache Software License 2.0\n\n[DORM]: https://docs.djangoproject.com/en/4.0/topics/db/queries/\n[PANDAS]: https://pandas.pydata.org/docs/\n[requests-cache]: https://github.com/requests-cache/requests-cache\n[Assignment]: https://developer.uspto.gov/api-catalog/patent-assignment-search-beta\n[OPS]: http://ops.epo.org\n[PPS]:  https://ppubs.uspto.gov/pubwebapp/static/pages/landing.html\n[PEDS]: https://developer.uspto.gov/api-catalog/ped\n[PTAB]: https://developer.uspto.gov/api-catalog/ptab-api-v2\n[USPTO]: http://developer.uspto.gov\n\n\n## Installation\n\n```\npip install patent_client\n```\n\nIf you only want access to USPTO resources, you\'re done!\nHowever, additional setup is necessary to access EPO Inpadoc and EPO Register resources. See the [Docs](http://patent-client.readthedocs.io).\n\n\n## Quick Start\n\nTo use the project:\n\n```python\n# Import the model classes you need\n>>> from patent_client import Inpadoc, Assignment, USApplication, PatentBiblio\n\n# Fetch US Patents with the word "tennis" in their title issued in 2010\n>>> pats = PatentBiblio.objects.filter(title="tennis", issue_date="2010-01-01->2010-12-31")\n>>> len(pats) > 10\nTrue\n\n# Look at the first one\n>>> pats[0]\nPublicationBiblio(publication_number=7841958, publication_date=2010-11-30, patent_title=Modular table tennis game)\n\n# Fetch US Applications\n>>> app = USApplication.objects.get(\'15710770\')\n>>> app.patent_title\n\'Camera Assembly with Concave-Shaped Front Face\'\n\n# Fetch from USPTO Assignments\n>>> assignments = Assignment.objects.filter(assignee=\'Google\')\n>>> len(assignments) > 23000\nTrue\n>>> assignment = Assignment.objects.get(\'47086-788\')\n>>> assignment.conveyance_text\n\'ASSIGNMENT OF ASSIGNORS INTEREST\'\n\n# Fetch from INPADOC\n>>> pub = Inpadoc.objects.get(\'EP3082535A1\')\n>>> pub.biblio.title\n\'AUTOMATIC FLUID DISPENSER\'\n\n```\n<!-- RTD-IGNORE -->\n\n## Documentation\n\nDocs, including a fulsome Getting Started are available on [Read the Docs](http://patent-client.readthedocs.io).\n\n<!-- END-RTD-IGNORE -->\n\n# Development\n\nTo run the all tests run:\n\n```\npytest\n```\n\nA developer guide is provided in the [Documentation](http://patent-client.readthedocs.io).\nPull requests welcome!\n\n# Related projects\n\n- [Python EPO OPS Client](https://github.com/55minutes/python-epo-ops-client)\n- [Google Public Patent Data](https://github.com/google/patents-public-data)\n- [PatentsView API Wrapper](https://github.com/mikeym88/PatentsView-API-Wrapper)\n- [USPTO Scrapy Scraper](https://github.com/blazers08/USPTO)\n\n',
    'author': 'Parker Hancock',
    'author_email': '633163+parkerhancock@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/parkerhancock/patent_client',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
