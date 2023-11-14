# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'XAgent'
copyright = '2023, XAgent'
author = 'XAgent'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', '**/Gitlab-flow.md']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'


# 添加对Markdown的支持
extensions = [
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'myst_parser',
]

myst_parser = {
    "add_mathjax": True,
    "html_img_options": ["zoom"],
    "url_schemes": ("http", "https", "mailto"),
    "auto_toc_tree_section": "Contents",
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

raw_enabled = True