.. _advanced_usage:

.. toctree::
    :hidden:

    wobblystitcher
    cell_map_advanced
    tube_map_advanced

ClearMap pipelines
==================

.. include:: ../introduction.rst

Installation
------------
For installation instructions, see :ref:`installation`.

Usage
-----
This is a guide for **advanced usage** (including custom pipelines) of *ClearMap*.
For **basic usage** see :ref:`gui`.


Functionality and Pipelines
---------------------------

ClearMap provides a larger set of high performance 3d image processing
functions that are introduced here: :doc:`../functionality`.

These functions are combined together in expert functions under
:mod:`~ClearMap.ImageProcessing.Experts` which are made use of in
pipelines found in :mod:`~ClearMap.Scripts` to quantify the data sets.

`CellMapPipeline`

The main tools are:

.. grid:: 1 2 2 2
    :gutter: 4
    :padding: 2 2 0 0
    :class-container: sd-text-center

    .. grid-item-card:: Stitching
        :img-top: ../static/stitching_icon.svg
        :class-card: intro-card
        :shadow: md

        *ClearMap* provides a stitching pipeline based on a custom algorithm implemented
        in the *Wobbly Stitcher* module.

        +++

        .. button-ref:: wobbly_stitcher
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            Wobbly stitcher

    .. grid-item-card::  Alignment
        :img-top: ../static/overlay.svg
        :class-card: intro-card
        :shadow: md

        The alignment pipeline is based on the *Elastix* library and provides
        the tools to align samples to a reference brain and to label discrete objects
        with the corresponding brain region.

        +++

        .. button-ref:: alignment
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            Brain registration

    .. grid-item-card::  Cell Detection
        :img-top: ../static/cells.svg
        :class-card: intro-card
        :shadow: md

        The *CellMap* pipeline is used for high performance, parallelized cell detection,
        labeling and quantification.

        +++

        .. button-ref:: cell_map_advanced
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To CellMap

    .. grid-item-card::  Vasculature analysis
        :img-top: ../static/vasculature.svg
        :class-card: intro-card
        :shadow: md

        The *TubeMap* pipeline is used for high performance, parallelized vasculature detection,
        labeling and quantification.

        +++

        .. button-ref:: tube_map_advanced
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To TubeMap
