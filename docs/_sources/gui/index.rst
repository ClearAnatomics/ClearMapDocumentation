.. _gui:

GUI usage
=========

.. role:: bash-code(code)
   :language: bash

Prerequisites
-------------
**Before starting any analysis please ensure that the following conditions are fulfilled**

-  You have enough space on your data partition
-  ClearMap2.1 is installed and up to date
-  Fiji (as in Fiji is Just ImageJ) is installed and up to date. (if you
   want to open your file in .tif)
-  You have a folder containing the sub-folders with your raw data.

Start ClearMap
--------------
There are 2 ways to start the software:

-  Use the start menu entry
-  Use the terminal:

    - Open the terminal (CTRL+ALT+T) and type

        .. code-block:: bash

            conda activate ClearMapUi
            clearmap-ui

        .. note::
            Note that other commands starting with clearmap (e.g. utilities)
            will also become available after installing

Software introduction
---------------------

The software contains the following tabs which correspond to different operations:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sample • Alignment • CellMap • Vasculature • Batch

The preferences of the software are controlled through 2 ways:

-  The Edit -> preferences menu for the general preferences
-  The config files starting with *\_default* in the
    :bash-code:`$HOME/.clearmap` folder for the analysis defaults

.. |info-icon| image:: images/info.svg
    :width: 15

.. hint::
    For each control, you can hover the control label to get a hint as to
    its function. More help is available for some controls through a |info-icon|
    icon on the right of the control, whenever some detailed explanation is
    deemed necessary.

.. figure:: images/preferences.png

When setting integer values, if max is required (e.g. max image
intensity), use :code:`–1` as per the python notation.

.. note::
    In the Data Viewer, if you cannot see your sample, then
      a) ensure that the LUT is set correctly on the right.
      b) right-click on the middle of the image and select **View all.**


.. toctree::
    :hidden:

    menu_sample
    menu_alignment
    menu_cell_map
    menu_vasculature
    menu_batch
