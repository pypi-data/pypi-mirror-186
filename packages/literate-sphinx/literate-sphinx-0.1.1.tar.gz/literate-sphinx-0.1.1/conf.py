# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Literate Sphinx'
copyright = '2023, Hubert Chathi'
author = 'Hubert Chathi'
release = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
print(sys.path)

extensions = [
    'literate_sphinx',
    'myst_parser',
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', 'licenses' ]

myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = []

html_theme_options = {
    'description': 'A literate programming extension for Sphinx',
    'extra_nav_links': {
        'Source': 'https://gitlab.com/uhoreg/literate-sphinx'
    }
}
