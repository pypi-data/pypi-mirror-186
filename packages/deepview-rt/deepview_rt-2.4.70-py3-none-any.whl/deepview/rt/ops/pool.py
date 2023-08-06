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


@auto_tensor
def avgpool(x,                      # type: Tensor
            window,                 # type: Tuple[int, int, int, int]
            strides=(1, 1, 1, 1),   # type: Tuple[int, int, int, int]
            padding='VALID',        # type: string
            dilation=(1, 1, 1, 1),  # type: Tuple[int, int, int, int]
            out=None                # type: Optional[Tensor]
            ):
    # type: (...) -> Tensor
    """
    avgpool
    """
    paddings = numpy.zeros(8, dtype=numpy.int32)
    padded = numpy.zeros(4, dtype=numpy.int32)

    err = lib.nn_tensor_padding(x.ptr,                                
                                padding.encode(),
                                window,
                                strides,                                                                
                                dilation,
                                ffi.cast('int32_t*', ffi.from_buffer(padded)),
                                ffi.cast('int32_t*', ffi.from_buffer(paddings)))
    if err != lib.NN_SUCCESS:
        raise Error(err)

    if out is None:
        out = Tensor(shape=padded, engine=x.engine)
    else:
        out.reshape(padded)

    err = lib.nn_avgpool_ex(out.ptr,
                            x.ptr,
                            window,
                            strides,
                            ffi.cast('int32_t*', ffi.from_buffer(paddings)),
                            dilation)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def maxpool(x,                      # type: Tensor
            window,                 # type: Tuple[int, int, int, int]
            strides=(1, 1, 1, 1),   # type: Tuple[int, int, int, int]
            padding='VALID',        # type: string
            dilation=(1, 1, 1, 1),  # type: Tuple[int, int, int, int]
            out=None                # type: Optional[Tensor]
            ):
    # type: (...) -> Tensor
    """
    maxpool
    """
    paddings = numpy.zeros(8, dtype=numpy.int32)
    padded = numpy.zeros(4, dtype=numpy.int32)

    err = lib.nn_tensor_padding(x.ptr,           
                                padding.encode(),     
                                window,
                                strides,                                                           
                                dilation,
                                ffi.cast('int32_t*', ffi.from_buffer(padded)),
                                ffi.cast('int32_t*', ffi.from_buffer(paddings)))
    if err != lib.NN_SUCCESS:
        raise Error(err)

    if out is None:
        out = Tensor(shape=padded, engine=x.engine)
    else:
        out.reshape(padded)

    err = lib.nn_maxpool_ex(out.ptr,
                            x.ptr,
                            window,
                            strides,
                            ffi.cast('int32_t*', ffi.from_buffer(paddings)),
                            dilation)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def reduce_sum(x,                   # type: Tensor
               axes=None,           # type: Optional[Tuple[int, ...]]
               keepdims=False,      # type: bool
               out=None             # type: Optional[Tensor]
               ):
    # type: (...) -> Tensor
    """
    reduce_sum
    """
    if out is None:
        raise ValueError('out parameter is currently required')
    n_axes = len(axes) if axes is not None else 0
    axes_ = axes if axes is not None else ffi.NULL
    err = lib.nn_reduce_sum(out.ptr, x.ptr, n_axes, axes_, keepdims)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def reduce_max(x,                   # type: Tensor
               axes=None,           # type: Optional[Tuple[int, ...]]
               keepdims=False,      # type: bool
               out=None             # type: Optional[Tensor]
               ):
    # type: (...) -> Tensor
    """
    reduce_max
    """
    if out is None:
        raise ValueError('out parameter is currently required')
    n_axes = len(axes) if axes is not None else 0
    axes_ = axes if axes is not None else ffi.NULL
    err = lib.nn_reduce_max(out.ptr, x.ptr, n_axes, axes_, keepdims)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def reduce_min(x,                   # type: Tensor
               axes=None,           # type: Optional[Tuple[int, ...]]
               keepdims=False,      # type: bool
               out=None             # type: Optional[Tensor]
               ):
    # type: (...) -> Tensor
    """
    reduce_max
    """
    if out is None:
        raise ValueError('out parameter is currently required')
    n_axes = len(axes) if axes is not None else 0
    axes_ = axes if axes is not None else ffi.NULL
    err = lib.nn_reduce_min(out.ptr, x.ptr, n_axes, axes_, keepdims)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def reduce_mean(x,                   # type: Tensor
                axes=None,           # type: Optional[Tuple[int, ...]]
                keepdims=False,      # type: bool
                out=None             # type: Optional[Tensor]
                ):
    # type: (...) -> Tensor
    """
    reduce_mean
    """
    if out is None:
        raise ValueError('out parameter is currently required')
    n_axes = len(axes) if axes is not None else 0
    axes_ = axes if axes is not None else ffi.NULL
    err = lib.nn_reduce_mean(out.ptr, x.ptr, n_axes, axes_, keepdims)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def reduce_product(x,                   # type: Tensor
                   axes=None,           # type: Optional[Tuple[int, ...]]
                   keepdims=False,      # type: bool
                   out=None             # type: Optional[Tensor]
                   ):
    # type: (...) -> Tensor
    """
    reduce_product
    """
    if out is None:
        raise ValueError('out parameter is currently required')
    n_axes = len(axes) if axes is not None else 0
    axes_ = axes if axes is not None else ffi.NULL
    err = lib.nn_reduce_product(out.ptr, x.ptr, n_axes, axes_, keepdims)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out
