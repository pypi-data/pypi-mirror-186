darfix
======

darfix is a Python library for the analysis of dark-field microscopy data. It provides a series of computer vision techniques, together with a graphical user interface and an Orange3 (https://github.com/biolab/orange3) add-on to define the workflow.

Installation
------------

If you are on Linux:
--------------------

It is recommended to create a virtual environment to avoid conflicts between dependencies (https://docs.python.org/3/library/venv.html).

.. code-block:: bash

    python3 -m venv /path/to/new/virtual/environment

    source /path/to/new/virtual/environment/bin/activate

*Note: To deactivate the environment call:* :code:`deactivate`

Then, you can install darfix with all its dependencies:

.. code-block:: bash

    pip install darfix[full]

To install darfix with a minimal set of dependencies run instead:

.. code-block:: bash

    pip install darfix

Start the GUI and make sure darfix appears as an add-on:

.. code-block:: bash

    orange-canvas

If you are on Windows:
----------------------

The easiest way is to install Miniconda: https://docs.conda.io/en/latest/miniconda.html

After installed, open **Anaconda Prompt** and install the following packages:

.. code-block:: bash

    conda config --add channels conda-forge

    conda install orange3 silx scikit-image opencv

And install darfix and ewoks:

.. code-block:: bash

    pip install ewoks[orange] darfix

Start the GUI and make sure darfix appears as an add-on:

.. code-block:: bash

    orange-canvas


To install from sources:
------------------------

.. code-block:: bash

    git clone https://gitlab.esrf.fr/XRD/darfix.git
    cd darfix
    pip install .

Or with all its dependencies:

.. code-block:: bash

    pip install .[full]

To test the orange workflow (only from sources) just run

.. code-block:: bash

    orange-canvas orangecontrib/darfix/tutorials/darfix_example2.ows

To test a workflow execution without the canvas (only from sources) just run

.. code-block:: bash

    darfix -wf orangecontrib/darfix/tutorials/darfix_example2.ows -fd orangecontrib/darfix/tutorials/ -td /tmp/darfix

Documentation
-------------

The documentation of the latest release is available at https://darfix.readthedocs.io/en/latest/

User guide
----------

A user guide can be downloaded at https://darfix.readthedocs.io/en/latest/user_guide.html
