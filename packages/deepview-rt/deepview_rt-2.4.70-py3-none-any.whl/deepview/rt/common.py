# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

import numpy

from .librt import lib, ffi


def version():
    # type: () -> str
    """
    Queries the version information from the underlying deepview-rt library.

    Returns:
        str: Library version string
    """
    return ffi.string(lib.nn_version()).decode('utf-8')


def strerror(err):
    # type: (int) -> str
    """
    Queries the human readable string for the error code.

    Args:
        err (int): The native (C ABI) NNError code.

    Returns:
        str: Error code as human readable string
    """
    s = lib.nn_strerror(err)
    if s != ffi.NULL:
        return ffi.string(s).decode('utf-8')
    return None


def init():
    return lib.nn_init(ffi.NULL)


def nativetype(dtype):
    # type: (numpy.dtype) -> int
    """
    Converts the Numpy type definition to the deepview-rt NNTensorType enum.
    This function will convert known mappings between Numpy and DeepViewRT but
    even if a mapping is known usage may still fail with
    TensorTypeUnsupportedError if the actual operation does not support this
    type.

    Note:
        Currently DeepViewRT ONLY supports numpy.float32.

    Returns:
        int: Native (C ABI) NNTensorType matching the Numpy datatype.

    Raises:
        TensorTypeUnsupportedError: If the Numpy datatype is not supported.
    """
    typemap = {
        numpy.int8: lib.NNTensorType_I8,
        numpy.uint8: lib.NNTensorType_U8,
        numpy.int16: lib.NNTensorType_I16,
        numpy.uint16: lib.NNTensorType_U16,
        numpy.int32: lib.NNTensorType_I32,
        numpy.uint32: lib.NNTensorType_U32,
        numpy.int64: lib.NNTensorType_I64,
        numpy.uint64: lib.NNTensorType_U64,
        numpy.float32: lib.NNTensorType_F32,
        numpy.float64: lib.NNTensorType_F64,
    }
    if dtype not in typemap:
        raise ValueError('unsupported type:', dtype)
    return typemap[dtype]


def numpytype(ntype):
    # type: (int) -> numpy.dtype
    typemap = {
        lib.NNTensorType_I8: numpy.int8,
        lib.NNTensorType_U8: numpy.uint8,
        lib.NNTensorType_I16: numpy.int16,
        lib.NNTensorType_U16: numpy.uint16,
        lib.NNTensorType_I32: numpy.int32,
        lib.NNTensorType_U32: numpy.uint32,
        lib.NNTensorType_I64: numpy.int64,
        lib.NNTensorType_U64: numpy.uint64,
        lib.NNTensorType_F32: numpy.float32,
        lib.NNTensorType_F64: numpy.float64,
    }

    if ntype not in typemap:
        raise ValueError('unsupported type:', ntype)
    return typemap[ntype]
