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
    description="Rewrite sphinx links.",
    author="HealthTell",
    url="https://bitbucket.org/healthtell/ht-sphinx/src/master/sphinx-ext-linkrewrite",
    install_requires=[
        "sphinx",
    ],
    packages=[
        "sphinx_ext_linkrewrite",
    ],
    # where to find the src.
    package_dir={
        'sphinx_ext_linkrewrite': 'sphinx_ext_linkrewrite',
    },
)
