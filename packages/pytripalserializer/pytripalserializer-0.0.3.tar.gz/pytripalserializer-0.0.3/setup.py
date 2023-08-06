# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests', 'tripser']

package_data = \
{'': ['*'], 'tests': ['test_data/*']}

install_requires = \
['click==8.0.1', 'poetry-release>=0.3.0,<0.4.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

entry_points = \
{'console_scripts': ['pytripalserializer = tripser.cli:cli']}

setup_kwargs = {
    'name': 'pytripalserializer',
    'version': '0.0.3',
    'description': "Serialize Tripal's JSON-LD API into RDF..",
    'long_description': '# PyTripalSerializer\n[![Documentation Status](https://readthedocs.org/projects/pytripalserializer/badge/?version=latest)](https://pytripalserializer.readthedocs.io/en/latest/?badge=latest)\n[![build & test](https://github.com/mpievolbio-scicomp/PyTripalSerializer/actions/workflows/dev.yml/badge.svg)](https://github.com/mpievolbio-scicomp/PyTripalSerializer/actions/workflows/dev.yml)\n## Serialize Tripal\'s JSON-LD API into RDF format\nThis package implements a recursive algorithm to parse the JSON-LD API of a [Tripal](https://tripal.info "Tripal")\ngenomic database webservice and serialize the encountered terms into a RDF document. Output will be saved in\na turtle file (.ttl).\n\n## Motivation\nThis work is a byproduct of a data integration project for multiomics data at [MPI for Evolutionary Biology](https://evolbio.mpg.de). Among various other data sources, we run an instance of the Tripal genomic database website engine. This\nservice provides a [JSON-LD](https://json-ld.org/) API, i.e., all data in the underlying relational database is accessible through appropriate http GET requests against that API. So far so good. Now, in our project, we are working\non integrating data based on Linked Data technology; in particular, all data sources should be accessible via (federated) SPARQL queries. Hence, the task is to convert the JSON-LD API into a SPARQL endpoint.\n\nThe challenge here is that the JSON-LD API only provides one document at a time. Querying a single document with e.g.\nthe `arq` utility (part of the [Apache-Jena](https://jena.apache.org/) package) is no problem. The problem starts\nwhen one then attempts to run queries against other JSON-LD documents referenced in the first document as object URIs but. These object URIs are not part of the current document (graph). Instead, they point to separate graph.\nSPARQL in its current implementation does not support dynamic generation of graph URIs from e.g. object URIs.\nHence the need for a code that recursively parses a JSON-LD document including all referenced documents.\n\nOf course this is a generic problem. This package implements a solution targeted for Tripal JSON-LD APIs but with minimal changes it should be adaptable for other JSON-LD APIs.\n## Installation\n\n### PyPI Releases\nThis package is released via the Python Package Index (PyPI). To install it, run\n\n```console\n$ pip install pytripalserializer\n```\n\n### Github development snapshot\nTo install the latest development snapshot from github, clone this repository\n\n```console\ngit clone https://github.com/mpievolbio-scicomp/PyTripalSerializer\n```\n\nNavigate into the cloned directory and run a local `pip install`:\n\n```console\ncd PyTripalSerializer\npip install [-e] .\n```\nThe optional flag `-e` would instruct `pip` to install symlinks to the source files, this is recommended for developers.\n\n## Usage\nThe simplest way to use the package is via the command line interface. The following example should\nbe instructive enough to get started:\n\n```console\n$ cd PyTripalSerializer\n$ cd src\n$ ./tripser http://pflu.evolbio.mpg.de/web-services/content/v0.1/CDS/11846 -o cds11846.ttl\n```\n\nRunning this command should produce the RDF turtle file "cds11846.ttl" in the src/ directory. "cds11846" has only 42 triples.\n\nBe aware that running the command on a top level URL such as http://pflu.evolbio.mpg.de/web-services/content/v0.1/ would parse the entire tree of documents which results in a graph of ~2 million triples and takes roughly 14hrs to complete on a reasonably well equipped workstation with 48 CPUs.\n\n## Testing\nRun the test suite with\n\n```console\npytest tests\n```\n\n## Documentation\nClick the documentation badge at the top of this README to access the online manual.\n',
    'author': 'Carsten Fortmann-Grote',
    'author_email': 'carsten.fortmann-grote@evolbio.mpg.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/CFGrote/PyTripalSerializer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0',
}


setup(**setup_kwargs)
