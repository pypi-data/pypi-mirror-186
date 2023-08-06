import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='oe-sphinx-theme',
    version=__import__('oe_sphinx_theme').__version__,
    author='OE Sphinx',
    author_email='klaas.millet@rwo.vlaanderen.be',
    packages=find_packages(),
    include_package_data=True,
    url='http://www.onroerenderfgoed.be/',
    license='BSD',
    description='OE sphinx theme',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    install_requires=('sphinx>=1.1', ),
    long_description=read_file('README.rst'),
    zip_safe=False,
)
