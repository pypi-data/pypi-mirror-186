# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests',
 'xedocs',
 'xedocs.databases',
 'xedocs.schemas',
 'xedocs.schemas.analysis',
 'xedocs.schemas.calibrations',
 'xedocs.schemas.corrections',
 'xedocs.schemas.operations_reports',
 'xedocs.schemas.pmt_data']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'click',
 'rframe>=0.2.0,<0.3.0',
 'rich',
 'tinydb>=4.7.0,<5.0.0',
 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{'db': ['pymongo']}

entry_points = \
{'console_scripts': ['xedocs = xedocs.cli:main'],
 'straxen': ['xedocs_protocol = xedocs._straxen_plugin'],
 'xedocs_db_interfaces': ['api = xedocs.databases.api:APIDatabase',
                          'github = xedocs.databases.github:GithubDatabase',
                          'local_repo = '
                          'xedocs.databases.local:LocalRepoDatabase',
                          'mongo = xedocs.databases.mongo:MongoDatabase',
                          'utilix = xedocs.databases.utilix:UtilixDatabase']}

setup_kwargs = {
    'name': 'xedocs',
    'version': '0.2.8',
    'description': 'Top-level package for xedocs.',
    'long_description': "=======================================\nXeDocs - XENON Metadata management tool\n=======================================\nxedocs is meant to replace cmt and bodega as well as helping tracking all shared documents especially if\nthey need to be versioned.\n\nWhat does Xedocs give you\n=========================\n\nData reading\n------------\n\n- Read data from multiple formats (e.g. mongodb, pandas) and locations with a simple unified interface.\n- Custom logic implemented on the document class, e.g. creating a tensorflow model from the data etc.\n- Multiple APIs for reading data, fun functional, ODM style, pandas and xarray.\n- Read data as objects, dataframes, dicts, json.\n    \nWriting data\n------------\n\n- Write data to multiple storage backends with the same interface\n- Custom per-collection rules for data insertion, deletion and updating.\n- Schema validation and type coercion so storage has uniform and consistent data.\n    \nOther\n-----\n\n- Custom panel widgets for graphical representation of data, web client\n- Auto-generated API server and client + openapi documentation\n- CLI for viewing and downloading data\n\n\nBasic Usage\n-----------\n\nExplore the available schemas\n\n.. code-block:: python\n\n    import xedocs\n\n    >>> xedocs.list_schemas()\n    >>> ['detector_numbers',\n        'fax_configs',\n        'plugin_lineages',\n        'context_lineages',\n        'pmt_gains',\n        'global_versions',\n        'electron_drift_velocities',\n        ...]\n\n    >>> xedocs.help('pmt_gains')\n\n    >>>\n            Schema name: pmt_gains\n            Index fields: ['version', 'time', 'detector', 'pmt']\n            Column fields: ['created_date', 'comments', 'value']\n    \n\nRead/write data from the shared development database, \nthis database is writable from the default analysis username/password\n\n.. code-block:: python\n\n    import xedocs\n\n    db = xedocs.development_db\n\n    docs = db.pmt_gains.find_docs(version='v1', pmt=[1,2,3,5], time='2021-01-01T00:00:00', detector='tpc')\n    gains = [doc.value for doc in docs]\n\n    doc = db.pmt_gains.find_one(version='v1', pmt=1, time='2021-01-01T00:00:00', detector='tpc')\n    pmt1_gain = doc.value\n\nRead from the straxen processing database, this database is read-only for the default analysis username/password\n\n\n.. code-block:: python\n\n    import xedocs\n\n    db = xedocs.straxen_db\n\n    ...\n    \nYou can also query documents directly from the schema class, \nSchemas will query the straxen database by default, if no explicit datasource is given.\n\n.. code-block:: python\n\n    from xedocs.schemas import DetectorNumber\n\n    drift_velocity = DetectorNumber.straxen_db.find_one(field='drift_velocity', version='v1')\n    \n    # Returns a Bodega object with attributes value, description etc.\n    drift_velocity.value\n\n    all_v1_documents = DetectorNumber.straxen_db.find(version='v1')\n\n\n\nRead data from alternative data sources specified by path, \ne.g csv files which will be loaded by pandas.\n\n.. code-block:: python\n\n    from xedocs.schemas import DetectorNumber\n    \n    g1_doc = DetectorNumber.find_one(datasource='/path/to/file.csv', version='v1', field='g1')\n    g1_value = g1_doc.value\n    g1_error = g1_doc.uncertainty\n\nThe path can also be a github URL or any other URL supported by fsspec. \n\n.. code-block:: python\n\n    from xedocs.schemas import DetectorNumber\n    \n    g1_doc = DetectorNumber.find_one(\n                             datasource='github://org:repo@/path/to/file.csv', \n                             version='v1', \n                             field='g1')\n\n\nSupported data sources\n\n    - MongoDB collections\n    - TinyDB tables\n    - JSON files\n    - REST API clients\n\nPlease open an issue on rframe_ if you want support for an additional data format.\n\nIf you want a new datasource to be available from a schema class, you can register it to the class:\n\n.. code-block:: python\n\n    from xedocs.schemas import DetectorNumber\n    \n    DetectorNumber.register_datasource('github://org:repo@/path/to/file.csv', name='github_repo')\n\n    # The source will now be available under the given name:\n\n    g1_doc = DetectorNumber.github_repo.find_one(version='v1', field='g1')\n\n\nDocumentation\n-------------\nFull documentation hosted by Readthedocs_\n\nCredits\n-------\n\n\nThis package was created with Cookiecutter_ and the `briggySmalls/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage\n.. _Readthedocs: https://xedocs.readthedocs.io/en/latest/\n.. _rframe: https://github.com/jmosbacher/rframe",
    'author': 'Yossi Mosbacher',
    'author_email': 'joe.mosbacher@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/XENONnT/xedocs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
