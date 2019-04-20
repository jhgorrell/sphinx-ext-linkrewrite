sphinx-ext-linkrewrite README
==================================================

.. image:: https://circleci.com/gh/jhgorrell/sphinx-ext-linkrewrite.svg?style=svg
   :target: https://circleci.com/gh/jhgorrell/sphinx-ext-linkrewrite

A way to rewrite sphinx links from one location to another.

When the top level README is rendered by a simple rst
processor (github or bitbucket) the links in that document
are relative to the project.  However, when that document is
used by Sphinx, the links wont point to the correct spot.

With this extention, Sphinx is capable of transforming the
links, so the simple links work and will work then processed.

Example:
--------------------------------------------------

This README links to 
`TARGET-DOC <./docs/source/TARGET-DOC.rst>`_.
When sphinx processes this file, the links will be changed
to link to the html docs.

::

    .. linkrewrite::
       :from: ./docs/source/(?P<path>.*)\.rst
       :to:   ./\g<path>.html


Install
--------------------------------------------------

To install from github:

::

    pip3 install git+https://github.com/jhgorrell/sphinx-ext-linkrewrite.git#egg=sphinx_ext_linkrewrite


Then, in your sphinx ``conf.py``:

::

    extentions.append('sphinx_ext_linkrewrite')


Quickstart
--------------------------------------------------

To get started as a dev:

::

    git clone https://github.com/jhgorrell/sphinx-ext-linkrewrite.git
    cd sphinx-ext-linkrewrite
    source ./setup.env
    make


Todo:
--------------------------------------------------

- Have ``linkrewrite`` conditinal on the output backend.


Links
----------------------------------------

- https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
- https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/extlinks.py
