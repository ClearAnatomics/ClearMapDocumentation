Installation
============

*ClearMap* can be installed in different ways. 
We recommend installation via `Anaconda <https://www.anaconda.com>`_.
The altenative is to install from source on `Github <https://www.github.com/ChristophKirst/ClearMap2>`_.


Installation with Anaconda
--------------------------

* download `Anaconda <https://www.anaconda.com>`_ 

  Install anaconda for Python 3 for your OS and install it folliwng 
  the `installation instructions <https://docs.anaconda.com/anaconda/install/>`_.


* clone *ClearMap* from git
  
  See `Cloning`_.
  
  
* create a *ClearMap* conda enviroment using the clear map environment file
  :download:`ClearMap.yml <../../ClearMap.yml>`.
 
  In a terminal change to the ClearMap root folder and type
 
  .. code:: bash
     
     $ conda env create -f ClearMap.yml
 
 
* activate your environment

  .. code:: bash
    
     $ conda activate ClearMap
   
   
* optionally compile *ClearMap* modules

  See `Compilation`_.


* run *ClearMap* 

  See `Running`_.
  

* trouble shooting

  The above might fail due to newer packages than we used to test our code.
  In that case you can use the 
  :download:`ClearMap_stable.yml <../../ClearMap_stable.yml>` environment 
  file with frozen package versions that works. 
  
   
Installation via Github
-----------------------

* clone *ClearMap* via git

  See `Cloning`_.

* install the depencies

  See `Dependencies`_.
   
* optionally compile *ClearMap* modules

  See `Compilation`_.


* run *ClearMap* 

  See `Running`_.


Cloning
-------

To clone *ClearMap* make sure git is installed. 

In a terminal change to a folder in which you like to place ClearMap and run
    
.. code:: bash
   
   $ cd path/to/clearmap
   $ git clone https://github.com/ChristophKirst/ClearMap2.git


Compilation 
------------

All modules are automatically compiled on their first run via cython.
 
.. note::
    On first run, compiling the various modules may take up to 5-15 minutes!
    
To trigger compilaltion of all modules in a single step you run the following
in a python console:

>>> import ClearMap.Compile



Running     
-------   

To run *ClearMap*  we recommend to use `spyder <https://www.spyder-ide.org/>`_
or `jupyer <https://jupyter.org>`_.


Both will be automatically installed in the ClearMap anaconda environment.

To run an analysis *ClearMap* provides main scripts in 
:mod:`~ClearMap.Scripts`. 

In spyder, open one of the scripts in the editor and execute the individual 
cells by placig the cursor in the cell and use Shift + Enter.

Before running, modify the parameters and filenames to match your data and 
analysis.
   
The two main scripts are :doc:`tubemap` and :doc:`cellmap'.

If you want to set up the ClearMap functions in a python console run

>>> from ClearMap.Environment import *

You can also use jupyter to run ClearMap. Our tutorials for
:ref:`CellMap.ipynb</CellMap.ipynb>` and :ref:`TubeMap.ipynb</TubeMap.ipynb>` 
are good points to start.


Configuration
-------------

To configure *ClearMap* open and edit the
:download:`Settings.py <../../ClearMap/Settings.py>` file.

See :mod:`~ClearMap.Settings`.


Dependencies
------------

The list of names of python libraries required by ClearMap can be 
found in the environment file :download:`ClearMap.yml <../../ClearMap.yml>`.


To satisfy all the dependencies the easiet is create a *ClearMap* environement 
via ``conda``:

.. code:: bash

   $ conda env create -f ClearMap.yml

Alternatively you can install the python dependencies via ``pip`` and use

.. code:: bash 
   
   $ pip install name

You can also do this via the OS software management, e.g. via ``apt-get`` by
using

.. code:: bash 
   
   $ sudo apt-get name


For exmple, if you’re starting from a fresh Ubuntu install, for instance, 
here are the steps to complete the installation. Open a terminal window and 
type the following instructions:

* Install pip
  
  .. code:: bash
    
     $ sudo apt-get update
     $ sudo apt-get install python-pip


* Install spyder
  
  .. code:: bash

     $ sudo apt-get install spyder


* Install the necessary libraries
  
  .. code:: bash

     $ sudo -H pip install python-opencv
     $ sudo -H pip install cython
     $ sudo -H pip install scikit-image
     $ ...


Computing Resources
-------------------

The processing with *CellMap* and *TubeMap* is best done on local workstations
or a cluster.

The minimal requirements for resonable performance are:
  * 256GB RAM
  * 12 CPUs
  * 24GB VRAM
  
For our work we used either a Dell Precision T7920 or HP Z840 workstation. 
Each workstation was equipped with 2 Intel Xeon Gold 6128 3.4G 6C/12T CPUs, 
512Gb of 2666MHz DDR4 RAM, 4x1Tb NVMe Class 40 Solid State Drives in a RAID0
array (plus a separate system disk), and an NVIDIA Quadro P6000, 24Gb VRAM 
video card. 

The workstations were operated by Linux Ubuntu 18.04LTS.
