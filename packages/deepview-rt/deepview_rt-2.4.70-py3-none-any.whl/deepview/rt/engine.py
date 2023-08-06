# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from .librt import ffi, lib
from .errors import check_error


class Engine:
    """
    The Engine class provides the interface to loading DeepViewRT Engine
    plugins such as the OpenCL engine (deepview-rt-opencl.so).  It can then be
    used to initialize Tensors with this engine.
    """
    def __init__(self):
        self.mem = ffi.new('char[]', lib.nn_engine_sizeof())
        self.ptr = lib.nn_engine_init(self.mem)

    def __del__(self):
        lib.nn_engine_unload(self.ptr)
        lib.nn_engine_release(self.ptr)

    def load(self, plugin):
        err = lib.nn_engine_load(self.ptr, plugin.encode('ascii'))
        check_error(err)

    def unload(self):
        lib.nn_engine_unload(self.ptr)

    def name(self):
        name = lib.nn_engine_name(self.ptr)
        if name != ffi.NULL:
            return ffi.string(name).decode('utf-8')
        return None


class EngineContext:
    previous = None
    current = None

    def __init__(self, engine):
        EngineContext.previous = EngineContext.current
        EngineContext.current = engine

    def __enter__(self):
        pass

    def __exit__(self, *args, **kwargs):
        EngineContext.current = EngineContext.previous
