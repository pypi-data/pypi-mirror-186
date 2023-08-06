# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

import numpy

from ..common import ffi, lib
from ..tensor import Tensor, auto_tensor
from ..errors import Error, InvalidShapeError
from typing import List, Optional


@auto_tensor
def concat(inputs, axis, out=None):
    # type: (List[Tensor], int, Optional[Tensor]) -> Tensor
    """
    Concatenate the tensors from list into a single tensor along the axis.

    Returns:
        Tensor: the concatenated tensor.
    """
    inputs = [Tensor(x)
              if isinstance(x, numpy.ndarray)
              else x for x in inputs]

    if out is None:
        out_shape = list(inputs[0].shape)
        for i in range(1, len(inputs)):
            out_shape[axis] += inputs[i].shape[axis]
        out = Tensor(shape=tuple(out_shape), engine=inputs[0].engine)

    rank = len(inputs[0].shape)
    prepend = 4-rank
    if prepend > 0:
        out.reshape(tuple([1]*prepend + list(out.shape)))
        for node in inputs:
            node.reshape(tuple([1]*prepend + list(node.shape)))
    elif prepend < 0:
        raise ValueError("Tensors have rank greater than 4")

    inputs_ptr = tuple([i.ptr for i in inputs])

    err = lib.nn_tensor_concat(out.ptr, len(inputs), inputs_ptr, axis+prepend)
    if err != lib.NN_SUCCESS:
        raise Error(err)

    out.reshape(out.shape[prepend:])

    for node in inputs:
        node.reshape(node.shape[prepend:])
    return out
