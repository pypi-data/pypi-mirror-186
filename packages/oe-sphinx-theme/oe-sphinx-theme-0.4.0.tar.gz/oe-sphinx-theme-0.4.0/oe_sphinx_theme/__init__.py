import os


__version__ = '0.4.0'


def get_theme_dir():
    """
    Returns path to directory containing this package's theme.

    This is designed to be used when setting the ``html_theme_path``
    option within Sphinx's ``conf.py`` file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "theme"))


def default_sidebars():
    """
    Returns a dictionary mapping for the templates used to render the
    sidebar on the index page and sub-pages.
    """
    return {
        'genindex': ['searchbox.html', 'globaltoc.html',],
        'modindex': ['searchbox.html', 'globaltoc.html',],
        'search': ['globaltoc.html',],
        '**': ['searchbox.html', 'globaltoc.html', 'relations.html']
    }
