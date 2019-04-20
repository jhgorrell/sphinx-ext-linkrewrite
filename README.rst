sphinx-ext-linkrewrite README
==================================================

A way to rewrite links from one location to another.

When the top level README is rendered by github or
bitbucket, the links in that document are relative to the
project.  However when that document is used by Sphinx, the
links wont point to the correct spot.

When github/bitbucket renders a rst document, it only
applies markup to the simple links.  So the toplevel links
need to be simple ones.

With this extention, Sphinx is capable of transforming the
links, so the document links will work in the s


Links
----------------------------------------

- https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
- https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/extlinks.py
