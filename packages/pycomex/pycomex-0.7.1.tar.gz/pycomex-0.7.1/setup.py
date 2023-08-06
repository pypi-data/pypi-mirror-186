# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycomex',
 'pycomex.app',
 'pycomex.examples',
 'tests',
 'tests.artifacts.experiment_results.mock_experiment.000',
 'tests.artifacts.experiment_results.mock_experiment.001',
 'tests.artifacts.experiment_results.mock_experiment.002',
 'tests.artifacts.experiment_results.mock_experiment.003',
 'tests.artifacts.experiment_results.mock_experiment.004',
 'tests.artifacts.experiment_results.mock_experiment.005',
 'tests.artifacts.experiment_results.mock_experiment.006',
 'tests.artifacts.experiment_results.mock_experiment.debug',
 'tests.artifacts.experiment_results.mock_sub_experiment.000',
 'tests.artifacts.experiment_results.mock_sub_experiment.001',
 'tests.artifacts.experiment_results.mock_sub_experiment.debug',
 'tests.assets']

package_data = \
{'': ['*'], 'pycomex': ['templates/*'], 'tests': ['templates/*']}

install_requires = \
['click==7.1.2',
 'jinja2==3.0.3',
 'matplotlib>=3.5.3',
 'numpy>=1.23.2',
 'psutil>=5.7.2']

entry_points = \
{'console_scripts': ['pycomex = pycomex.cli:main']}

setup_kwargs = {
    'name': 'pycomex',
    'version': '0.7.1',
    'description': 'Python Computational Experiments',
    'long_description': '.. image:: https://img.shields.io/pypi/v/pycomex.svg\n        :target: https://pypi.python.org/pypi/pycomex\n\n.. image:: https://readthedocs.org/projects/pycomex/badge/?version=latest\n        :target: https://pycomex.readthedocs.io/en/latest/?version=latest\n        :alt: Documentation Status\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n\nPyComex - Python Computational Experiments\n================================================\n\nMicroframework to improve the experience of running and managing records of computational experiments,\nsuch as machine learning and data science experiments, in Python.\n\n* Free software: MIT license\n* Documentation: https://pycomex.readthedocs.io.\n\nFeatures\n--------\n\n* Automatically create (nested) folder structure for results of each run of an experiment\n* Simply attach metadata such as performance metrics to experiment object and they will be automatically\n  stored as JSON file\n* Easily attach file artifacts such as ``matplotlib`` figures to experiment records\n* Log messages to stdout as well as permanently store into log file\n* Ready-to-use automatically generated boilerplate code for the analysis and post-processing of\n  experiment data after experiments have terminated.\n* Experiment inheritance: Experiment modules can inherit from other modules and extend their functionality\n  via parameter overwrites and hooks!\n\nInstallation\n------------\n\nInstall stable version with ``pip``\n\n.. code-block:: console\n\n    pip3 install pycomex\n\nOr the most recent development version\n\n.. code-block:: console\n\n    git clone https://github.com/the16thpythonist/pycomex.git\n    cd pycomex ; pip3 install .\n\nQuickstart\n----------\n\nEach computational experiment has to be bundled as a standalone python module. Important experiment\nparameters are placed at the top. Actual execution of the experiment is placed within the ``Experiment``\ncontext manager.\n\nUpon entering the context, a new archive folder for each run of the experiment is created.\n\nArchiving of metadata, file artifacts and error handling is automatically managed on context exit.\n\n.. code-block:: python\n\n    # quickstart.py\n    """\n    This doc string will be saved as the "description" meta data of the experiment records\n    """\n    from pycomex.experiment import Experiment\n    from pycomex.util import Skippable\n\n    # Experiment parameters can simply be defined as uppercase global variables.\n    # These are automatically detected and can possibly be overwritten in command\n    # line invocation\n    HELLO = "hello "\n    WORLD = "world!"\n\n    # Experiment context manager needs 3 positional arguments:\n    # - Path to an existing folder in which to store the results\n    # - A namespace name unique for each experiment\n    # - access to the local globals() dict\n    with Skippable(), (e := Experiment("/tmp", "example/quickstart", globals())):\n\n        # Internally saved into automatically created nested dict\n        # {\'strings\': {\'hello_world\': \'...\'}}\n        e["strings/hello_world"] = HELLO + WORLD\n\n        # Alternative to "print". Message is printed to stdout as well as\n        # recorded to log file\n        e.info("some debug message")\n\n        # Automatically saves text file artifact to the experiment record folder\n        file_name = "hello_world.txt"\n        e.commit_raw(file_name, HELLO + WORLD)\n        # e.commit_fig(file_name, fig)\n        # e.commit_png(file_name, image)\n        # ...\n\n    # All the code inside this context will be copied to the "analysis.py"\n    # file which will be created as an experiment artifact.\n    with Skippable(), e.analysis:\n        # And we can access all the internal fields of the experiment object\n        # and the experiment parameters here!\n        print(HELLO, WORLD)\n        print(e[\'strings/hello_world\'])\n        # logging will print to stdout but not modify the log file\n        e.info(\'analysis done\')\n\nThis example would create the following folder structure:\n\n.. code-block:: python\n\n    tmp\n    |- results\n       |- example\n          |- 000\n             |+ experiment_log.txt     # Contains all the log messages printed by experiment\n             |+ experiment_meta.txt    # Meta information about the experiment\n             |+ experiment_data.json   # All the data that was added to the internal exp. dict\n             |+ hello_world.txt        # Text artifact that was committed to the experiment\n             |+ snapshot.py            # Copy of the original experiment python module\n             |+ analysis.py            # boilerplate code to get started with analysis of results\n\nThe ``analysis.py`` file is of special importance. It is created as a boilerplate starting\nplace for additional code, which performs analysis or post processing on the results of the experiment.\nThis can for example be used to transform data into a different format or create plots for visualization.\n\nSpecifically note these two aspects:\n\n1. The analysis file contains all of the code which was defined in the ``e.analysis`` context of the\n   original experiment file! This code snippet is automatically transferred at the end of the experiment.\n2. The analysis file actually imports the snapshot copy of the original experiment file. This does not\n   trigger the experiment to be executed again! The ``Experiment`` instance automatically notices that it\n   is being imported and not explicitly executed. It will also populate all of it\'s internal attributes\n   from the persistently saved data in ``experiment_data.json``, which means it is still possible to access\n   all the data of the experiment without having to execute it again!\n\n.. code-block:: python\n\n    # analysis.py\n\n    # [...] imports omitted\n    # Importing the experiment itself\n    from snapshot import *\n\n    PATH = pathlib.Path(__file__).parent.absolute()\n    DATA_PATH = os.path.join(PATH, \'experiment_data.json\')\n    # Load the all raw data of the experiment\n    with open(DATA_PATH, mode=\'r\') as json_file:\n        DATA: Dict[str, Any] = json.load(json_file)\n\n\n    if __name__ == \'__main__\':\n        print(\'RAW DATA KEYS:\')\n        pprint(list(DATA.keys()))\n\n        # ~ The analysis template from the experiment file\n        # And we can access all the internal fields of the experiment object\n        # and the experiment parameters here!\n        print(HELLO, WORLD)\n        print(e[\'strings/hello_world\'])\n        # logging will print to stdout but not modify the log file\n        e.info(\'analysis done\')\n\n\nFor more information and more interesting examples visit the Documentation: https://pycomex.readthedocs.io !\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage\n',
    'author': 'Jonas Teufel',
    'author_email': 'jonseb1998@gmail.com',
    'maintainer': 'Jonas Teufel',
    'maintainer_email': 'jonseb1998@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
