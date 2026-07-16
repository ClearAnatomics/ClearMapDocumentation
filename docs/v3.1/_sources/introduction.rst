.. _introduction:


Introduction
------------

*ClearMap* is an open-source toolbox for the analysis and registration of
volumetric data from cleared tissues.

*ClearMap* is designed to analyse terabyte-sized 3-D datasets obtained via
light sheet microscopy from iDISCO+ cleared tissue samples immunolabeled
for proteins. It has been written for mapping immediate early genes
[Renier2016]_ as well as vasculature networks of whole mouse brains
[Kirst2020]_.

.. hint::

    *ClearMap* tools may also be useful for data obtained with other
    types of microscopes, markers, clearing techniques, species, organs, or samples.

.. image:: /static/cell_abstract_2016.jpg
   :target: https://doi.org/10.1016/j.cell.2016.05.007
   :width: 300
.. image:: /static/cell_abstract_2020.jpg
   :target: https://doi.org/10.1016/j.cell.2020.01.028
   :width: 300


*ClearMap* 3.1 extends the original cell-detection and vasculature
pipelines with:

- a **GUI** for interactive analysis without scripting,
- a **YAML-based configuration system** with schema validation,
- a **channel-centred workspace** that organises all intermediate and
  final outputs automatically,
- **myelinated-tract mapping** (TractMap) and **multi-channel
  colocalization** pipelines,
- **atlas landmark-based registration refinement**,
- **group analysis and batch processing** for multi-sample studies.

*ClearMap* is written in Python 3 and is designed to take advantage of
the parallel processing capabilities of modern workstations.  We hope the
open structure of the code will enable many new modules to be added to
broaden the range of applications to different types of biological objects
or structures.
