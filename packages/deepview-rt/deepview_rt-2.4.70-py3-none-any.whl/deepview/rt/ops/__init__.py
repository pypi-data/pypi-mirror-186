# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

"""
The pattern to all functions is to return the output tensor and optionally
accept the output tensor as parameter "out", when this parameter is not
provided it will be created with the appropriate setup (shape, datatype, and
engine).  Since the function will return the out parameter regardless it can be
used for lazy initialization as in the following example, here the c tensor is
created by the add() function and reused by the subtract() function.

Example:

.. code-block:: python
    c = None
    a = deepview.rt.Tensor(numpy.random.rand(1))
    b = deepview.rt.Tensor(numpy.random.rand(1))
    c = deepview.rt.ops.add(a, b, c)
    c = deepview.rt.ops.subtract(a, b, c)

In cases where we wish to experiment with custom graphs without using RTM
models they could be represented, for example, using the networkx module by
having vertices representing the ops and edges representing the tensors.  In
this case the out tensors would be the edge leaving a vertex which would then
be reused by the vertex on the other side of the edge as an input.
"""

from .activation import *
from .array import *
from .conv import conv
from .math import *
from .pool import *
