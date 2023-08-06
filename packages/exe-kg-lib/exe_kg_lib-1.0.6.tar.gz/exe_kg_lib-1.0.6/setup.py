# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exe_kg_lib',
 'exe_kg_lib.classes',
 'exe_kg_lib.classes.tasks',
 'exe_kg_lib.cli',
 'exe_kg_lib.utils',
 'exe_kg_lib.utils.task_utils']

package_data = \
{'': ['*']}

install_requires = \
['black[d]>=22.10.0,<23.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'pandas>=1.5.2,<2.0.0',
 'rdflib>=6.2.0,<7.0.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'typer>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'exe-kg-lib',
    'version': '1.0.6',
    'description': 'Library for executable ML pipelines represented by KGs.',
    'long_description': "# ExeKGLib\n\n![PyPI](https://img.shields.io/pypi/v/exe-kg-lib)\n![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)\n![Poetry](https://img.shields.io/badge/poetry-v1.2.2-blue)\n[![Code style: black][black-badge]][black]\n[![License](https://img.shields.io/badge/license-AGPL%203.0-blue)](https://www.gnu.org/licenses/agpl-3.0.en.html)\n\nPython library for conveniently constructing and executing Machine Learning (ML) pipelines represented by Knowledge Graphs (KGs).\n\nDetailed information (installation, documentation etc.) about the library can be found in [its website](https://boschresearch.github.io/ExeKGLib/) and basic information is shown below.\n\n## Overview\n\n[//]: # (--8<-- [start:overview])\nThe functionality of this Python library can be divided in the below two parts:\n\n1. **Executable KG construction**: An executable KG representing an ML pipeline is constructed as per user's input (programmatically or via CLI) based on the KG schemas. The construction is done by sequentially creating pairs of instances of [ds:AtomicTask](https://nsai-uio.github.io/ExeKGOntology/OnToology/ds_exeKGOntology.ttl/documentation/index-en.html#AtomicTask) and [ds:AtomicMethod](https://nsai-uio.github.io/ExeKGOntology/OnToology/ds_exeKGOntology.ttl/documentation/index-en.html#AtomicMethod) sub-classes, and their properties. The definition of these sub-classes can be found in the [bottom-level KG schemas](#bottom-level-kg-schemas). After each KG component is built, it is validated using the KG schemas and added to an RDFLib `Graph` object. The KG is finally saved in Turtle format.\n2. **ML pipeline execution**: The executable KG is parsed using RDFLib and queried using SPARQL to retrieve its ML pipeline. The pipeline's ordered tasks are sequentially mapped to Python objects that include an implemented `run_method()` Python method which is then invoked. This is as an abstract method of the _Task_ class that is implemented by its bottom-level children classes.\n\nThe different implementations of `run_method()` correspond to the [ds:AtomicMethod](https://nsai-uio.github.io/ExeKGOntology/OnToology/ds_exeKGOntology.ttl/documentation/index-en.html#AtomicMethod) bottom-level sub-classes that are defined in the Visualization, Statistics, and ML KG schemas. The method categories are described below.\n\n1. **Visualization**: This is a set of methods for visualization, including two types: (1) The plot canvas methods that define the plot size and layout. (2) The various kinds of plot methods (line plot, scatter plot, bar plot, etc.). These methods use matplotlib to visualize data.\n2. **Statistics and Feature Engineering**: This includes methods for statistical analysis and feature engineering like IQR calculation, mean and std-deviation calculation, etc., which can then form complex methods like outlier detection method and normalization method.\n3. **Machine Learning**: This is a group of methods that support ML algorithms like Linear Regression, MLP, and k-NN and helper functions that perform e.g. data splitting and ML model performance calculation.\n\nThis library is part of the following paper submitted to ESWC 2023:<br>\n_Klironomos A., Zhou B., Tan Z., Zheng Z., Gad-Elrab M., Paulheim H., Kharlamov E.: **ExeKGLib: A Python Library for Machine Learning Analytics based on Knowledge Graphs**_\n\n[//]: # (--8<-- [end:overview])\n\n## Getting started\n\n[//]: # (--8<-- [start:gettingstarted])\nThe library is available as a [PyPi package](https://pypi.org/project/exe-kg-lib/).\n\nTo download, run `pip install exe-kg-lib`.\n\n[//]: # (--8<-- [end:gettingstarted])\n\n## Usage\n\n[//]: # (--8<-- [start:usage])\n### Creating an executable KG\n#### Via CLI\n1. Run `python kg_construction.py`.\n2. Follow the input prompts.\n\n#### Via code\nSee the [provided examples](examples/).\n\n### Executing a generated KG\nRun `python kg_execution.py [kg_file_path]`.\n\n[//]: # (--8<-- [end:usage])\n\n## Installation\nSee the [installation page](https://boschresearch.github.io/ExeKGLib/installation/) of the library's website.\n\n## Adding a new ML-related task and method\n\n[//]: # (--8<-- [start:extending])\nTo perform this type of library extension, there are 3 required steps:\n\n1. Selection of a relevant bottom-level KG schema (Statistics, ML, or Visualization) according to the type of the new task and method.\n2. Addition of new semantic components (entities, properties, etc) to the selected KG schema.\n3. Addition of a Python class to the corresponding module of `exe_kg_lib.classes.tasks` package.\n\nFor steps 2 and 3, refer to the [relevant page](https://boschresearch.github.io/ExeKGLib/adding-new-task-and-method/) of the library's website.\n\n[//]: # (--8<-- [end:extending])\n\n## Documentation\nSee the _Code Reference_ and _Development_ sections of the [library's website](https://boschresearch.github.io/ExeKGLib/).\n\n## External resources\n\n[//]: # (--8<-- [start:externalresources])\n### Top-level KG schemas\n- [Data Science KG schema](https://w3id.org/def/exekg-ds)\n\n### Bottom-level KG schemas\n- [Visualization KG schema](https://w3id.org/def/exekg-visu)\n- [Statistics KG schema](https://w3id.org/def/exekg-stats)\n- [Machine Learning KG schema](https://w3id.org/def/exekg-ml)\n\nThe above KG schemas are included in the [ExeKGOntology repository](https://github.com/nsai-uio/ExeKGOntology).\n\n### Dataset used in code examples\nThis dataset (located in `exe_kg_lib/examples/data/dummy_data.csv`) was generated using the `sklearn.datasets.make_classification()` function of the [scikit-learn Python library](https://scikit-learn.org/).\n\n[//]: # (--8<-- [end:externalresources])\n\n## License\n\nExeKGLib is open-sourced under the AGPL-3.0 license. See the\n[LICENSE](LICENSE.md) file for details.\n\n<!-- URLs -->\n[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg\n[black]: https://github.com/psf/black\n[ci-badge]: https://github.com/boschresearch/ExeKGLib/actions/workflows/ci.yaml/badge.svg\n[ci]: https://github.com/boschresearch/ExeKGLib/actions/workflows/ci.yaml\n[docs-badge]: https://img.shields.io/badge/docs-gh--pages-inactive\n[docs]: https://github.com/boschresearch/ExeKGLib/tree/gh-pages\n[license-badge]: https://img.shields.io/badge/License-All%20rights%20reserved-informational\n[license-url]: https://pages.github.boschdevcloud.com/bcai-internal//latest/license\n[pre-commit-badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n[pre-commit]: https://github.com/pre-commit/pre-commit\n",
    'author': 'Antonis Klironomos',
    'author_email': 'antonis.klironomos@de.bosch.com',
    'maintainer': 'Antonis Klironomos',
    'maintainer_email': 'antonis.klironomos@de.bosch.com',
    'url': 'https://boschresearch.github.io/ExeKGLib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
