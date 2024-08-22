"""Sphinx configuration."""
project = "Quant_Data"
author = "Yan Zhang"
copyright = "2024, Yan Zhang"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
