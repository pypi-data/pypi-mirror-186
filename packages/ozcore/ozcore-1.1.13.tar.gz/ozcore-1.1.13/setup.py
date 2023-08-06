# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ozcore',
 'ozcore.core',
 'ozcore.core.aggrid',
 'ozcore.core.data',
 'ozcore.core.data.csv',
 'ozcore.core.data.sqlite',
 'ozcore.core.office',
 'ozcore.core.office.docx',
 'ozcore.core.path',
 'ozcore.core.qgrid']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ozcore',
    'version': '1.1.13',
    'description': 'My core.',
    'long_description': '======\nOzCore\n======\n\nOzCore is my core.\n\n\n.. image:: https://badge.fury.io/py/ozcore.svg\n    :target: https://pypi.python.org/pypi/ozcore/\n    :alt: PyPI version\n\n\n.. image:: https://readthedocs.org/projects/ozcore/badge/?version=latest\n    :target: https://ozcore.readthedocs.io/en/latest/?badge=latest\n    :alt: Documentation Status\n\n\n.. image:: http://hits.dwyl.com/ozgurkalan/OzCore.svg\n    :target: http://hits.dwyl.com/ozgurkalan/OzCore\n    :alt: HitCount\n\n\n\n\n\n\nIt is automating my boring stuff. A time saver for me. I can access frequently used modules and methods easliy. Most of my time is passing with Jupyter Notebooks, and OzCore is my best friend. \n\nMany code snippets derive from a hard processes. I search for the best fitting options and try them sometimes for hours or days. OzCore keeps my good practices as side notes. My quality time for coding is mostly passing with annoying dev-environment, re-setups and glitches. OzCore skips the hard process and provides me with a fresh working environment, where All necessary packages installed.\n\nGoals\n=====\n\n* a Jupyter Notebook having the most used modules.\n* shorthand to \n    * path operations\n    * tmp folder actions\n    * Sqlite operations\n    * CSV operations\n    * Dataframe operations\n    * Dummy records\n    * Jupyter initial setups\n    * Jupyter Notebook grid plugins\n    * and some MS Office automations\n\n\nWarnings\n========\n\nWork In Progress\n~~~~~~~~~~~~~~~~\n\nThis package is continuously WIP. It is for my development projects and I happily share it with open source developers. But, please bear with the versions and tests, which may effect your applications.\n\n\nMassive Dependencies\n~~~~~~~~~~~~~~~~~~~~\n\nSince OzCore is a collection of snippets using diverse packages, massive amount of dependencies will be downloaded.\n\n.. warning::\n\n    Please see dependencies in ``pyproject.toml`` before installing.\n\nMacOS bound modules\n~~~~~~~~~~~~~~~~~~~\n\nSome of the helper modules and functions are directly referenced to MacOS environment. Espacially Windows users may not like it. And some references are pointing to options which may not be available in your system. Such as OneDrive folder or gDrive folder. I have tests to distinguish between users, nevertheless you should be aware of this.\n\n------------\n\n\nInstallation\n============\n\nI would prefer to run on an Anaconda environment. Here you will find multiple examples.\n\n.. warning::\n\n    Python environment management has become a disaster. Please be sure where you are with ``which python`` . \n\n\nI. Anaconda\n~~~~~~~~~~~\n\nYou may want to set the global Python version with Pyenv as ``pyenv global 3.8.3`` (of course if pyenv is available.)\n\n.. code:: bash\n\n    # create new env \n    conda create -n py383\n\n    conda activate py383\n\n    # this initiates every source bindings to new env\n    conda install pip\n\n    # install ozcore\n    conda install ozcore\n\n\n\nII. Virtualenv\n~~~~~~~~~~~~~~\n\n.. code:: bash\n\n    # create a virtualenv\n    python -m venv .venv\n\n    source .venv/bin/activate\n\n    pip install ozcore\n\n\nIII. Pip simple\n~~~~~~~~~~~~~~~\n\n.. code:: bash\n\n    # in any environment having pip\n    pip install ozcore\n\n\nIV. Poetry with Pyenv\n~~~~~~~~~~~~~~~~~~~~~\n\n.. code:: bash\n\n    # in any package folder (3.8.4 version of python is arbitrary)\n    pyenv local 3.8.4\n\n    poetry shell\n\n    poetry add ozcore\n\n\nV. GitHub with Pip\n~~~~~~~~~~~~~~~~~~\n\n.. code:: bash\n\n    # in any environment having pip\n    pip install https://github.com/ozgurkalan/OzCore.git\n\n\nVI. GitHub clone\n~~~~~~~~~~~~~~~~\n\n.. code:: bash\n\n    # in some folder, e.g. Desktop\n    git clone https://github.com/ozgurkalan/OzCore.git\n\n\n\nJupyter Kernel\n==============\n\nJupyter has its own configuration. Espacially when you have Anaconda installed,  ``kernel.json`` may have what conda sets. \n\nFor your Jupyter Notebook to run in your dedicated environment, please use the following script::\n\n    # add kernell to Jupyter\n    python -m ipykernel install --user --name=<your_env_name>\n\n    # remove the kernel from Jupyter\n    jupyter kernelspec uninstall <your_env_name>\n\n\nFresh installs may have problems with enabling extentions. You shall run the commands below to activate.\n\n.. code:: bash\n\n    jupyter nbextension enable --py --sys-prefix qgrid\n    jupyter nbextension enable --py --sys-prefix widgetsnbextension\n\n\nJupyter Extensions\n==================\n\nThis step copies the ``nbextensions`` javascript and css files into the jupyter server’s search directory, and edits some jupyter config files. \n\n.. code:: bash\n\n    jupyter contrib nbextension install --user\n\n\n\n\n',
    'author': 'Ozgur Kalan',
    'author_email': 'ozgurkalan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ozcore.readthedocs.io/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
