# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jubilee'
copyright = "2024, Sonya Vasquez"
author = "Sonya Vasquez"
release = "3.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",  # enable numpy and google style docstring parsing.
    "sphinx.ext.autodoc",  # enable doc generation from code docstrings.
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']



html_theme_options = {
    "navbar_center": ["navbar-nav"],
    "show_prev_next": False,
    "external_links":
    [
        {
            "url": "https://github.com/jubilee3d",
            "name": "Source Files",
        },
    ],
    "show_nav_level": 0, # collapse sidebar to caption.
    "collapse_navigation": True,
}

#html_sidebars = {'**': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
#html_sidebars = {
#   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
#   'using/windows': ['windowssidebar.html', 'searchbox.html'],
#}
html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"]
}



# Sphinx Options.

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False
