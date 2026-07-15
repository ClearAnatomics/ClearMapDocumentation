.. _package-organisation:

Package Organisation
====================

ClearMap is designed for advanced and fast image processing of large
(terabyte) 3-D datasets obtained from tissue clearing [Kirst2020]_
[Renier2016]_.

The modular source management allows unified handling of various data
sources (image files, memory maps, shared memory arrays, numpy arrays,
GPU arrays, graph formats) and fast parallel 3-D image and graph
processing as well as interactive visualisation of large 3-D images.

`ClearMap <https://github.com/ClearAnatomics/ClearMap>`_ is open-source
software released under the GPL v3 licence.


Architecture overview
---------------------

ClearMap 3.1 is organised into three layers:

**Pipeline orchestrators** (:mod:`~ClearMap.pipeline_orchestrators`)
    High-level workers that implement each processing pipeline end-to-end.
    These are what the GUI drives and what advanced users call directly in
    scripts.  Each orchestrator reads its parameters from YAML config files
    and writes outputs through the workspace.

    Key classes:

    - :class:`~ClearMap.pipeline_orchestrators.sample_info_management.SampleManager`
      — root object for a single experiment (channel definitions, workspace
      reconciliation, channel queries).
    - :class:`~ClearMap.pipeline_orchestrators.experiment_controller.ExperimentController`
      — wires config, sample manager, and all workers together; single
      entry point for UI patches.
    - :class:`~ClearMap.pipeline_orchestrators.cell_map.CellDetector`
      — cell detection, filtering, atlas alignment, voxelization.
    - :class:`~ClearMap.pipeline_orchestrators.tube_map.BinaryVesselProcessor`
      / :class:`~ClearMap.pipeline_orchestrators.tube_map.VesselGraphProcessor`
      — vessel binarization, graph construction, and annotation.
    - :class:`~ClearMap.pipeline_orchestrators.tract_map.TractMapProcessor`
      — myelinated-tract binarization and coordinate mapping.
    - :class:`~ClearMap.pipeline_orchestrators.colocalization.ColocalizationProcessor`
      — nearest-neighbour colocalization between channel pairs.
    - :class:`~ClearMap.pipeline_orchestrators.registration_orchestrator.RegistrationProcessor`
      — resampling and Elastix-based atlas registration.
    - :class:`~ClearMap.pipeline_orchestrators.stitching_orchestrator.StitchingProcessor`
      — rigid and wobbly stitching.

**Configuration system** (:mod:`~ClearMap.config`)
    YAML-based configuration with in-memory working model, atomic commits,
    JSON-schema validation, and automatic derivation of dependent fields via
    config adjusters.

    - :class:`~ClearMap.config.config_coordinator.ConfigCoordinator`
      — central coordinator (apply → adjust → validate → commit).
    - :class:`~ClearMap.config.config_handler.ConfigHandler`
      — file resolution and IO for YAML / ConfigObj / JSON.
    - :class:`~ClearMap.config.defaults_provider.DefaultsProvider`
      — three-level default precedence (user → packaged → code).

**Workspace and assets** (:mod:`~ClearMap.IO.workspace2`, :mod:`~ClearMap.IO.workspace_asset`)
    Channel-centred workspace that maps *(channel, asset_type)* pairs to
    on-disk :class:`~ClearMap.IO.workspace_asset.Asset` objects.

    - :class:`~ClearMap.IO.workspace2.Workspace2`
      — the workspace itself (persisted as ``workspace.yml``).
    - :class:`~ClearMap.IO.workspace_asset.Asset`
      — a single logical file or folder.


Modules
-------

   * `Alignment`_ — stitching, resampling, and registration
   * `Analysis`_ — measurements and statistical analysis
   * `ImageProcessing`_ — correcting and quantifying image data
   * `IO`_ — reading and writing data
   * `ParallelProcessing`_ — organising parallel processing
   * `Visualization`_ — visualising data and results


