# Configuration file for the Sphinx documentation builder.
#
# For a full list of sphinx builder options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('../..'))
di = os.path.abspath(os.pardir)
remove_docs = di.strip('docs')

for r,d,f in os.walk(r"{}credsweeper".format(remove_docs)):
    sys.path.append(r)

# -- Project information -----------------------------------------------------

project = 'CredSweeper'
copyright = '2021, Samsung CredTeam'
author = 'CredTeam'

from credsweeper import __version__ as credsweeper_version

# The short X.Y version
version = '.'.join(credsweeper_version.split('.')[0:2])

# The full version, including alpha/beta/rc tags
release = credsweeper_version

# The master toctree document.
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
    'm2r2',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'navigation_depth': 3
}

# The name of an image file (relative to this directory) to place at the top of the sidebar.
html_logo = 'https://raw.githubusercontent.com/Samsung/CredSweeper/main/docs/images/Logo.png'

html_scaled_image_link = False
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ci_doc'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ci', u'CI Documentation',
     [author], 1)
]

sys.path.append(os.path.dirname(__file__)+'/..')
