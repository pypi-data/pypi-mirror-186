# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['odin',
 'odin.annotated_resource',
 'odin.codecs',
 'odin.contrib',
 'odin.contrib.arrow',
 'odin.contrib.geo',
 'odin.contrib.money',
 'odin.contrib.pint',
 'odin.contrib.sphinx',
 'odin.contrib.swagger',
 'odin.fields',
 'odin.mapping',
 'odin.utils',
 'tests',
 'tests.annotated_resources',
 'tests.contrib']

package_data = \
{'': ['*'], 'tests': ['fixtures/*']}

extras_require = \
{'arrow': ['arrow'],
 'msgpack': ['msgpack'],
 'pint': ['pint'],
 'toml': ['toml'],
 'yaml': ['pyyaml']}

setup_kwargs = {
    'name': 'odin',
    'version': '2.1',
    'description': 'Data-structure definition/validation/traversal, mapping and serialisation toolkit for Python',
    'long_description': '\n####\nOdin\n####\n\nOdin provides a declarative framework for defining resources (classes) and their relationships, validation of the fields\nthat make up the resources and mapping between objects (either a resource, or other python structures).\n\nOdin also comes with built in serialisation tools for importing and exporting data from resources.\n\n+---------+-------------------------------------------------------------------------------------------------------------+\n| Docs/   | .. image:: https://readthedocs.org/projects/odin/badge/?version=latest                                      |\n| Help    |    :target: https://odin.readthedocs.org/                                                                   |\n|         |    :alt: ReadTheDocs                                                                                        |\n|         | .. image:: https://img.shields.io/badge/gitterim-timsavage.odin-brightgreen.svg?style=flat                  |\n|         |    :target: https://gitter.im/timsavage/odin                                                                |\n|         |    :alt: Gitter.im                                                                                          |\n+---------+-------------------------------------------------------------------------------------------------------------+\n| Build   | .. image:: https://github.com/python-odin/odin/actions/workflows/python-package.yml/badge.svg               |\n|         |    :target: https://github.com/python-odin/odin/actions/workflows/python-package.yml                        |\n|         |    :alt: Python package                                                                                     |\n+---------+-------------------------------------------------------------------------------------------------------------+\n| Quality | .. image:: https://sonarcloud.io/api/project_badges/measure?project=python-odin_odin&metric=sqale_rating    |\n|         |    :target: https://sonarcloud.io/dashboard?id=python-odin/odin                                             |\n|         |    :alt: Maintainability                                                                                    |\n|         | .. image:: https://sonarcloud.io/api/project_badges/measure?project=python-odin_odin&metric=security_rating |\n|         |    :target: https://sonarcloud.io/project/security_hotspots                                                 |\n|         |    :alt: Security                                                                                           |\n|         | .. image:: https://sonarcloud.io/api/project_badges/measure?project=python-odin_odin&metric=coverage        |\n|         |    :target: https://sonarcloud.io/code?id=python-odin_odin                                                  |\n|         |    :alt: Test Coverage                                                                                      |\n|         | .. image:: https://img.shields.io/badge/code%20style-black-000000.svg                                       |\n|         |    :target: https://github.com/ambv/black                                                                   |\n|         |    :alt: Once you go Black...                                                                               |\n+---------+-------------------------------------------------------------------------------------------------------------+\n| Package | .. image:: https://img.shields.io/pypi/v/odin                                                               |\n|         |    :target: https://pypi.io/pypi/odin/                                                                      |\n|         |    :alt: Latest Version                                                                                     |\n|         | .. image:: https://img.shields.io/pypi/pyversions/odin                                                      |\n|         |    :target: https://pypi.io/pypi/odin/                                                                      |\n|         | .. image:: https://img.shields.io/pypi/l/odin                                                               |\n|         |    :target: https://pypi.io/pypi/odin/                                                                      |\n|         | .. image:: https://img.shields.io/pypi/wheel/odin                                                           |\n|         |    :alt: PyPI - Wheel                                                                                       |\n|         |    :target: https://pypi.io/pypi/odin/                                                                      |\n+---------+-------------------------------------------------------------------------------------------------------------+\n\n\nHighlights\n**********\n\n* Class based declarative style\n* Class based annotations style! ✨ new in 2.0\n* Fields for building composite resources\n* Field and Resource level validation\n* Easy extension to support custom fields\n* Python 3.8+ and PyPy :sup:`1` supported\n* Support for documenting resources with `Sphinx <http://sphinx-doc.org/>`_\n* Minimal dependencies\n\n:sup:`1` certain contrib items are not supported. Pint is not installable with PyPy.\n\nUse cases\n*********\n* Design, document and validate complex (and simple!) data structures\n* Convert structures to and from different formats such as JSON, YAML, MsgPack, CSV, TOML\n* Validate API inputs\n* Define message formats for communications protocols, like an RPC\n* Map API requests to ORM objects\n\nQuick links\n***********\n\n* `Documentation <https://odin.readthedocs.org/>`_\n* `Project home <https://github.com/python-odin/odin>`_\n* `Issue tracker <https://github.com/python-odin/odin/issues>`_\n\n\nUpcoming features\n*****************\n\n**In development**\n\n* XML Codec (export only)\n* Complete documentation coverage\n* Improvements for CSV Codec (writing, reading multi resource CSV\'s)\n\n\nRequires\n********\n\n**Optional**\n\n* simplejson - Odin will use simplejson if it is available or fallback to the builtin json library\n* msgpack-python - To enable use of the msgpack codec\n* pyyaml - To enable use of the YAML codec\n* toml - To enable use of the TOML codec\n\n**Contrib**\n\n* arrow - Support for Arrow data types.\n* pint - Support for physical quantities using the `Pint <http://pint.readthedocs.org/>`_ library.\n\n**Development**\n\n* pytest - Testing\n* pytest-cov - Coverage reporting\n\nExample\n*******\n\n**Definition**\n\n.. code-block:: python\n\n    import odin\n\n    class Author(odin.Resource):\n        name = odin.StringField()\n\n    class Publisher(odin.Resource):\n        name = odin.StringField()\n\n    class Book(odin.Resource):\n        title = odin.StringField()\n        authors = odin.ArrayOf(Author)\n        publisher = odin.DictAs(Publisher)\n        genre = odin.StringField()\n        num_pages = odin.IntegerField()\n\n**Using Annotations**\n\n.. code-block:: python\n\n    import odin\n\n    class Author(odin.AnnotatedResource):\n        name: str\n\n    class Publisher(odin.AnnotatedResource):\n        name: str\n        website: Optional[odin.Url]\n\n    class Book(odin.AnnotatedResource):\n        title: str\n        authors: List[Author]\n        publisher: Publisher\n        genre: str\n        num_pages: int\n\n**Usage**::\n\n    >>> b = Book(\n            title="Consider Phlebas",\n            genre="Space Opera",\n            publisher=Publisher(name="Macmillan"),\n            num_pages=471\n        )\n    >>> b.authors.append(Author(name="Iain M. Banks"))\n    >>> from odin.codecs import json_codec\n    >>> json_codec.dumps(b, indent=4)\n    {\n        "$": "Book",\n        "authors": [\n            {\n                "$": "Author",\n                "name": "Iain M. Banks"\n            }\n        ],\n        "genre": "Space Opera",\n        "num_pages": 471,\n        "publisher": {\n            "$": "Publisher",\n            "name": "Macmillan"\n        },\n        "title": "Consider Phlebas"\n    }\n\n\n',
    'author': 'Tim Savage',
    'author_email': 'tim@savage.company',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/python-odin/odin',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