Alignment
^^^^^^^^^

.. include:: Alignment.rst


Analysis
^^^^^^^^
.. FIXME move to Analysis.__init__.py

The :mod:`~ClearMap.Analysis` module provides methods for the
quantification and analysis of the data, including:

* graph and network analysis for very large graphs

  - :mod:`~ClearMap.Analysis.graphs`

  enabling:

  - graph preprocessing and cleanup
  - graph branch reduction
  - graph annotation
  - graphs embedded in 3-D space
  - 3-D graphs with 3-D edge geometry
  - graph vertex and edge label morphological operations
  - sub-graph extraction
  - network analysis

* colocalization analysis between fluorescence channels

  - :mod:`~ClearMap.Analysis.colocalization`

* measurement routines to quantify the results

  - :mod:`~ClearMap.Analysis.Measurements`

  enabling:

  - measurements of expression levels
  - measurements of geometric shapes and radii
  - maxima detection
  - voxelization

* statistics routines to analyse the results

  - :mod:`~ClearMap.Analysis.Statistics`

* vasculature-specific analysis utilities

  - :mod:`~ClearMap.Analysis.vasculature`


ImageProcessing
^^^^^^^^^^^^^^^

.. FIXME move to ImageProcessing.__init__.py

The :mod:`~ClearMap.ImageProcessing` module is the core of *ClearMap*
and provides methods to process 3-D images of TB size, including:

* binary image processing

  - :mod:`~ClearMap.ImageProcessing.Binary`

  with filling and discrete topology-based binary smoothing routines:

  - :mod:`~ClearMap.ImageProcessing.Binary.Filling`
  - :mod:`~ClearMap.ImageProcessing.Binary.Smoothing`

* clipping and normalisation

  - :mod:`~ClearMap.ImageProcessing.Clipping`

* 3-D local gradients and Hessian matrices

  - :mod:`~ClearMap.ImageProcessing.Differentiation`

  with 3-D tube filter and tubeness measures:

  - :mod:`~ClearMap.ImageProcessing.Differentiation.Hessian`

* 3-D filtering

  - :mod:`~ClearMap.ImageProcessing.Filter`

  with 3-D rank filter library (>30 filters):

  - :mod:`~ClearMap.ImageProcessing.Filter.Rank`

* skeletonization via parallel thinning

  - :mod:`~ClearMap.ImageProcessing.Skeletonization`

* 3-D tracing

  - :mod:`~ClearMap.ImageProcessing.Tracing`

* fast calculation of 3-D local image statistics

  - :mod:`~ClearMap.ImageProcessing.LocalStatistics`

* hysteresis and seeded thresholding

  - :mod:`~ClearMap.ImageProcessing.Thresholding`

* light-sheet artifact removal

  - :mod:`~ClearMap.ImageProcessing.LightsheetCorrection`

* illumination correction

  - :mod:`~ClearMap.ImageProcessing.IlluminationCorrection`

* machine learning based image processing

  - :mod:`~ClearMap.ImageProcessing.machine_learning`

  with vessel and tube filling deep convolutional neural network:

  - :mod:`~ClearMap.ImageProcessing.machine_learning.vessel_filling`

* expert processing pipelines for specific applications

  - :mod:`~ClearMap.ImageProcessing.Experts`


IO
^^

The :mod:`~ClearMap.IO` module provides a unified interface to read and
write data in any format that ClearMap supports.  All format dispatch is
handled by :mod:`~ClearMap.IO.IO` so calling code never needs to import
format-specific modules directly. It is organised around the core concept
of the Source which allow slicing and conversion to and from virtual sources,
the cornerstone of ClearMaps parallel processing

Sources and sinks:

- :mod:`~ClearMap.IO.Source` — base source class
- :mod:`~ClearMap.IO.Slice` — virtual sliced sources for parallel
  processing

Workspace and assets (new in v3):

