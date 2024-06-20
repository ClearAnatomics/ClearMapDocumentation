# -*- coding: utf-8 -*-
#
# ClearMap documentation build configuration file
#
__author__ = 'Christoph Kirst <christoph.kirst.ck@gmail.com>'
__license__ = 'GPLv3 - GNU General Public License v3 (see LICENSE)'
__copyright__ = 'Copyright © 2024 by Christoph Kirst, Charly Rousseau, and the ClearMap team'
__webpage__ = 'https://idisco.info'
__download__ = 'https://www.github.com/ChristophKirst/ClearMap2'

import os
import sys
from pathlib import Path
import shutil
import pkgutil

from sphinx.builders.html import StandaloneHTMLBuilder

from documentation.source.custom_autodoc import CustomAutosummaryRenderer

# =============================================================================
# ============================ Path setup ======================================
# =============================================================================

# Add paths to the modules to document and sphinx extensions
doc_dir = Path(__file__).absolute().parent
clearmap_dir = doc_dir.parent.parent
sys.path.insert(0, str(clearmap_dir))  # Add ClearMap to the path
sys.path.insert(1, str(clearmap_dir / 'IO'))  # Add ClearMap to the path
sys.path.insert(2, str(doc_dir / 'extensions'))  # Add extensions to the path

import ClearMap.custom_scripts
from ClearMap import Settings

license_path = Path(Settings.clearmap_path).parent / 'licenses/LICENSE.txt'
cell_map_nb_path = Path(Settings.clearmap_path) / 'Scripts/cell_map_tutorial.ipynb'
tube_map_nb_path = Path(Settings.clearmap_path) / 'Scripts/tube_map_tutorial.ipynb'
rst_epilog = f"""
.. |license_path| replace:: {license_path}
.. |cell_map_nb_path| replace:: {cell_map_nb_path}
.. |tube_map_nb_path| replace:: {tube_map_nb_path}
"""
# FIXME: check if the above does anything useful

# =============================================================================
# ============================ Project information =============================
# =============================================================================
project = ClearMap.__title__
copyright = ClearMap.__copyright__
version = ClearMap.__version__
release = ClearMap.__version__


# def has_submodules(package_name):
#     # print(package_name)
#     package_name = str(package_name)
#     try:
#         package = __import__(package_name)
#         return any(pkgutil.iter_modules(package.__path__))
#     except ImportError:
#         return False


def post_process_documentation(app, exclude_dirs, paths_to_replace, replacement, extension='.html'):
    """
    Browse doc_dir recursively and in each .rst file, replace any path from
    `paths_to_replace` with `replacement`

    Parameters
    ----------
    app: sphinx.application.Sphinx
        The Sphinx application
    exclude_dirs : list[str]
        The list of directories to exclude
    paths_to_replace : list[str]
        The list of path that should be replaced by `replacement`
    replacement : str
        The replacement string
    extension : str
        The extension of the files to process

    Returns
    -------

    """
    print('-' * 80)
    print(f'Post processing documentation in {app.srcdir} with {paths_to_replace} -> {replacement}')
    print('-' * 80)
    for root, _, files in os.walk(app.outdir):
        # Skip directories in exclude_dirs
        if any(exclude_dir in root for exclude_dir in exclude_dirs):
            print(f'Skipping excluded folder {root}')
            continue
        else:
            print(f'Processing folder {root}')
        for file in files:
            if file.endswith(extension):
                # print(f'Processing file {file}')
                src_file_path = os.path.join(root, file)
                with open(src_file_path, 'r') as in_file, open(src_file_path, 'w') as out_file:
                    file_content = in_file.read()
                    for path in paths_to_replace:
                        if path in file_content:
                            print(f'\tWould replace {path} with {replacement} in {src_file_path}')
                    else:
                        print(f'\tNo replacement needed in {src_file_path}')
                        # file_content = file_content.replace(path, replacement)
                    # out_file.write(file_content)


def cleanup(app, exception):
    # The directory containing the generated .rst files
    paths_to_replace = [os.path.abspath(os.path.expanduser('~/'))]  # The paths to replace
    replacement = '~/'  # The replacement string
    exclude_dirs = ['_build', 'static', 'templates', 'extensions', 'deprecated', 'spikes', 'themes']
    post_process_documentation(app, exclude_dirs, paths_to_replace, replacement)
    return []  # To comply with the sphinx extension API


