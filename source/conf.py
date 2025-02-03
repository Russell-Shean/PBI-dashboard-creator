
import os
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PBI_dashboard_creator'
copyright = '2025, Russell Shean'
author = 'Russell Shean'
release = '1.0.65'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

#Set the canonical URL

#A canonical URL allows you to specify the preferred version of a web page to prevent duplicated content.
# Set your html_baseurl to your Read the Docs canonical URL using a Read the Docs environment variable:
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

# this is needed too?
extensions = ["myst_parser"]