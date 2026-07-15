Functionality
=============

ClearMap 2.0 is designed for advanced and fast image processing of large
(Terabyte) 3D data sets [Kirst2020]_ obtained from tissue clearing. It is a 
complete redesign of 
`ClearMap 1.0 <https://www.github.com/ChristophKirst/ClearMap>`_ [Renier2016]_.

The modular source management allows a unified handling of various data sources
(image files, binary files, memory maps, shared memory arrays, numpy arrays,
GPU arrays, graph formats) and fast parallel 3D image and graph
processing as well as interactive visualization of large 3d images.

In the following we provide a list of the ClearMap 2.0 functionality.
`ClearMap 2.0 <https://github.com/ChristophKirst/ClearMap2>`_ is open source 
software and available for download under
https://github.com/ChristophKirst/ClearMap2.



Modules
-------

The ClearMap code is structured into these main modules:

   * `Alignment`_ for stitching, resampling, and registration of images onto references
   * `Analysis`_ for measurements and statistical analysis of the data
   * `ImageProcessing`_ for correcting and quantifying image data
   * `IO`_ for reading and writing data
   * `ParallelProcessing`_ for organizing parallel processing of the data
   * `Visualization`_ for visualizing the data and results.


Alignment
^^^^^^^^^

The :mod:`ClearMap.Alignment` module includes methods for

    * 3d resampling: 
      
        - :mod:`~ClearMap.Alignment.Resampling`
        
    * 3d alignment to reference atlases (e.g. 
      `Allen Brain Institute Atlases <https://portal.brain-map.org/>`_) via
      interfacing to
      `elastix <http://elastix.isi.uu.nl <http://elastix.isi.uu.nl>`_:
    
        - :mod:`~ClearMap.Alignment.Elastix`
        - :mod:`~ClearMap.Alignment.Annotation`
        
    * 3d rigid and wobbly stitching via :doc:`wobblystitcher`:
    
        - :mod:`~ClearMap.Alignment.Stitching.StitchingRigid`
        - :mod:`~ClearMap.Alignment.Stitching.StitchingWobbly`


Analysis
^^^^^^^^

The :mod:`~ClearMap.Analysis` module provides methods for the quantification
and analysis of the data, including:

    * graph and network analysis for very large graphs 
    
      - :mod:`~ClearMap.Analysis.Graphs`
      
      enabling:
        - graph preprocessing and cleanup
        - graph branch reduction
        - graph annotation 
        - graphs embedded 3d space
        - 3d graphs with 3d edge geometry
        - graph vertex and edge label morphological operations
        - sub-graph extraction
        - network analysis

    * measurement routines to quantify the results
      
      - :mod:`~ClearMap.Analysis.Measurements`
        
      enabling:
        - measurments of expression levels
        - measurments of geometric shapes and radii
        - maxima detection 
        - voxelization

    * statistics routines to analyse the results
      
      - :mod:`~ClearMap.Analysis.Statistics`
        

ImageProcessing
^^^^^^^^^^^^^^^

The :mod:`~ClearMap.ImageProcessing` module is the core of *ClearMap* and
provides methods to process 3d images of TB size, including:

  * binary image processing 
    
    - :mod:`~ClearMap.ImageProcessing.Binary`
    
    with filling and discrete topology based binary smoothing routines:
    
    - :mod:`~ClearMap.ImageProcessing.Binary.Filling`
    - :mod:`~ClearMap.ImageProcessing.Binary.Smoothing` 

  * clipping and normalization 
    
    - :mod:`~ClearMap.ImageProcessing.Clipping`
  
  * 3d local gradients and Hessian matrices
     
    - :mod:`~ClearMap.ImageProcessing.Differentiation`
  
    with 3d tube filter and tubeness measures:
    
    - :mod:`~ClearMap.ImageProcessing.Differentiation.Hessian`
  
  * 3d filtering
    
    - :mod:`~ClearMap.ImageProcessing.Filter` 
  
    with 3d rank filter library (>30 filters)
    
    - :mod:`~ClearMap.ImageProcessing.Filter.Rank`
  
  * skeletonization via parallel thinning
    
    - :mod:`~ClearMap.ImageProcessing.Skeletonization`
  
  * 3d tracing
    
    - :mod:`~ClearMap.ImageProcessing.Tracing`
  
  * fast calculation of 3d local image statistics
    
    - :mod:`~ClearMap.ImageProcessing.LocalStatistics`
  
  * fast 3d local image statistics
  
    - :mod:`~ClearMap.ImageProcessing.LocalStatistics`
  
  * hysteresis and seeded thresholding
    
    - :mod:`~ClearMap.ImageProcessing.Thresholding`
  
  * light-sheet artifact removal
    
    - :mod:`~ClearMap.ImageProcessing.LightsheetCorrection`
     
  * illuminatoin correction
    
    - :mod:`~ClearMap.ImageProcessing.IlluminationCorrection`
    
  * machine learning based image processing
    
    - :mod:`~ClearMap.ImageProcessing.MachineLearning`
    
    with vessel and tube filling deep convolutional neural network:
    
    - :mod:`~ClearMap.ImageProcessing.MachineLearning.VesselFilling`
  
  * expert processing pipelines for specific applications
    
    - :mod:`~ClearMap.ImageProcessing.Experts`