# -- Setup --------------------------------------------------------------------
def setup(app):
    def cut_header(pre=2, what=None):
        """
        Cut title in modules to avoid duplication of the module name with automodule

        Parameters
        ----------
        pre
        what

        Returns
        -------

        """
        def process(app, what_, name, obj, options, lines):
            if what and what_ not in what:
                return
            if len(lines) >= 2 and len(lines[1]) > 0 and lines[1][0] in ['-', '=', '^']:
                del lines[:pre]
                if lines and lines[-1]:
                    lines.append('')
        return process

    app.connect('autodoc-process-docstring', cut_header(2, ['module']))
    import sphinx
    sphinx.ext.autosummary.generate.AutosummaryRenderer = CustomAutosummaryRenderer
    # sphinx.ext.autosummary.generate.generate_autosummary_docs = custom_generate_autosummary_docs
    # app.connect('build-finished', cleanup)


# -- General configuration ----------------------------------------------------
extensions = [
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autopackagesummary',
    'sphinx_copybutton',
    'sphinx.ext.viewcode', 
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'matplotlib.sphinxext.mathmpl',
    'sphinx_design',   # For grid design
    'sphinxcontrib.youtube',
    'sphinx_carousel.carousel'
]

master_doc = 'index'
templates_path = ['templates']
source_suffix = '.rst'

show_authors = True
add_module_names = False

numfig = True
numfig_format = {'figure': "Figure %s",
                 'table': 'Table %s',
                 'section': 'Section %s'}
numfig_secnum_depth = 1

# =============================================================================
# ================================ Modules ====================================
# =============================================================================

exclude_patterns = ['Build', 'docs', 'tests', 'Tests', 'GUI', 'Resources', 'External',
                    'Examples', 'static', 'themes', 'extensions', 'deprecated', 'spikes']

modindex_common_prefix = ['ClearMap.']

autosummary_mock_imports = [
    'ClearMap.Compile',
    'ClearMap.External',
    'ClearMap.Tests',
    'ClearMap.Tests.Files',
    'ClearMap.External.geodesic_distance',
    'ClearMap.External.pickle_python_2',
    'ClearMap.Environment',
    'ClearMap.IO.workspace2',
    'ClearMap.IO.workspace_asset',
    'ClearMap.Visualization.PyVista',
    'ClearMap.Visualization.volcano',
    'ClearMap.Visualization.spikes',
    'ClearMap.Visualization.GUI',
    'ClearMap.gui.run_gui',
    'ClearMap.gui.spikes',
    'ClearMap.Scripts.vasculature_stats_scripts',
    'ClearMap.Scripts.total_length_and_basic_stats',
    'ClearMap.Scripts.realign_static',
    'ClearMap.Scripts.script_3d',
    'ClearMap.Scripts.streamlined_flow',
    'ClearMap.Scripts.test_file_list',
    'ClearMap.Scripts.test_resampling',
    'ClearMap.custom_scripts',
    'ClearMap.Analysis.vasculature.flow.linearSystem',
    'ClearMap.ParallelProcessing.DataProcessing.statistics.StatisticsPointList',
    'ClearMap.ParallelProcessing.DataProcessing.statistics.StatisticsPointListCode',
    # 'ClearMap.Analysis.vasculature',
    # 'ClearMap.Analysis.vasculature.flow',
]

# Exclude all module in subpackages
# TODO: check if this is really necessary
exclude_subpackages = [
    ClearMap.custom_scripts,  # ClearMap.Tests
]
for package in exclude_subpackages:
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        if name.startswith('_'):
            continue
        if __debug__:
            print(f'Excluding:{package.__name__}.{name}')
        autosummary_mock_imports.append(f'{package.__name__}.{name}')

# Copy scripts to documentation
scripts_folder = Path(Settings.clearmap_path) / 'Scripts'
shutil.copytree(scripts_folder, doc_dir / 'scripts', dirs_exist_ok=True)

# debug - speed up compilation for testing
debug = False
if debug:
    autosummary_mock_imports.extend([
        'ClearMap.Analysis',
        # 'ClearMap.External',
        'ClearMap.IO',
        'ClearMap.ImageProcessing',
        'ClearMap.ParallelProcessing',
        'ClearMap.Utils',
        'ClearMap.Visualization',
        # 'ClearMap.Tests',
        'ClearMap.Resources',
    ])

# =============================================================================
# ============================ nbsphinx =======================================
# =============================================================================
nbsphinx_execute = 'never'

# =============================================================================
# ============================ Autodoc ========================================
# =============================================================================

autodoc_member_order = 'groupwise'  # 'bysource'

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    # 'imported-members': True,
    'show-inheritance': True,
    # 'inherited-members' : True
}

