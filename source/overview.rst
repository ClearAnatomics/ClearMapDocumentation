.. _overview:

Overview
========

.. include:: introduction.rst


Functionality and Pipelines
---------------------------

ClearMap provides a large set of high-performance 3D image processing
functions that are introduced here: :doc:`functionality`.

These functions are combined in expert modules under
:mod:`~ClearMap.ImageProcessing.Experts`, which are orchestrated by the
pipeline workers in :mod:`~ClearMap.pipeline_orchestrators`.

The main pipelines are:

  * :doc:`advanced/wobblystitcher` — non-rigid stitching of tiled acquisitions
  * :doc:`cellmap` — cell detection and density mapping
  * :doc:`tubemap` — vasculature binarization, graph construction, and annotation


Usage
-----

An introduction of how to use *ClearMap* can be found here:

:doc:`usage`


Documentation
-------------

The full code documentation can be found here:

:doc:`index`


Source
------

https://github.com/ClearAnatomics/ClearMap


Authors
-------

Lead programming and design
""""""""""""""""""""""""""""
Christoph Kirst and Charly Rousseau

Scripts and specific applications
"""""""""""""""""""""""""""""""""
Nicolas Renier and Christoph Kirst

Vessel filling network
""""""""""""""""""""""
Sophie Skriabine and Christoph Kirst

GUI and pipeline orchestrators
"""""""""""""""""""""""""""""""
Charly Rousseau

Documentation
""""""""""""""
Christoph Kirst, Nicolas Renier, and Charly Rousseau


License
-------

GNU GENERAL PUBLIC LICENSE Version 3

See :download:`LICENSE <../LICENSE.txt>` or `gnu.org <http://www.gnu.org/licenses/gpl-3.0.en.html>`_ for details.


Social Media
------------

.. .. timeline:: clearmap_idisco