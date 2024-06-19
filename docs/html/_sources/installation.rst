.. _installation:


Installation
------------

Computing Resources
===================

The processing with *CellMap* and *TubeMap* is best done on local workstations
or a cluster. We use high performance workstations from DELL or HP with at least
(for reasonable performance):
* 256GB RAM
* 12 CPUs
* 24GB VRAM
* Fast SSDs, NVMe preferred in a RAID0 configuration
* For the vasculature analysis pipeline, a recent nVidia GPU with >= 24GB VRAM is required

The workstations were operated by Linux Ubuntu 18.04LTS or later.

.. For our work we used either a Dell Precision T7920 or HP Z840 workstation.
    Each workstation was equipped with 2 Intel Xeon Gold 6128 3.4G 6C/12T CPUs,
    512Gb of 2666MHz DDR4 RAM, 4x1Tb NVMe Class 40 Solid State Drives in a RAID0
    array (plus a separate system disk), and an NVIDIA Quadro P6000, 24Gb VRAM
    video card.


Getting ClearMap
================

*ClearMap* currently runs on Linux, although some parts might work on Windows.
For this tutorial we assume you are using a recent version of Ubuntu Linux.

The required software packages for Linux are *build-essential*, *git* and recent proprietary nVidia drivers if
you plan on using the vasculature analysis pipeline.

We recommend installation via `Miniconda <https://docs.anaconda.com/free/miniconda/index.html>`_ although
you can also install the dependencies manually.


The steps are as follows:

* Download `Miniconda3 <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_
* Install anaconda for Python 3 for your OS and install it following
  the `installation instructions <https://docs.anaconda.com/anaconda/install/>`_.
* Clone *ClearMap* from git
* Trigger the installation (which creates the environment...)

Please follow the steps below for simple installation from the terminal.

.. code-block:: bash

    cd /tmp
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh  # follow the instructions
    source ~/.bashrc  # reload the bashrc to activate conda
    git clone https://github.com/ChristophKirst/ClearMap2.git
    cd ClearMap2
    chmod +x install_gui.sh
    ./install.sh -f ClearMapUi39.yml

.. attention::
    The installation script will create a new conda environment called ClearMapUi39.
    The compilation of the ClearMap modules will take some time (about 15 minutes).


.. tip::
    The GUI installation script automatically creates a .ClearMap directory in your home directory.
    This directory contains the main settings file and the default configuration files for the
    ClearMap GUI. You can modify the settings in the .ClearMap directory to match your system configuration.
    The settings file is best edited through the *preferences* dialog in the ClearMap GUI.


.. note::
    Although *ClearMap* ships with the required libraries and should work out of the box,
    you can still configure some paths for *ClearMap* by editing the
    :download:`Settings.py <../../ClearMap/Settings.py>` file.

    See :mod:`~ClearMap.Settings`.


Running
=======

You can now run ClearMap by activating the ClearMap environment and starting the UI:

.. code-block:: bash

    conda activate ClearMapUi39
    clearmap-ui

Alternatively, you can run the ClearMap scripts directly from your IDE, see:
:mod:`~ClearMap.Scripts`.


Before running, modify the parameters and filenames to match your data and 
analysis.

.. deprecated:: 2.1.0
    The two main scripts :doc:`tubemap` and :doc:`cellmap` are now deprecated.
    Please use the new_api versions instead

You can also use jupyter to run ClearMap. Our tutorials notebooks (`CellMap notebook <_static/scripts/cell_map_tutorial.ipynb>`_ or
`TubeMap notebook <../../ClearMap/Scripts/tube_map_tutorial.ipynb>`_) are good starting points.....
