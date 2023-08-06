OE Sphinx Theme
================

This is a custom `Sphinx <http://sphinx.pocoo.org/>`_ theme.


Installing
----------

This theme is available on PyPI so you can install it directly by this command::

    pip install oe-sphinx-theme

you can install from Github::

    pip install git+git://github.com/OnroerendErfgoed/oe-sphinx-theme

Once installed you should change your Sphinx ``conf.py`` to include::

    import oe_sphinx_theme
    html_theme = 'oe_sphinx'
    html_theme_path = [oe_sphinx_theme.get_theme_dir()]
