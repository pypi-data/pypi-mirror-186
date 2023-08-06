# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

import numpy as np

from collections.abc import Mapping
from pathlib import Path
from os.path import isfile
from .librt import ffi, lib
from .errors import check_error
from .tensor import Tensor


class Context:
    def __init__(self,
                 engine=None,
                 memory_size=0,
                 cache_size=int(4 * 1024 * 1024),
                 ):
        self.model = None
        self.memory_size = memory_size
        self.cache_size = cache_size
        self.engine = engine
        engine_ptr = engine.ptr if engine is not None else ffi.NULL
        self.ptr = lib.nn_context_init(engine_ptr,
                                       self.memory_size,
                                       ffi.NULL,
                                       self.cache_size,
                                       ffi.NULL)
        if self.ptr == ffi.NULL:
            raise RuntimeError('failed to create context')

    def __del__(self):
        lib.nn_context_release(self.ptr)

    def load(self, model):
        if isinstance(model, bytes) or isinstance(model, bytearray):
            self.load_model(model)
        elif isinstance(model, Path) or isfile(model):
            with open(model, 'rb') as f:
                self.load_model(bytearray(f.read()))
        else:
            raise ValueError('Unable to load unknown model')

    def load_model(self, model):
        model = ffi.from_buffer(model)
        err = lib.nn_model_validate(model, len(model))
        if err != 0:
            msg = lib.nn_model_validate_error(err)
            raise RuntimeError('invalid RTMx model: %s' %
                               ffi.string(msg).decode('utf-8'))
        err = lib.nn_context_model_load(self.ptr, len(model), model)
        check_error(err)
        self.model = model

    def unload(self):
        lib.nn_context_model_unload(self.ptr)
        self.model = None

    @property
    def is_loaded(self):
        return self.model is not None

    @property
    def name(self):
        if self.is_loaded:
            name = lib.nn_model_name(self.model)
            if name != ffi.NULL:
                return ffi.string(name).decode('utf-8')
        return None

    def label_count(self):
        return lib.nn_model_label_count(self.model)

    def labels(self):
        return [ffi.string(lib.nn_model_label(self.model, i)).decode('utf-8')
                for i in range(self.label_count())]

    @property
    def inputs(self):
        if not self.is_loaded:
            return ()
        n_inputs = ffi.new('size_t[1]')
        ref_inputs = lib.nn_model_inputs(self.model, n_inputs)
        if ref_inputs != ffi.NULL:
            return tuple(
                [int(i) for i in ffi.cast('uint32_t[%d]' % n_inputs[0],
                                          ref_inputs)])
        return ()

    @property
    def outputs(self):
        if not self.is_loaded:
            return ()
        n_outputs = ffi.new('size_t[1]')
        ref_outputs = lib.nn_model_outputs(self.model, n_outputs)
        if ref_outputs != ffi.NULL:
            return tuple(
                [int(i) for i in ffi.cast('uint32_t[%d]' % n_outputs[0],
                                          ref_outputs)])
        return ()

    @property
    def layer_count(self):
        if self.is_loaded:
            return lib.nn_model_layer_count(self.model)
        return 0

    def layer_lookup(self, name):
        return lib.nn_model_layer_lookup(self.model, name.encode('utf-8'))

    def layer_name(self, index):
        if index < self.layer_count:
            name = lib.nn_model_layer_name(self.model, index)
            if name != ffi.NULL:
                return ffi.string(name).decode('utf-8')
        return None

    def layer_type(self, index):
        if index < self.layer_count:
            name = lib.nn_model_layer_type(self.model, index)
            if name != ffi.NULL:
                return ffi.string(name).decode('utf-8')
        return None

    def layer_shape(self, index):
        if index < self.layer_count:
            n_dims = ffi.new('size_t[1]')
            shape = lib.nn_model_layer_shape(self.model, index, n_dims)
            if shape != ffi.NULL:
                return tuple(
                    [int(i) for i in ffi.cast('int32_t[%d]' % n_dims[0],
                                              shape)])
        return tuple()

    def layer_axis(self, index):
        if index < self.layer_count:
            return lib.nn_model_layer_axis(self.model, index)
        return -1

    def layer_scales(self, index):
        if index < self.layer_count:
            n_scales = ffi.new('size_t[1]')
            scales = lib.nn_model_layer_scales(self.model, index, n_scales)
            if scales != ffi.NULL:
                return tuple(
                    [float(i) for i in ffi.cast('float[%d]' % n_scales[0],
                                                scales)])
        return tuple()

    def layer_zeros(self, index):
        if index < self.layer_count:
            n_zeros = ffi.new('size_t[1]')
            zeros = lib.nn_model_layer_zeros(self.model, index, n_zeros)
            if zeros != ffi.NULL:
                return tuple(
                    [int(i) for i in ffi.cast('int32_t[%d]' % n_zeros[0],
                                              zeros)])
        return tuple()

    def layers(self):
        return [
            {
                'name': self.layer_name(i),
                'type': self.layer_type(i),
                'shape': self.layer_shape(i)
            } for i in range(self.layer_count)]

    def input_names(self):
        return [tensor['name'] for tensor in filter(lambda x: x['type'] == 'input', self.layers())]

    def output_names(self):
        names_resource = lib.nn_model_resource(
            self.model, "outputs".encode('utf-8'))
        assert names_resource != ffi.NULL, "output names not found"
        names = lib.nn_model_resource_meta(names_resource)
        assert names != ffi.NULL, "output names not found"
        names = ffi.string(names).decode('utf-8')
        return names.split('\n')

    def tensor(self, name):
        if isinstance(name, int):
            ptr = lib.nn_context_tensor_index(self.ptr, name)
        else:
            ptr = lib.nn_context_tensor(self.ptr, name.encode('utf-8'))
        if ptr != ffi.NULL:
            return Tensor(wrap=ptr)
        return None

    def run(self, inputs=None):
        if isinstance(inputs, Mapping):
            for key, item in inputs.items():
                t = self.tensor(key)
                if t is None:
                    raise ValueError('input %s is not in model' % key)
                if isinstance(item, (np.ndarray, Tensor)):
                    t.copy_from(item)
                else:
                    raise ValueError('unsupported type in inputs map for '
                                     'item %s: %s' % (key, type(item)))
        elif isinstance(inputs, (np.ndarray, Tensor)):
            for i in range(self.layer_count):
                if self.layer_type(i) == 'input':
                    self.tensor(i).copy_from(inputs)

        err = lib.nn_context_run(self.ptr)
        check_error(err)

    def cache_tensor(self):
        return Tensor(wrap = lib.nn_context_cache(self.ptr))
