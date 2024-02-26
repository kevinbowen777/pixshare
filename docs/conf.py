"""Sphinx configuration."""

project = "pixshare"
author = "Kevin Bowen"
copyright = f"2023, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "pixshare"
extensions = [
    "sphinx.ext.duration",
]