- :mod:`~ClearMap.IO.workspace2` — channel-centred workspace
- :mod:`~ClearMap.IO.workspace_asset` — on-disk asset model
- :mod:`~ClearMap.IO.assets_constants` — asset type registry
- :mod:`~ClearMap.IO.assets_specs` — TypeSpec, ChannelSpec, StateManager

Supported source types:

================ ============================ =====================================================
Format           Module                       Description
================ ============================ =====================================================
tif              :mod:`~ClearMap.IO.TIF`      tif images and stacks
raw / mhd        :mod:`~ClearMap.IO.MHD`      raw image files with optional mhd header file
nrrd             :mod:`~ClearMap.IO.NRRD`     nearly raw raster data files
csv              :mod:`~ClearMap.IO.CSV`      text files as comma separated values
npy              :mod:`~ClearMap.IO.NPY`      numpy binary file
gt               :mod:`~ClearMap.IO.GT`       graph tool file
file list        :mod:`~ClearMap.IO.FileList` folder, file list or file expression for source files
\-               :mod:`~ClearMap.IO.MMP`      memory mapped file
\-               :mod:`~ClearMap.IO.SMA`      shared memory array
================ ============================ =====================================================


ParallelProcessing
^^^^^^^^^^^^^^^^^^

The :mod:`~ClearMap.ParallelProcessing` module provides methods for
distributed processing.

* large data arrays can be processed in blocks via a specialised
  `IO`_ source

  - :mod:`~ClearMap.ParallelProcessing.Block`
  - :mod:`~ClearMap.ParallelProcessing.BlockProcessing`

* or via shared memory arrays

  - :mod:`~ClearMap.ParallelProcessing.SharedMemoryArray`
  - :mod:`~ClearMap.ParallelProcessing.SharedMemoryManager`

* numerical processing routines for TB data arrays are collected in

  - :mod:`~ClearMap.ParallelProcessing.DataProcessing`

  including speed-ups for numpy array processing, convolution and
  measurement routines:

  - :mod:`~ClearMap.ParallelProcessing.DataProcessing.ArrayProcessing`
  - :mod:`~ClearMap.ParallelProcessing.DataProcessing.ConvolvePointList`
  - :mod:`~ClearMap.ParallelProcessing.DataProcessing.DevolvePointList`
  - :mod:`~ClearMap.ParallelProcessing.DataProcessing.MeasurePointList`


Visualization
^^^^^^^^^^^^^

:mod:`ClearMap.Visualization` comes with a large set of interactive
visualisation functions using various backends:

* :mod:`~ClearMap.Visualization.Qt`

  providing:

  - fast interactive 2-D slice plotting of 3-D TB datasets

    - :mod:`~ClearMap.Visualization.Qt.DataViewer`

  - overlays and/or synchronised window display of multiple datasets

    - :mod:`~ClearMap.Visualization.Qt.Plot3d`

  - scatter overlays with depth display and atlas-region colouring

    - :class:`~ClearMap.Visualization.Qt.widgets.Scatter3D`

* :mod:`~ClearMap.Visualization.Vispy`

  providing:

  - 3-D volume rendering, list and line plots

    - :mod:`~ClearMap.Visualization.Vispy.Plot3d`

  - 3-D graph plots as lines or mesh with edge geometries

    - :mod:`~ClearMap.Visualization.Vispy.plot_graph_3d`


GUI
^^^

The :mod:`~ClearMap.gui` package provides a PyQt5-based graphical user
interface that exposes every pipeline step without requiring scripting.
See :ref:`gui` for a full walkthrough.

- :mod:`~ClearMap.gui.app` — main window and application entry point
- :mod:`~ClearMap.gui.tabs` — concrete tab classes for each pipeline step
- :mod:`~ClearMap.gui.params` — parameter-link objects (UI ↔ YAML config)
- :mod:`~ClearMap.gui.widgets` — custom Qt widgets (scatter, progress, etc.)
