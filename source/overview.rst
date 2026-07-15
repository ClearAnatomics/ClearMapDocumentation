.. _overview:

Overview
========

.. include:: introduction.rst


Functionality and Pipelines
---------------------------

ClearMap provides a large set of high-performance 3-D image processing
functions described in :doc:`package_organisation`.

These functions are combined in expert modules under
:mod:`~ClearMap.ImageProcessing.Experts`, which are orchestrated by the
pipeline workers in :mod:`~ClearMap.pipeline_orchestrators`.

The main pipelines are:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Pipeline
     - Purpose
     - Documentation
   * - **Stitching**
     - Non-rigid stitching of tiled acquisitions
     - :doc:`advanced/wobblystitcher`
   * - **CellMap**
     - Cell detection, atlas alignment, density mapping
     - :doc:`cellmap`
   * - **TubeMap**
     - Vasculature binarization, graph construction, annotation
     - :doc:`tubemap`
   * - **TractMap**
     - Myelinated-tract binarization and coordinate mapping
     - (see :mod:`~ClearMap.pipeline_orchestrators.tract_map`)
   * - **Colocalization**
     - Multi-channel overlap quantification
     - (see :mod:`~ClearMap.pipeline_orchestrators.colocalization`)
   * - **Group analysis**
     - Batch processing, group comparisons, statistics
     - (see :mod:`~ClearMap.pipeline_orchestrators.group_orchestrators`)


Usage
-----

An introduction to how to use *ClearMap* can be found here: :doc:`usage`.

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
Sophie Skriabine, Christoph Kirst, Maxime Boyer

GUI, pipeline orchestrators, and configuration system
"""""""""""""""""""""""""""""""""""""""""""""""""""""
Charly Rousseau

Colocalization module
^^^^^^^^^^^^^^^^^^^^^^
Gaël Cousin and Charly Rousseau

Documentation
""""""""""""""
Christoph Kirst, Nicolas Renier, Charly Rousseau, Louise Mathé, Gabriele Lienhard, Daniela Domingues


License
-------

GNU GENERAL PUBLIC LICENSE Version 3

See :download:`LICENSE <../LICENSE.txt>` or
`gnu.org <http://www.gnu.org/licenses/gpl-3.0.en.html>`_ for details.


Social Media
------------

.. .. timeline:: clearmap_idisco
