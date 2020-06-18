Overview
========

Introduction
------------

*ClearMap* is a toolbox for the analysis and registration of volumetric
data from cleared tissues.

*ClearMap* has been designed to analyze terabyte-sized 3d datasets obtained 
via light sheet microscopy from iDISCO+ cleared tissue samples 
immunolabeled for proteins. 
 
*ClearMap* has been written for mapping immediate early genes [Renier2016]_
as well as vasculature networks of whole mouse brains [Kirst2020]_

.. image:: Static/cell_abstract_2020.jpg
   :target: https://doi.org/10.1016/j.cell.2016.05.007 
   :width: 300  
.. image:: Static/cell_abstract_2016.jpg
   :target: https://doi.org/10.1016/j.cell.2020.01.028
   :width: 300
  

*ClearMap* tools may also be useful for data obtained with other types of 
microscopes, types of markers, clearing techniques, as well as other species,
organs, or samples.

*ClearMap* is written in Python 3 and is designed to take advantage of
parallel processing capabilities of modern workstations. We hope the open 
structure of the code will enable many new modules to be added to *ClearMap*
to broaden the range of applications to different types of biological objects 
or structures.


Functionality and Pipelines
---------------------------

ClearMap provides a larger set of high performance 3d image processing 
functions that are introduced here: :doc:`functionality`.

These functions are combined together in expert functions under
:mod:`~ClearMap.ImageProcessing.Experts` which are made use of in 
pipelines found in :mod:`~ClearMap.Scripts` to quantify the data sets. 

The main tools are:

  * :doc:`wobblystitcher`
  * :doc:`cellmap`
  * :doc:`tubemap`


Usage
-----

An introdution of how to use *ClearMap* can be found here: 

:doc:`usage`


Documentation
-------------

The full code doucmentation can be found here:

:doc:`index`


Source
------

https://github.com/ChristophKirst/ClearMap2


Authors
-------

Lead programming and design
"""""""""""""""""""""""""""
Christoph Kirst

Scripts and specific applications
"""""""""""""""""""""""""""""""""
Nicolas Renier and Christoph Kirst

Vessle filling network
""""""""""""""""""""""
Sophie Skriabine and Christoph Kirst

Documentation:
""""""""""""""
Christoph Kirst and Nicolas Renier


License
-------

GNU GENERAL PUBLIC LICENSE Version 3

See :download:`LICENSE <../../LICENSE.txt>` or `gnu.org <http://www.gnu.org/licenses/gpl-3.0.en.html>`_ for details.


Social Media
------------

.. timeline:: clearmap_idisco


