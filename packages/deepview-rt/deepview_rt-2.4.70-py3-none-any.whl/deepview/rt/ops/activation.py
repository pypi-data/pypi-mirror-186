# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from __future__ import division

import numpy

from enum import Enum
from ..common import ffi, lib
from ..tensor import Tensor, auto_tensor
from ..errors import Error
from typing import Optional


class Activation(Enum):
    Linear = lib.NNActivation_Linear
    Sigmoid = lib.NNActivation_Sigmoid
    Tanh = lib.NNActivation_Tanh
    ReLU = lib.NNActivation_ReLU
    ReLU6 = lib.NNActivation_ReLU6


@auto_tensor
def sigmoid(x,          # type: Tensor
            out=None    # type: Optional[Tensor]
            ):
    # type: (...) -> Tensor
    """
    .. math::
        out = \\frac { 1 } { 1 + e^-x }

    Calculate the sigmoid of each element of the tensor.

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
    err = lib.nn_sigmoid(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def sigmoid_fast(x,          # type: Tensor
                 out=None    # type: Optional[Tensor]
                 ):
    # type: (...) -> Tensor
    """
    .. math::
        out = \\frac { 1 } { 1 + |x| }

    Calculate the approximate sigmoid of each element of the tensor.

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
    err = lib.nn_sigmoid_fast(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def tanh(x,          # type: Tensor
         out=None    # type: Optional[Tensor]
         ):
    # type: (...) -> Tensor
    """
    .. math::
        out = tanh(x)

    Calculate the tanh of each element of the tensor.

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
    err = lib.nn_tanh(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def relu(x,          # type: Tensor
         out=None    # type: Optional[Tensor]
         ):
    # type: (...) -> Tensor
    """
    .. math::
        out = max(0, x)

    Calculate the relu of each element of the tensor.

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
    err = lib.nn_relu(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def relu6(x,            # type: Tensor
          out=None      # type: Optional[Tensor]
          ):
    # type: (...) -> Tensor
    """
    .. math::
        out = min(max(0, x), 6)

    Calculate the relu6 of each element of the tensor.

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
    err = lib.nn_relu6(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out


@auto_tensor
def softmax(x,          # type: Tensor
            out=None    # type: Optional[Tensor]
            ):
    # type: (...) -> Tensor
    """
    .. math::
        out = softmax(x)

    Calculate the softmax of the tensor.

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
    err = lib.nn_softmax(out.ptr, x.ptr)
    if err != lib.NN_SUCCESS:
        raise Error(err)
    return out
