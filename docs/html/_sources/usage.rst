Usage
=====

*ClearMap* is best run through the main :mod:`~ClearMap.Scripts`:

================================ =============== ===================================== ==============================================================
Script                           Documentation    Tutorial                             Description
================================ =============== ===================================== ==============================================================
:mod:`~ClearMap.Scripts.CellMap` :doc:`cellmap`  :ref:`CellMap.ipynb </CellMap.ipynb>` Cell detection pipeline, e.g. for immediate early gene mapping
:mod:`~ClearMap.Scripts.TubeMap` :doc:`tubemap`  :ref:`TubeMap.ipynb </TubeMap.ipynb>` Vasculature network construction pipeline
================================ =============== ===================================== ==============================================================


ClearMap Environment
--------------------

To make your functions available in your python console run

>>> from ClearMap.Environment import *


Note
^^^^
When running this for the first time sub-modules will be compiled on demand 
which can take up to 10-30min.


Example
-------

Here is a simple example that loads a data source and plots it:

>>> from ClearMap.Environment import *
>>> source = io.as_source('path_to_filename')
>>> p3d.plot(source)