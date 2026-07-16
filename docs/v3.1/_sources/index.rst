ClearMap Documentation
======================

.. toctree::
    :hidden:
    :maxdepth: 2

    overview
    getting_started
    installation
    usage
    package_organisation
    gui/index
    advanced/advanced_usage
    api
    media
    references

..    static/scripts/cell_map_tutorial
    advanced/wobblystitcher
    cellmap
    tubemap
    scripts/cell_map_tutorial

**Date**: |today| **Version**: |version|

**Useful links**:
`Source Repository <https://github.com/ChristophKirst/ClearMap2>`__ |
`Issues & Ideas <https://github.com/ChristophKirst/ClearMap2/issues>`__ |
`License <../LICENSE>`__

.. raw:: html

    <div id="cmCarousel" class="carousel slide scc-shadow-control"
         data-bs-ride="carousel" data-bs-interval="4000">

      <div class="carousel-indicators scc-top-indicator scc-shadow-indicator">
        <button type="button" data-bs-target="#cmCarousel" data-bs-slide-to="0"
                class="active" aria-current="true"></button>
        <button type="button" data-bs-target="#cmCarousel" data-bs-slide-to="1"></button>
        <button type="button" data-bs-target="#cmCarousel" data-bs-slide-to="2"></button>
        <button type="button" data-bs-target="#cmCarousel" data-bs-slide-to="3"></button>
        <button type="button" data-bs-target="#cmCarousel" data-bs-slide-to="4"></button>
      </div>

      <div class="carousel-inner">

        <div class="carousel-item active">
          <img src="_static/ClearMap_banner.jpg" class="d-block w-100" alt="ClearMap">
          <div class="carousel-caption scc-below-control">
            <h5>ClearMap</h5>
            <p>High-performance volumetric image analysis</p>
          </div>
        </div>

        <div class="carousel-item">
          <img src="_static/stitching_banner.png" class="d-block w-100" alt="Stitching">
          <div class="carousel-caption scc-below-control">
            <h5>Custom stitching</h5>
            <p>Tile stitching for terabyte-scale datasets</p>
          </div>
        </div>

        <div class="carousel-item">
          <img src="_static/sagittal_cell_count_banner.png" class="d-block w-100" alt="Cell counting">
          <div class="carousel-caption scc-below-control">
            <h5>Cell counting</h5>
            <p>Whole-brain cell detection and atlas mapping</p>
          </div>
        </div>

        <div class="carousel-item">
          <img src="_static/vasculature_banner_bright.png" class="d-block w-100" alt="Vasculature">
          <div class="carousel-caption scc-below-control">
            <h5>Brain vasculature</h5>
            <p>Graph-based vessel network analysis</p>
          </div>
        </div>

        <div class="carousel-item">
          <img src="_static/development_banner.png" class="d-block w-100" alt="Development">
          <div class="carousel-caption scc-below-control">
            <h5>Brain development</h5>
            <p>Developmental atlas registration and comparison</p>
          </div>
        </div>

      </div>

      <button class="carousel-control-prev scc-top-control scc-shadow-control"
              type="button" data-bs-target="#cmCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next scc-top-control scc-shadow-control"
              type="button" data-bs-target="#cmCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
        <span class="visually-hidden">Next</span>
      </button>

    </div>

|

:mod:`ClearMap` is an open source, GPL-licensed program and set of libraries providing high-performance,
easy-to-use tools to analyse TB scale volumetric image datasets using the `Python <https://www.python.org/>`__
programming language.


*ClearMap* has been written for mapping immediate early genes [Renier2016]_
as well as vasculature networks of whole mouse brains [Kirst2020]_


.. grid:: 1 2 2 2
    :gutter: 4
    :padding: 2 2 0 0
    :class-container: sd-text-center

    .. grid-item-card:: Getting started
        :img-top: static/index_getting_started.svg
        :class-card: intro-card
        :shadow: md

        The getting started guides provide an overview of the *ClearMap* software
        and how to use it. It is recommended to start here if you are new to *ClearMap*.

        +++

        .. button-ref:: getting_started
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the getting started guides

    .. grid-item-card::  GUI
        :img-top: static/gui-symbol.svg
        :class-card: intro-card
        :shadow: md

        The GUI documentation provides an overview of the graphical user interface. If you
        want to perform analysis without writing scripts, this is the place to start.

        +++

        .. button-ref:: gui
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the GUI documentation

    .. grid-item-card::  Advanced usage
        :img-top: static/index_user_guide.svg
        :class-card: intro-card
        :shadow: md

        The user guide provides a detailed description of the *ClearMap* software and how to use it.
        This is meant for more advanced users who want to understand the software in more detail or
        want to write their own scripts.

        +++

        .. button-ref:: advanced_usage
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the user guide

    .. grid-item-card::  API reference
        :img-top: static/index_api.svg
        :class-card: intro-card
        :shadow: md

        The API reference provides a detailed description of the *ClearMap* modules and functions.
        This will be your go-to place if you want to write your own scripts or understand the
        underlying algorithms.

        +++

        .. button-ref:: api
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the reference guide


Navigating
----------

`Table of Contents <toc.rst>`__ | :ref:`genindex` | :ref:`modindex` | :ref:`search`
