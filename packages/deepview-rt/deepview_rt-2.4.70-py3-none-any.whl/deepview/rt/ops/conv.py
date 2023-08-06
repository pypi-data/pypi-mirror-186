# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from __future__ import division

import numpy

from typing import List, Optional, Tuple
from ..common import ffi, lib
from ..tensor import Tensor, auto_tensor
from ..errors import Error, InvalidShapeError
from .activation import Activation


@auto_tensor
def conv(x,                             # type: Tensor
         k,                             # type: Tensor
         bias=None,                     # type: Optional[Tensor]
         activation=Activation.Linear,  # type: Activation
         cache=None,                    # type: Optional[Tensor]
         groups=1,                      # type: int
         strides=(1, 1, 1, 1),          # type: Tuple[int,int,int,int]
         padding='VALID',               # type: string
         dilation=(1, 1, 1, 1),         # type: Tuple[int, int, int, int]
         out=None                       # type: Optional[Tensor]
         ):
    # type: (...) -> Tensor
    """
    conv

    Args:
        inp (Tensor): The input tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    paddings = numpy.zeros(8, dtype=numpy.int32)
    padded = numpy.zeros(4, dtype=numpy.int32)
    window = (1, k.shape[0], k.shape[1], 1)

    err = lib.nn_tensor_padding(x.ptr,
                                padding.encode(),
                                window,
                                strides,                                
                                dilation,
                                ffi.cast('int32_t*', ffi.from_buffer(padded)),
                                ffi.cast('int32_t*', ffi.from_buffer(paddings)))
    if err != lib.NN_SUCCESS:
        raise Error(err)

    if groups == 0:
        assert k.shape[3] == 1, 'Only depthwise convolutions are supported for groups == 0'
        padded[3] = k.shape[2]
    if groups == 1:
        padded[3] = k.shape[3]
    else:
        assert k.shape[2] == groups, 'Invalid group size %d for filter %s' % (groups, k)
        assert k.shape[3] == 1, 'Only depthwise convolutions are supported for groups > 1'
        padded[3] = k.shape[2] * k.shape[3]

    if out is None:
        out = Tensor(shape=padded, engine=x.engine)
    else:
        out.reshape(padded)

    err = lib.nn_conv_ex(out.ptr,
                         cache.ptr if cache is not None else ffi.NULL,
                         x.ptr,
                         k.ptr,
                         bias.ptr if bias is not None else ffi.NULL,                         
                         strides,
                         ffi.cast('int32_t*', ffi.from_buffer(paddings)),
                         dilation,
                         groups,
                         activation.value)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out