IO
^^

The :mod:`~ClearMap.IO` module provides methods to hold information about data
and read and write data files efficiently as sources and sinks, that can
be sliced and turned into virtual sources useful for parallel processing
and memory mapping:
  
  - :mod:`~ClearMap.IO.Source`
  - :mod:`~ClearMap.IO.Slice`

Supported source types include:
  
================ ============================ =============================================================
Format           Module                       Description
================ ============================ =============================================================
tif              :mod:`~ClearMap.IO.TIF`      tif images and stacks
raw / mhd        :mod:`~ClearMap.IO.MHD`      raw image files with optional mhd header file
nrrd             :mod:`~ClearMap.IO.NRRD`     nearly raw raster data files
csv              :mod:`~ClearMap.IO.CSV`      text files as comma separated values   
npy              :mod:`~ClearMap.IO.NPY`      numpy binary file
gt               :mod:`~ClearMap.IO.GT`       graph tool file
file list        :mod:`~ClearMap.IO.FileList` folder, file list or file expression for a list source files
-                :mod:`~ClearMap.IO.MMP`      memory mapped file
-                :mod:`~ClearMap.IO.SMA`      shared memory array
================ ============================ =============================================================

 
The :mod:`~ClearMap.IO` module also provides a workspace that handles the
organization of files in :doc:`cellmap` and :doc:`tubemap` projects:

  - :mod:`~ClearMap.IO.Workspace`
  
  
  
ParallelProcessing
^^^^^^^^^^^^^^^^^^

The :mod:`~ClearMap.ParallelProcessing` module provides methods for distributed
processing.

  * large data arrays can be proccessed in blocks via a specialized `IO`_ source

    - :mod:`~ClearMap.ParallelProcessing.Block`
    - :mod:`~ClearMap.ParallelProcessing.BlockProcessing`

  * or via shared memory arrays:

    - :mod:`~ClearMap.ParallelProcessing.SharedMemoryArray`
    - :mod:`~ClearMap.ParallelProcessing.SharedMemoryManager`

  * numerical processing routines for TB data arrays are collected in
    
    - :mod:`~ClearMap.ParallelProcessing.DataProcessing`
  
    including speed ups for numpy array processing, convolution and measurement
    routines:

      - :mod:`~ClearMap.ParallelProcessing.DataProcessing.ArrayProcessing`
      - :mod:`~ClearMap.ParallelProcessing.DataProcessing.ConvolvePointList`
      - :mod:`~ClearMap.ParallelProcessing.DataProcessing.DevolvePointList`
      - :mod:`~ClearMap.ParallelProcessing.DataProcessing.MeasurePointList`
      - :mod:`~ClearMap.ParallelProcessing.DataProcessing.StatisticsPointList`
  

Visualization
^^^^^^^^^^^^^

*ClearMap's* "mod:`ClearMap.Visualization` module comes with a larger set of
interactive visualization functions using various backends:

  * :mod:`~ClearMap.Visualization.Qt`
    
    providing:
    
    - fast interactive 2d slice plotting of 3d TB data sets
    
      - :mod:`~ClearMap.Visualization.Qt.DataViewer`
    
    - overlays and/or synchronized window display of multiple data sets.
    
      - :mod:`~ClearMap.Visualization.Qt.Plot3d`    

  * :mod:`~ClearMap.Visualization.Vispy`

    providing:
    
    -  3d volume rendering, lists and line plots
    
       - :mod:`~ClearMap.Visualization.Vispy.Plot3d`
    
    -  3d plots 3d graphs as lines or mesh plots with edge geometries, etc
    
       - :mod:`~ClearMap.Visualization.Vispy.PlotGraph3d`
