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
    "machines/machines": [],  # No sidebar for this page
#    "machines/jubilee_3/jubilee3": ['page-toc'],
#    "faqs": ['page-toc'],  # No sidebar for this page
    "machines/jubilee_3/jubilee3": ['sidebar-nav-bs'],
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"],
}

print(html_sidebars["machines/jubilee_3/jubilee3"])

# For edit-this-page context.
html_context = {
    "github_url": "https://github.com",
    "github_user": "jubilee3d",
    "github_repo": "jubilee3d.github.io",
    "github_version": "develop",
    "doc_path": "docs",
}