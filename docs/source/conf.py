# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jubilee'
copyright = "2024, Sonya Vasquez"
author = "Sonya Vasquez"
#release = "3.0.0" # appears in navbar-logo if specified.

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",  # enable numpy and google style docstring parsing.
    "sphinx.ext.autodoc",  # enable doc generation from code docstrings.
    "sphinx_design",
    "sphinxcontrib.pdfembed", # from https://github.com/SuperKogito/sphinxcontrib-pdfembed
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']


html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "header_links_before_dropdown": 6,
    "show_prev_next": False,
    "external_links":
    [
        {
            "url": "https://github.com/jubilee3d",
            "name": "Source Files",
        },
    ],
    "show_nav_level": 0,  # collapse sidebar to caption.
    "collapse_navigation": True,
    "secondary_sidebar_items": [],  # Remove secondary sidebar.
    "footer_start": ["copyright"], # "sphinx-version"],
    "footer_end": ["edit-this-page"],
    "use_edit_page_button": True,  # Must be true for "edit-this-page" to work.
}

html_sidebars = {
    "machines/machines": [],  # No displayed sidebar for this page
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"],
}

# For edit-this-page context.
html_context = {
    "github_url": "https://github.com",
    "github_user": "jubilee3d",
    "github_repo": "jubilee3d.github.io",
    "github_version": "develop",
    "doc_path": "docs",
}
