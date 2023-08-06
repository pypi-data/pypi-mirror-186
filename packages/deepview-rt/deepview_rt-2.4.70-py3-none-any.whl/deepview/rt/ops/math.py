# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from __future__ import division

import numpy

from typing import List, Optional
from ..common import ffi, lib
from ..tensor import Tensor, auto_tensor
from ..errors import Error, InvalidShapeError
from .activation import Activation


@auto_tensor
def add(a,          # Tensor
        b,          # Tensor
        out=None    # type: Optional[Tensor]
        ):
    # type: (...) -> Tensor
    """
    Add two tensors together, storing the results into the out tensor.  If
    out is None it will be created with the expected shape of the output.
    In either case the resulting out tensor is returned.

    Args:
        a (Tensor): The left-hand tensor.
        b (Tensor): The right-hand tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        if a.shape == b.shape:
            out = Tensor(shape=a.shape, engine=a.engine)
        else:
            na = a.map()
            nb = b.map()
            out = Tensor(shape=numpy.broadcast(na, nb).shape, engine=a.engine)
            a.unmap()
            b.unmap()
    err = lib.nn_add(out.ptr, a.ptr, b.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def subtract(a,          # Tensor
             b,          # Tensor
             out=None    # type: Optional[Tensor]
             ):
    # type: (...) -> Tensor
    """
    Subtract the b tensor from the a tensor, storing the results into the out
    tensor. If out is None it will be created with the expected shape of the
    output. In either case the resulting out tensor is returned.

    Args:
        a (Tensor): The left-hand tensor.
        b (Tensor): The right-hand tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        if a.shape == b.shape:
            out = Tensor(shape=a.shape, engine=a.engine)
        else:
            na = a.map()
            nb = b.map()
            out = Tensor(shape=numpy.broadcast(na, nb).shape, engine=a.engine)
            a.unmap()
            b.unmap()
    err = lib.nn_subtract(out.ptr, a.ptr, b.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def multiply(a,          # Tensor
             b,          # Tensor
             out=None    # type: Optional[Tensor]
             ):
    # type: (...) -> Tensor
    """
    Multiply the a and b tensors, storing the results into the out tensor.
    If out is None it will be created with the expected shape of the output.
    In either case the resulting out tensor is returned.

    Args:
        a (Tensor): The left-hand tensor.
        b (Tensor): The right-hand tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        if a.shape == b.shape:
            out = Tensor(shape=a.shape, engine=a.engine)
        else:
            na = a.map()
            nb = b.map()
            out = Tensor(shape=numpy.broadcast(na, nb).shape, engine=a.engine)
            a.unmap()
            b.unmap()
    err = lib.nn_multiply(out.ptr, a.ptr, b.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def divide(a,          # Tensor
           b,          # Tensor
           out=None    # type: Optional[Tensor]
           ):
    # type: (...) -> Tensor
    """
    .. math::
        c = \\frac { a } { b }

    Divide the a tensor by the b tensor, storing the results into the out
    tensor. If out is None it will be created with the expected shape of the
    output. In either case the resulting out tensor is returned.

    Args:
        a (Tensor): The left-hand tensor.
        b (Tensor): The right-hand tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        if a.shape == b.shape:
            out = Tensor(shape=a.shape, engine=a.engine)
        else:
            na = a.map()
            nb = b.map()
            out = Tensor(shape=numpy.broadcast(na, nb).shape, engine=a.engine)
            a.unmap()
            b.unmap()
    err = lib.nn_divide(out.ptr, a.ptr, b.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def abs(x,          # type: Tensor
        out=None    # type: Optional[Tensor]
        ):
    # type: (...) -> Tensor
    """
    .. math::
        out = |x|

    Calculate the absolute value of each element of the tensor.

    Args:
        x (Tensor): The input tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        out = Tensor(shape=x.shape, engine=x.engine)
    err = lib.nn_abs(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def sqrt(x,          # type: Tensor
         out=None    # type: Optional[Tensor]
         ):
    # type: (...) -> Tensor
    """
    .. math::
        out = sqrt(x)

    Calculate the square root of each element of the tensor.

    Args:
        x (Tensor): The input tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        out = Tensor(shape=x.shape, engine=x.engine)
    err = lib.nn_sqrt(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def exp(x,          # type: Tensor
        out=None    # type: Optional[Tensor]
        ):
    # type: (...) -> Tensor
    """
    .. math::
        out = sqrt(x)

    Calculate the square root of each element of the tensor.

    Args:
        x (Tensor): The input tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        out = Tensor(shape=x.shape, engine=x.engine)
    err = lib.nn_exp(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def log(x,          # type: Tensor
        out=None    # type: Optional[Tensor]
        ):
    # type: (...) -> Tensor
    """
    .. math::
        out = sqrt(x)

    Calculate the square root of each element of the tensor.

    Args:
        x (Tensor): The input tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if out is None:
        out = Tensor(shape=x.shape, engine=x.engine)
    err = lib.nn_log(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def matmul(a,                   # Tensor
           b,                   # Tensor
           transpose_a=False,   # type: bool
           transpose_b=False,   # type: bool
           out=None             # type: Optional[Tensor]
           ):
    # type: (...) -> Tensor
    """
    .. math::
        out = matmul(a,b)

    Calculate the matrix multiplication of A and B.

    Args:
        a (Tensor): The A tensor.
        b (Tensor): The B tensor.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if len(a.shape) != 2:
        raise InvalidShapeError('matmul requires rank-2 tensors, ' +
                                'but a has shape %s' % a.shape)
    if len(b.shape) != 2:
        raise InvalidShapeError('matmul requires rank-2 tensors, ' +
                                'but b has shape %s' % b.shape)
    if out is None:
        c_rows = a.shape[1] if transpose_a else a.shape[0]
        c_cols = b.shape[0] if transpose_b else b.shape[1]
        out = Tensor(shape=(c_rows, c_cols), engine=a.engine)
    err = lib.nn_matmul(out.ptr, a.ptr, b.ptr, transpose_a, transpose_b)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def dense(x,                                # type: Tensor
          w,                                # type: Tensor
          b=None,                           # type: Optional[Tensor]
          activation=Activation.Linear,     # type: Activation
          out=None                          # type: Optional[Tensor]
          ):
    # type: (...) -> Tensor
    """
    .. math::
        out = dense(x, w, b)

    Calculate the matrix multiplication of x and w plus bias b.

    Args:
        x (Tensor): The A tensor.
        w (Tensor): The B tensor, transposed.
        b (Optional[Tensor]): The optional bias.
        activation (Optional[Activation]): The optional activation function.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if len(x.shape) != 2:
        raise InvalidShapeError('linear requires rank-2 tensors, ' +
                                'but x has shape %s' % x.shape)
    if len(w.shape) != 2:
        raise InvalidShapeError('linear requires rank-2 tensors, ' +
                                'but w has shape %s' % w.shape)
    if out is None:
        out = Tensor(shape=(x.shape[0], w.shape[1]), engine=x.engine)
    b_ptr = b.ptr if b is not None else ffi.NULL
    err = lib.nn_dense(out.ptr, x.ptr, w.ptr, b_ptr, activation.value)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def linear(x,                               # type: Tensor
           w,                               # type: Tensor
           b=None,                          # type: Optional[Tensor]
           activation=Activation.Linear,    # type: Activation
           out=None                         # type: Optional[Tensor]
           ):
    # type: (...) -> Tensor
    """
    .. math::
        out = linear(x, w, b)

    Calculate the matrix multiplication of x and wT (transposed) plus bias b.

    Args:
        x (Tensor): The A tensor.
        w (Tensor): The B tensor, transposed.
        b (Optional[Tensor]): The optional bias.
        activation (Optional[Activation]): The optional activation function.
        out (Optional[Tensor]):
            Optional result tensor, if not provided it will be created.

    Returns:
        Tensor: The out tensor holding the results of the operation.

    Raises:
        Error: if an error happened.
    """
    if len(x.shape) != 2:
        raise InvalidShapeError('linear requires rank-2 tensors, ' +
                                'but x has shape %s' % x.shape)
    if len(w.shape) != 2:
        raise InvalidShapeError('linear requires rank-2 tensors, ' +
                                'but w has shape %s' % w.shape)
    if out is None:
        out = Tensor(shape=(x.shape[0], w.shape[0]), engine=x.engine)
    b_ptr = b.ptr if b is not None else ffi.NULL
    err = lib.nn_linear(out.ptr, x.ptr, w.ptr, b_ptr, activation.value)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out
