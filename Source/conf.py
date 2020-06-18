# -*- coding: utf-8 -*-
#
# ClearMap documentation build configuration file
#
__author__    = 'Christoph Kirst <christoph.kirst.ck@gmail.com>'
__license__   = 'GPLv3 - GNU General Pulic License v3 (see LICENSE)'
__copyright__ = 'Copyright © 2020 by Christoph Kirst'
__webpage__   = 'http://idisco.info'
__download__  = 'http://www.github.com/ChristophKirst/ClearMap2'

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, basedir)
sys.path.insert(0, os.path.join(basedir, 'Documentation/Source/Extensions'))

# -- Setup --------------------------------------------------------------------

def setup(app):
  app.add_stylesheet('clearmap_utils.css')
  app.add_stylesheet('clearmap_sidebar.css')
#  app.add_javascript('clearmap_togglebutton.js')
#  app.add_javascript('cleatmap_sidebar.js')
  
  #cut title in modules
  from typing import Any, Callable, List
  from sphinx.application import Sphinx
  def cut_header(pre: int = 2, what: str = None) -> Callable:
    def process(app: Sphinx, what_: str, name: str, obj: Any, options: Any, lines: List[str]) -> None:
      if what and what_ not in what:
          return
      if len(lines) >= 2 and len(lines[1]) > 0 and lines[1][0] in ['-', '=', '^']:
        #print(name, )
        #print(lines[:pre])
        del lines[:pre]
        if lines and lines[-1]:
            lines.append('')
    return process;

  
  app.connect('autodoc-process-docstring', cut_header(2, what=['module']))


# -- General configuration ----------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode', 
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
#    'sphinx.ext.autosectionlabel',
    'matplotlib.sphinxext.mathmpl',  
#    'matplotlib.sphinxext.only_directives',
#    'matplotlib.sphinxext.plot_directive', 
    'twitter',
    'youtube',
    'autopackagesummary',
    'sphinx_copybutton',
    'nbsphinx'
]

master_doc = 'index'

templates_path = ['Templates']

exclude_patterns = ['Build', 'docs']

source_suffix = '.rst'


modindex_common_prefix = ['ClearMap.']

autosummary_mock_imports = ['ClearMap.External.geodesic_distance',
                            'ClearMap.External.pickle_python_2',
                            #'ClearMap.Scripts.TubeMap',
                            #'ClearMap.Scripts.CellMap'
                           ];

# debug - speed up compilation for testing
debug = False;
if debug:
  autosummary_mock_imports += ['ClearMap.Analysis',
                               'ClearMap.External',
                               'ClearMap.ImageProcessing',
                               'ClearMap.IO',
                               'ClearMap.ParallelProcessing',
                               'ClearMap.Resources',
                               #'ClearMap.Scripts',
                               'ClearMap.Tests',
                               'ClearMap.Utils',
                               'ClearMap.Visualization'];
# -- Project information ------------------------------------------------------

import ClearMap
project   = ClearMap.__title__
copyright = ClearMap.__copyright__
version   = ClearMap.__version__
release   = ClearMap.__version__

# -- General config -----------------------------------------------------------

show_authors = True

add_module_names = False

numfig = True;
numfig_format = {'figure'  : "Figure %s", 
                 'table'   : 'Table %s', 
                 'section' : 'Section %s'};
numfig_secnum_depth = 1;

html_sourcelink_suffix = ''

#use gif for html
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

# -- Autodoc configuration ----------------------------------------------------

#autodoc_member_order = 'bysource'
autodoc_member_order = 'groupwise'

autodoc_default_options = {'members' : True, 
                           'undoc-members' : True, 
                           'show-inheritance' : True
                           #'inherited-members' : True
                          }


autosummary_generate = True

autosummary_imported_members = True


# -- Napoleon configuration ---------------------------------------------------

napoleon_custom_sections = ["Arguments", "Returns", "References", 
                            "Note", "Examples",                            
                            "Illumination correction", "Background removal",
                            "Equalization", "DoG Filter",
                            "Maxima Detection", "Shape detection",
                            "Intensity detection", "General parameter",
                            "Clipping", "Lightsheet correction",
                            "Median filter", "Pseudo Deconvolution",
                            "Adaptive Thresholding", "Equalization",
                            "Tube filter", "Binary filling", "Binary smoothing",
                            "Smoothing", "Filling" ]


napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False

napoleon_google_docstring = False
napoleon_numpy_docstring = True

napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False


# -- Options for HTML output --------------------------------------------------

html_theme_path = ['./Themes'];

html_theme = 'ClearMap'

html_static_path = ['Static']


html_sidebars = { '**': ['sidebar.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }

html_additional_pages = {'home': 'home.html'}

htmlhelp_basename = 'ClearMapDoc'


html_use_index = True

html_split_index = False

html_show_sourcelink = True

html_show_copyright = True

html_show_sphinx = False


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'clearmap.tex', u'ClearMap Documentation', u'Christoph Kirst', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'clearmap', u'ClearMap Documentation',
     [u'Christoph Kirst'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'ClearMap', u'ClearMap Documentation',
   u'Christoph Kirst', 'ClearMap', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False