autosummary_generate = True
autosummary_imported_members = True

# =============================================================================
# ============================ Napoleon (numpydoc) ============================
# =============================================================================
napoleon_custom_sections = [
    "Arguments", "Returns", "References",
    "Note", "Examples",
    "Illumination correction", "Background removal",
    "Equalization", "DoG Filter",
    "Maxima Detection", "Shape detection",
    "Intensity detection", "General parameter",
    "Clipping", "Lightsheet correction",
    "Median filter", "Pseudo Deconvolution",
    "Adaptive Thresholding", "Equalization",
    "Tube filter", "Binary filling", "Binary smoothing",
    "Smoothing", "Filling"
]


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


# =============================================================================
# ============================ HTML ===========================================
# =============================================================================

html_sourcelink_suffix = ''

# use gif for html
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

html_css_files = [
    'css/custom.css',
]
carousel_bootstrap_add_css_js = False
carousel_bootstrap_prefix = ''

html_logo = str(Path(Settings.clearmap_path) / 'gui/creator/icons/logo.png')

html_theme_path = ['./themes']
# html_theme = 'ClearMap'
html_theme = 'pydata_sphinx_theme'

# pydata_social_buttons = {
#     {"title": "GitHub", "classes": "fab fa-github", "url": "https://github.com/ChristophKirst/ClearMap2"},
#     # {"title": "X", "classes": "fab square-x-twitter", "url": "https://twitter.com/clearmap_idisco"},
#     {"title": "X", "classes": "fab fa-square-x-twitter", "url": "https://twitter.com/clearmap_idisco"},
# }

html_theme_options = {
    'body_max_width': 'auto',
    'github_url': 'https://github.com/ChristophKirst/ClearMap2',
    # 'twitter_url': 'https://twitter.com/clearmap_idisco',
    'icon_links': [
        # {'name': 'ClearMap', 'url': 'https://idisco.info', 'icon': html_logo},
        {'name': 'X',
         'url': 'https://twitter.com/clearmap_idisco',
         'icon': 'fab fa-square-x-twitter',
         'type': 'fontawesome'},
    ],
    "show_nav_level": 2,
    'logo': {
        'text': f'ClearMap {version}',
        'image_light': html_logo,
        'image_dark': html_logo,
    }
}

html_static_path = ['static']
banner_images = ['_static/ClearMap_banner.jpg', '_static/ClearMap_banner_brain_bw.jpg', '_static/TubeMap_raw.png']

# html_sidebars = {'**': ['sidebar.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }
# html_additional_pages = {'home': 'home.html'}
htmlhelp_basename = 'ClearMapDoc'


html_use_index = True
html_split_index = False
html_show_sourcelink = True
html_show_copyright = True
html_show_sphinx = False

# =============================================================================
# =============================== LATEX =======================================
# =============================================================================

latex_elements = {
    # 'papersize': 'letterpaper',  # The paper size ('letterpaper' or 'a4paper').
    # 'pointsize': '10pt',      # The font size ('10pt', '11pt' or '12pt').
    # 'preamble': '',      # Additional stuff for the LaTeX preamble.
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'clearmap.tex', u'ClearMap Documentation', u'Christoph Kirst', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# =============================================================================
# ============================ MAN PAGES ======================================
# =============================================================================

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'clearmap', u'ClearMap Documentation',
     [u'Christoph Kirst'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# =============================================================================
# ============================ TEXINFO ========================================
# =============================================================================

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'ClearMap', u'ClearMap Documentation',
   u'Christoph Kirst', 'ClearMap', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# =============================================================================
# ============================== Monkey patching ==============================
# =============================================================================
# Comes after the configuration because the correct paths are used in the config
# mocked_clearmap_path = '/home/clearmap_user/ClearMap2'
# ClearMap.Settings.clearmap_path = mocked_clearmap_path
# ClearMap.Settings.resources_path = os.path.join(mocked_clearmap_path, 'Resources')
# ClearMap.Settings.atlas_folder = os.path.join(ClearMap.Settings.resources_path, 'Atlas')
# ClearMap.Settings.external_path = os.path.join(mocked_clearmap_path, 'External')
# ClearMap.Settings.test_path = os.path.join(mocked_clearmap_path, 'Tests')
# ClearMap.Settings.test_data_path = os.path.join(ClearMap.Settings.test_path, 'Data')
#
# ClearMap.Settings.elastix_path = os.path.join(ClearMap.Settings.external_path, 'elastix', 'build')
