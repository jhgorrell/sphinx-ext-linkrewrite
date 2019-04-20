#
# sphinx-ext-linkrewrite/setup.py ---
#

from __future__ import (
    absolute_import,
)

import os
from distutils.core import (
    setup,
)

#####

setup(
    name="sphinx-ext-linkrewrite",
    version="0.0.1",
    description="FIXME",
    author="FIXME",
    url="FIXME",
    install_requires=[
        "sphinx",
    ],
    packages=[
        "sphinx-ext-linkrewrite",
    ],
    # where to find the src.
    package_dir={
        'sphinx-ext-linkrewrite': 'sphinx_ext_linkrewrite',
    },
)
