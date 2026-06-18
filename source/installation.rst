.. _installation:

Installation
------------

Computing Resources
===================

ClearMap is designed for high-performance workstations or clusters.
Minimum recommended specifications:

* **RAM**: 256 GB
* **CPU**: 12 cores
* **Storage**: Fast SSDs, NVMe preferred in a RAID0 configuration
* **GPU**: nVidia GPU with ≥ 24 GB VRAM (required for the vasculature
  deep-filling step; optional otherwise)

ClearMap has been tested on Ubuntu 20.04 LTS and later.

.. note::
    The vasculature pipeline's deep vessel filling step
    (:class:`~ClearMap.pipeline_orchestrators.tube_map.BinaryVesselProcessor`)
    requires a CUDA-capable nVidia GPU with at least 24 GB of VRAM.
    All other pipelines run on CPU only.


Getting ClearMap
================

ClearMap currently runs on **Linux**.  Some components may work on
Windows or macOS but these platforms are not officially supported.

Required system packages before starting:

.. code-block:: bash

    sudo apt install build-essential git

And, if you plan to use the vasculature pipeline, recent proprietary
nVidia drivers.

Choosing a package manager
~~~~~~~~~~~~~~~~~~~~~~~~~~

ClearMap requires `conda <https://conda.io>`_.
We recommend **Miniforge** over Anaconda or Miniconda for two reasons:

1. **Pricing policy** — Anaconda Inc. changed its terms of service in
   2023; the default ``defaults`` channel is no longer free for many
   organisations.  Miniforge uses the community-maintained
   ``conda-forge`` channel, which is always free.
2. **PyTorch compatibility** — Pytorch decided to move to pip only.

.. warning::
    Several users have reported environment-solve failures when
    installing ClearMap under full Anaconda.  If you already have
    Anaconda installed you can still try, but Miniforge is strongly
    recommended.  The symptoms are typically unsatisfiable dependency
    conflicts during the ``conda env create`` step.

Install Miniforge
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /tmp
    wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
    bash Miniforge3-Linux-x86_64.sh   # accept the licence, confirm init
    source ~/.bashrc                   # reload to activate conda


Install ClearMap
~~~~~~~~~~~~~~~~

.. code-block:: bash

    git clone https://github.com/ClearAnatomics/ClearMap.git
    cd ClearMap
    chmod +x install_gui.sh
    ./install_gui.sh

.. attention::
    The installer creates a conda environment called **ClearMap3.1** and
    compiles all Cython extensions.  This takes approximately 15–30 minutes
    depending on your hardware.

.. tip::
    The installer creates ``~/.clearmap/`` which holds the main settings
    file and default configuration templates.  You can review these
    settings through the **Preferences** dialog inside the GUI rather
    than editing them by hand.

.. note::
    For advanced path configuration (e.g. custom atlas locations) see
    :mod:`~ClearMap.Settings` and
    :download:`Settings.py <../../ClearMap/Settings.py>`.


Running ClearMap
================

GUI (recommended)
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    conda activate ClearMap3.1
    clearmap-ui

Scripted / headless use
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    conda activate ClearMap3.1

    # Cell detection
    python -m ClearMap.Scripts.cell_map_new_api /path/to/experiment

    # Vasculature
    python -m ClearMap.Scripts.tube_map_new_api /path/to/experiment

Full script source and interactive usage examples are in :ref:`usage`.
