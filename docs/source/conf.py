# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Database 4 Everything'
copyright = '2024, Nadim-Daniel Ghaznavi'
author = 'Nadim-Daniel Ghaznavi'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.append('..')
sys.path.append('../assets')
sys.path.append('../assets/py')
sys.path.append('../assets/py/Infrastructure')
sys.path.append('../assets/py/Reports')
sys.path.append('../assets/py/Mining')

extensions = [
  'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
