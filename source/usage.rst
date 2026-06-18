.. _usage:

Usage
=====

GUI (recommended)
-----------------

The simplest way to use *ClearMap* is through the Graphical User Interface:

.. code-block:: bash

    conda activate ClearMap3.1
    clearmap-ui

The GUI guides you through every pipeline step — sample configuration,
stitching, registration, cell detection, and vasculature analysis — and
writes all results to a workspace directory.

See :ref:`gui` for a full walkthrough.


Scripted / headless use
-----------------------

For batch processing or HPC environments, use the new-API scripts.

.. code-block:: bash

    conda activate ClearMap3.1

    # Cell detection
    python -m ClearMap.Scripts.cell_map_new_api /path/to/experiment

    # Vasculature
    python -m ClearMap.Scripts.tube_map_new_api /path/to/experiment

Both scripts call
:func:`~ClearMap.pipeline_orchestrators.utils.init_sample_manager_and_processors`
to initialise the experiment, then run stitching, registration, and
pipeline-specific steps.  Edit the YAML config files in your experiment
folder to control parameters rather than editing the scripts themselves.

**Cell detection (CellMap)**

.. literalinclude:: ../../ClearMap/Scripts/cell_map_new_api.py
   :language: python
   :caption: ClearMap/Scripts/cell_map_new_api.py

**Vasculature (TubeMap)**

.. literalinclude:: ../../ClearMap/Scripts/tube_map_new_api.py
   :language: python
   :caption: ClearMap/Scripts/tube_map_new_api.py

See :doc:`cellmap` and :doc:`tubemap` for pipeline-specific documentation.


Interactive / console use
--------------------------

For exploratory analysis in IPython, Jupyter, or an IDE, import only
what you need:

.. code-block:: python

    # IO — read and write any supported format
    import ClearMap.IO.IO as io

    data   = io.read('volume.npy')
    source = io.as_source('volume.tif', slicing=(slice(0, 100),))
    print(source.shape, source.dtype)
    io.write('output.tif', data)

.. code-block:: python

    # Workspace and sample manager
    from ClearMap.pipeline_orchestrators.sample_info_management import build_sample_manager

    sm  = build_sample_manager('/path/to/experiment')
    raw = sm.get('raw', channel='cfos')
    print(raw.is_tiled, raw.tile_grid_shape)

.. code-block:: python

    # Graph analysis
    from ClearMap.Analysis.graphs.graph_gt import Graph

    g = Graph.load('/path/to/graph.gt')
    print(g.n_vertices, g.n_edges)

.. code-block:: python

    # 3-D visualisation
    import ClearMap.Visualization.Qt.Plot3d as plot_3d

    plot_3d.plot('volume.tif')

.. note::
    On first run, Cython sub-modules are compiled on demand.
    This takes 10–30 minutes but only happens once per installation.

.. deprecated:: 3.1.0

    ``from ClearMap.Environment import *`` (the old convenience namespace)
    is no longer recommended.  Wildcard imports from large packages make
    dependencies opaque and break static analysis tools.  Use explicit
    imports as shown above.


.. _deprecated_scripts:

Deprecated scripts
------------------

.. deprecated:: 2.1.0

    The monolithic scripts below are retained for reference but will be
    removed in a future release.  Use the new-API scripts or the GUI instead.

    .. list-table::
       :header-rows: 1
       :widths: 25 20 55

       * - Script
         - Documentation
         - Replacement
       * - :mod:`~ClearMap.Scripts.CellMap`
         - :doc:`cellmap`
         - :mod:`~ClearMap.Scripts.cell_map_new_api`
       * - :mod:`~ClearMap.Scripts.TubeMap`
         - :doc:`tubemap`
         - :mod:`~ClearMap.Scripts.tube_map_new_api`

    See :ref:`v3_migration` for a full comparison of the old and new APIs.


.. toctree::
    :hidden:
    :maxdepth: 2

    overview
    functionality
    advanced/wobblystitcher
    cellmap
    tubemap
