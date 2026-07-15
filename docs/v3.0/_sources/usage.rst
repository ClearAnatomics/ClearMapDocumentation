.. _usage:


Usage
=====

GUI
---
The simplest way to use *ClearMap* is to run the Graphical User Interface (GUI) by typing:

.. code-block:: bash

    # Replace ClearMapUi39 with your environment name
    # This is printed at the end of the installation script for reference
    conda activate ClearMapUi39
    clearmap-ui

Alternative scripts
-------------------
Alternatively, you can use the following scripts to run the main functions of *ClearMap*:
:mod:`~ClearMap.Scripts.cell_map_new_api` and :mod:`~ClearMap.Scripts.tube_map_new_api`. [1]_

ClearMap Environment
--------------------

To make your functions available in your python console run

>>> from ClearMap.Environment import *


.. note::
    When running this for the first time sub-modules will be compiled on demand
    which can take up to 10-30min.


Example
-------

Here is a simple example that loads a data source and plots it:

>>> from ClearMap.Environment import *
>>> source = io.as_source('path_to_filename')
>>> p3d.plot(source)


.. [1]
    .. deprecated:: 2.1.0
        The Former CellMap and TubeMap scripts are now deprecated. For standard uses, see the GUI,
        or use the new :mod:`~ClearMap.Scripts.cell_map_new_api` and :mod:`~ClearMap.Scripts.tube_map_new_api` scripts.

        ================================ =============== =============================================================================== ==============================================================
        Script                           Documentation   Tutorial                                                                        Description
        ================================ =============== =============================================================================== ==============================================================
        :mod:`~ClearMap.Scripts.CellMap` :doc:`cellmap`  :ref:`cell_map_tutorial.ipynb <_static/scripts/cell_map_tutorial.ipynb>`        Cell detection pipeline, e.g. for immediate early gene mapping
        :mod:`~ClearMap.Scripts.TubeMap` :doc:`tubemap`  :ref:`tube_map_tutorial.ipynb <../../ClearMap/Scripts/tube_map_tutorial.ipynb>`               Vasculature network construction pipeline
        ================================ =============== =============================================================================== ==============================================================


.. toctree::
    :hidden:
    :maxdepth: 2

    overview
    functionality
    advanced/wobblystitcher
    cellmap
    tubemap
