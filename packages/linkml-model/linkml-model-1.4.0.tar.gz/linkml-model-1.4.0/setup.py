# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linkml_model']

package_data = \
{'': ['*'],
 'linkml_model': ['graphql/*',
                  'json/*',
                  'jsonld/*',
                  'jsonschema/*',
                  'model/*',
                  'model/docs/*',
                  'model/docs/specification/*',
                  'model/schema/*',
                  'owl/*',
                  'rdf/*',
                  'shex/*',
                  'sqlddl/*']}

install_requires = \
['linkml-runtime>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'linkml-model',
    'version': '1.4.0',
    'description': 'Metamodel schema, documentation, and specification for the Linked Open Data Modeling Language (LinkML)',
    'long_description': '[![Pyversions](https://img.shields.io/pypi/pyversions/linkml_model.svg)](https://pypi.python.org/pypi/linkml_model)\n![](https://github.com/linkml/linkml-model/workflows/Build/badge.svg)\n[![PyPi](https://img.shields.io/pypi/v/linkml_model.svg)](https://pypi.python.org/pypi/linkml_model)\n[![DOI](https://zenodo.org/badge/13996/linkml/linkml-model.svg)](https://zenodo.org/badge/latestdoi/13996/linkml/linkml-model)\n\n\n# LinkML Model\n\nMetamodel schema, documentation, and specification for the Linked Open Data Modeling Language (LinkML)\n\nThis documentation is best viewed view the generated web documentation\n\n- [https://w3id.org/linkml/](https://linkml.github.io/linkml-model/docs)\n\n## Quick Links\n\n- [Generated documentation](https://linkml.github.io/linkml-model/docs)\n- [Specification](https://linkml.io/linkml-model/docs/specification/00preamble/)\n- [Source YAML for metamodel](https://github.com/linkml/linkml-model/tree/main/linkml_model/model/schema)\n- [Main LinkML site](https://linkml.io)\n\n## About LinkML\n\nLinkML is a modeling framework for building datamodels and related applications.\n\nThe best place to start discovering more about linkml is on the main LinkML website, [linkml.io/linkml](https://linkml.io/linkml)\n\nLinkML is self-describing, and the underlying datamodel for describing data models is in LinkML. This repository contains that data model\n\n## For Developers\n\nSee the [contributing docs](https://linkml.io/linkml/contributing/contributing.html)\n\n### Installation\n\nThis project uses poetry:\n\n```bash\n> cd linkml-model\n> poetry install\n```\n\n## Running tests\n\n```bash\n> make test\n```\n',
    'author': 'Chris Mungall',
    'author_email': 'cjmungall@lbl.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://linkml.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
