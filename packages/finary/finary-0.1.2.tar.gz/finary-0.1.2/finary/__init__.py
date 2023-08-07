"""
finary
=====

Provides
  1. Excel tools
  2. Actuary tools (work in progress)
  3. ALM model (work in progress)

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://mclavier.com>`_.


The docstring examples assume that `numpy` has been imported as ``np``::

  >>> import finary as fa

Code snippets are indicated by three greater-than signs::

  >>> x = 42
  >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring::

  >>> help(np.sort)
  ... # doctest: +SKIP


Available subpackages
---------------------
matha
    Basic functions used by several sub-packages.
excel
    Core Random Tools
"""


__version__ = "1.0.0"
__author__ = "Mathieu Clavier"


# import modules that should be available when the package is imported
import finary.excel 
import finary.matha
