# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from __future__ import division

import numpy

from .librt import ffi, lib
from .common import nativetype, numpytype
from .errors import check_error
from .engine import Engine, EngineContext
from typing import Optional, Tuple, List
from functools import wraps


def auto_tensor(fn):
    @wraps(fn)
    def wrapped(*fn_args, **fn_kwargs):
        new_args = [Tensor(x)
                    if isinstance(x, numpy.ndarray)
                    else x for x in fn_args]
        new_kwargs = {k: Tensor(x)
                      if isinstance(x, numpy.ndarray)
                      else x for k, x in fn_kwargs.items()}
        return fn(*new_args, **new_kwargs)
    wrapped.__doc__ = fn.__doc__
    return wrapped


class Tensor:
    """
    Tensor objects are the primary means of holding data within DeepViewRT.
    All operations use data through tensor objects.

    Shapes are currently limited to a maximum of 4 dimensions, attempting to
    use more dimensions will raise an exception.
    """

    NNTensorType_RAW = lib.NNTensorType_RAW 
    NNTensorType_STR = lib.NNTensorType_STR 
    NNTensorType_I8 = lib.NNTensorType_I8 
    NNTensorType_U8 = lib.NNTensorType_U8 
    NNTensorType_I16 = lib.NNTensorType_I16 
    NNTensorType_U16 = lib.NNTensorType_U16 
    NNTensorType_I32 = lib.NNTensorType_I32 
    NNTensorType_U32 = lib.NNTensorType_U32 
    NNTensorType_I64 = lib.NNTensorType_I64 
    NNTensorType_U64 = lib.NNTensorType_U64 
    NNTensorType_F16 = lib.NNTensorType_F16 
    NNTensorType_F32 = lib.NNTensorType_F32 
    NNTensorType_F64 = lib.NNTensorType_F64 

    def __init__(self,
                 copy_from=None,        # type: Optional[numpy.ndarray]
                 shape=None,            # type: Optional[Tuple[int, ...]]
                 engine=None,           # type: Optional[Engine]
                 dtype=numpy.float32,   # type: numpy.dtype
                 wrap=None              # type: Optional[long]
                 ):
        # type: (...) -> None
        """
        Constructs a DeepViewRT tensor.  If copy_from is set to a valid Numpy
        array it will be mapped into the Tensor and a reference will be held
        to ensure validity across the lifespan of the tensor, if shape is also
        provided the tensor will be reshaped accordingly.

        Note that though copy_from will be mapped to the Tensor there's no
        guarantee that the memory will be used beyond initialization of a
        Engine backed tensor as this is defined by the specific engine
        implementation.  As an alternative consider a role reversal where the
        tensor owns the data and a numpy array is retrieved through tensor's
        map/unmap methods.

        If copy_from is None then shape can be used to allocate a zero
        initialized tensor. If neither copy_from nor shape is provided then an
        empty tensor is created.

        The engine parameter can be used to create a Tensor using the
        specified engine plugin.

        Args:
            copy_from (Optional[numpy.ndarray]):
                Create a tensor mapped from the specified numpy array.
            shape (Optional[List[int]]):
                Shape (or reshape, if copy_from is provided) of the tensor.
            engine (Optional[Engine]):
                Create the tensor using this engine.
            dtype (numpy.dtype):
                Sets the underlying datatype, only numpy.float32 is currently
                supported.

        Raises:
            TensorTypeUnsupportedError:
                If dtype is an unknown or unsupported type.
            Error:
                If an internal error occurs.
        """
        if wrap is not None:
            self.owns_self = False
            self.ptr = wrap
        else:
            self.owns_self = True
            self.mem = ffi.new('char[]', lib.nn_tensor_sizeof())

            eng = ffi.NULL
            if engine is not None:
                eng = engine.ptr
            elif EngineContext.current is not None:
                eng = EngineContext.current.ptr

            self.ptr = lib.nn_tensor_init(self.mem, eng)
            self.engine = engine

            if copy_from is not None:
                self.copied_from = copy_from.astype(numpy.float32,
                                                    order='C',
                                                    casting='unsafe',
                                                    copy=False)
                local_shape = tuple([int(x) for x in copy_from.shape])
                err = lib.nn_tensor_assign(self.ptr,
                                           nativetype(dtype),
                                           len(local_shape), local_shape,
                                           ffi.from_buffer(self.copied_from))
                check_error(err)
                if shape is not None:
                    self.reshape(shape)
            elif shape is not None:
                # Ensure shape is a Tuple[int, ...].
                local_shape = tuple([int(x) for x in shape])
                err = lib.nn_tensor_alloc(self.ptr,
                                          nativetype(dtype),
                                          len(local_shape),
                                          local_shape)
                check_error(err)

    def __del__(self):
        if self.owns_self:
            lib.nn_tensor_release(self.ptr)

    def __repr__(self):
        s = self.map().__repr__()
        self.unmap()
        return s

    def engine_name(self):
        # type: () -> Optional[str]
        """
        The tensor's engine's name.

        Returns:
            str: Engine name or None if no engine is associated to tensor.
        """
        engine = lib.nn_tensor_engine(self.ptr)
        if engine != ffi.NULL:
            return ffi.string(lib.nn_engine_name(engine)).decode('utf-8')
        return None

    def engine_version(self):
        # type: () -> Optional[str]
        """
        The tensor's engine's version number.

        Returns:
            str:
                Engine version string or None if no engine is associated to
                tensor.
        """
        engine = lib.nn_tensor_engine(self.ptr)
        if engine != ffi.NULL:
            return ffi.string(lib.nn_engine_version(engine)).decode('utf-8')
        return None

    def volume(self):
        # type: () -> int
        """
        Volume of the tensor's data which is the inner product of it's shape.

        Returns:
            int: The volume of the tensor.
        """
        return lib.nn_tensor_volume(self.ptr)

    def element_size(self):
        # type: () -> int
        """
        Size in bytes of an individual tensor data element.

        Returns:
            int: Element size of the tensor.
        """
        return lib.nn_tensor_element_size(self.ptr)

    @property
    def ntype(self):
        # type: () -> int
        return lib.nn_tensor_type(self.ptr)

    @property
    def dtype(self):
        # type: () -> numpy.dtype
        return numpytype(self.ntype)

    @property
    def time(self):
        # type: () -> int
        return lib.nn_tensor_time(self.ptr)

    def size(self):
        # type: () -> int
        """
        Size in bytes of the tensor's data, this is equivalent to
        volume * element_size.

        Returns:
            int: The tensor's data size in bytes.
        """
        return self.volume() * self.element_size()

    @property
    def dims(self):
        # type: () -> int
        """
        Number of dimensions for this tensor.

        Returns:
            int: the number of dimensions for the tensor.
        """
        return lib.nn_tensor_dims(self.ptr)

    @property
    def shape(self):
        # type: () -> Tuple[int, ...]
        """
        Shape of the tensor's data.

        Returns:
            Tuple[int, ...]: The shape of the tensor.
        """
        return tuple([int(i) for i in ffi.cast('int32_t[%d]' %
                                               lib.nn_tensor_dims(self.ptr),
                                               lib.nn_tensor_shape(self.ptr))])

    def reshape(self, newshape):
        # type: (Tuple[int, ...]) -> Tuple[int, ...]
        """
        Reshapes the tensor representation, new shape must have the same
        volume as previous.

        Raises:
            Error: If reshape operation fails.
        """
        err = lib.nn_tensor_reshape(self.ptr, len(newshape), newshape)
        check_error(err)

        return self.shape

    def sync(self):
        # type: () -> None
        """
        Synchronize the tensor and preceeding operations.

        Raises:
            Error: If synchronization fails.
        """
        err = lib.nn_tensor_sync(self.ptr)
        check_error(err)

    def map(self, writeable=True):
        # type: (bool) -> numpy.ndarray
        """
        Maps the tensor and returns a Numpy array map over the underlying
        buffer. The tensor must be unmapped once no longer needed, note that
        extreme care must be taken if calling unmap while the Numpy array
        continues to exist with a now invalid pointer.  Another option is to
        use the array() method which will return a copy of the tensor's data
        which is safer though slower.

        Args:
            writeable (bool):
                If true the tensor is mapped as writeable otherwise read-only

        Returns:
            numpy.ndarray: A Numpy array mapped to the tensor's data.

        Raises:
            TensorNoDataError:
                If the map failed, likely because the tensor has no data.
        """
        if writeable:
            m = lib.nn_tensor_maprw(self.ptr)
        else:
            m = lib.nn_tensor_mapro(self.ptr)
        if m == ffi.NULL:
            check_error(14)
        buf = ffi.buffer(m, self.size())
        t = numpy.frombuffer(buf, self.dtype)
        return numpy.reshape(t, self.shape)

    def unmap(self):
        # type: () -> None
        """
        Unmaps the tensor.

        Raises:
            Error: on internal error.
        """
        lib.nn_tensor_unmap(self.ptr)

    def array(self):
        # type: () -> numpy.ndarray
        """
        Returns a copy of the tensor's data as a new numpy array.

        Returns:
            numpy.ndarray: Numpy array of the tensor's data

        Raises:
            TensorNoDataError: if the tensor has no data.
        """
        m = self.map(False)
        a = m.copy()
        self.unmap()
        return a

    def copy_from(self, x):
        # type: (numpy.ndarray) -> None
        """
        Copies the Numpy array into the Tensor
        """
        if isinstance(x, numpy.ndarray):
            m = self.map(True)
            m[:] = x
            self.unmap()
        elif isinstance(x, Tensor):
            err = lib.nn_tensor_copy(self.ptr, x.ptr)
            check_error(err, 'Tensor copy_from failed')
        else:
            raise ValueError('Tensor copy_from with invalid type:', type(x))

    def fill(self, value):
        # type: (float) -> None
        """
        Fills the tensor with the provided value which will be casted
        to double then eventually to the tensor's data type.
        """
        err = lib.nn_tensor_fill(self.ptr, ffi.cast("double", value))
        check_error(err)

    def pad(self, head, tail, fill=0.0, out=None):
        # type: (Tuple[int, ...], Tuple[int, ...], float) -> Tensor
        if len(head) != len(tail) or len(head) != len(self.shape):
            check_error(8, 'pad head [%s] and tail [%s] size must '
                        'match tensor dimension count %d' %
                        (head, tail, self.dims))

        head = tuple([int(x) for x in head])
        tail = tuple([int(x) for x in tail])
        shape = tuple([i + h + t for i, h, t
                       in zip(self.shape, head, tail)])

        if out is not None:
            if out.shape != shape:
                raise ValueError('shape mismatch padding into out '
                                 '%s requires %d' % (out.shape, shape))
        else:
            out = Tensor(shape=shape, engine=self.engine)

        err = lib.nn_tensor_pad(out.ptr, self.ptr, head, tail, fill)
        check_error(err)
        return out

    def shuffle(self, order, out=None):
        if len(order) > self.dims:
            check_error(8, 'order tuple must match tensor rank')

        if out is None:
            out = Tensor(shape=self.shape, engine=self.engine)

        err = lib.nn_tensor_shuffle(out.ptr, self.ptr, len(order), order)
        check_error(err, 'failed to shuffle tensor using order %s' % order)
        return out

    def slice(self, axes, head=None, tail=None, out=None):
        if len(axes) > self.dims:
            check_error(8, 'axes tuple larger than tensor rank')

        for a in axes:
            if a < 0 or a > self.dims:
                check_error(8, 'invalid axis: %d' % a)
        if head is not None:
            if len(axes) != len(head):
                check_error(8, 'size of head tuple must match axes')
        if tail is not None:
            if len(axes) != len(tail):
                check_error(8, 'size of tail tuple must match axes')

        head_ = [0, 0, 0, 0]
        tail_ = [self.shape[i] if i < self.dims else 1 for i in range(4)]

        for i in range(len(axes)):
            if head[i] < 0:
                head_[axes[i]] = self.shape[axes[i]] - head[i]
            else:
                head_[axes[i]] = head[i]

            if tail[i] == 0:
                tail_[axes[i]] = self.shape[axes[i]]
            elif tail[i] < 0:
                tail_[axes[i]] = self.shape[axes[i]] - tail[i]
            else:
                tail_[axes[i]] = tail[i]

        if out is None:
            outshape = [x for x in self.shape]
            for i in axes:
                outshape[i] -= head_[i]
                outshape[i] -= self.shape[i] - tail_[i]
            out = Tensor(shape=outshape, engine=self.engine)

        err = lib.nn_tensor_slice(out.ptr,
                                  self.ptr,
                                  len(axes),
                                  axes,
                                  head,
                                  tail)
        check_error(err)
        return out

    def view(self,                  # type: deepview.rt.Tensor
             shape,                 # type: Optional[Tuple[int, ...]]
             offset=0,              # type: int
             dtype=numpy.float32    # type: numpy.dtype
             ):
        tensor = Tensor(engine=self.engine)
        tensor.copied_from = self
        local_shape = tuple([int(x) for x in shape])
        err = lib.nn_tensor_view(tensor.ptr,
                                 nativetype(dtype),
                                 len(local_shape), local_shape,
                                 self.ptr,
                                 offset)
        check_error(err)
        return tensor
        
    class IMG_PROC:
        """
        Flags for how image preprocessing should be done
        """
        UNSIGNED_NORM = 0x0001
        WHITENING = 0x0002
        SIGNED_NORM = 0x0004
        IMAGENET = 0x0008
        MIRROR = 0x1000
        FLIP = 0x2000

    def get_aux_object(self, name:str, ntype:str = "float"):
        aux = lib.nn_tensor_aux_object_by_name(self.ptr, name.encode("ASCII"))
        aux = ffi.cast(ntype+"*", aux)
        return aux

    @ffi.callback("void(NNTensor*)")
    def nn_free(x):
        if x:
            lib.nn_free(x)

    def set_aux_object(self, name:str, data:List, ntype:str = "float"):
        aux = lib.nn_tensor_aux_object_by_name(self.ptr, name.encode("ASCII"))

        if aux:
            aux = ffi.cast(ntype+"*", aux)
        else:
            aux = ffi.cast(ntype+"*", lib.nn_malloc(ffi.sizeof(ntype) * len(data)))
            lib.nn_tensor_set_aux_object_by_name(self.ptr, name.encode("ASCII"), aux, Tensor.nn_free, 1, 0)

        for i in range(len(data)):
            aux[i] = data[i]
        return
    
    def map_read(self, ntype:str = "float"):
        data = lib.nn_tensor_mapro(self.ptr)
        data = ffi.cast(ntype+"*", data)
        return data

    def load_image(self, image_fp, img_proc:int):
        """
        Loads an image into the tensor using PIL and numpy

        Parameters
        ----------
        image_fp: str | bytes | Path | SupportsRead[Bytes]
            A filename or path object or file object of the image to load into the tensor
        
        img_proc: int
            The image processing flags to use
        """
        from PIL import Image
        import math
        tensor_shape = self.shape
        tensor_size = self.size()
        tensor_type = self.ntype

        if tensor_type == Tensor.NNTensorType_U8 or tensor_type == Tensor.NNTensorType_I8:
            if img_proc:
                raise NotImplementedError
            im = Image.open(image_fp)
            im = im.resize((tensor_shape[2], tensor_shape[1]), Image.BICUBIC)
            source:numpy.ndarray = numpy.array(im)

            # This resize pads the channels if needed
            source.resize((tensor_shape[1], tensor_shape[2], tensor_shape[3]))
            if tensor_type == Tensor.NNTensorType_U8:
                source = source.astype("uint8")
            else:
                minus128 = lambda x: x - 128
                source = minus128(source)
                source = source.astype("int8")

            self.copy_from(source)
            return
        elif tensor_type == Tensor.NNTensorType_F32:
            im = Image.open(image_fp)
            im = im.resize((tensor_shape[2], tensor_shape[1]), Image.BICUBIC)
            source:numpy.ndarray = numpy.array(im)
            c = source.shape[2]
            # This resize pads the channels if needed
            source.resize((tensor_shape[1], tensor_shape[2], tensor_shape[3]))
            source = source.astype("float32")
            if img_proc & Tensor.IMG_PROC.UNSIGNED_NORM:
                unsigned_float = lambda x: x / 255.0
                source = unsigned_float(source)
            if img_proc & Tensor.IMG_PROC.SIGNED_NORM:
                signed_float = lambda x: x / 127.5 - 1
                source = signed_float(source)
            if (img_proc & Tensor.IMG_PROC.IMAGENET) and c==3:
                source[:,:,0] -= 123
                source[:,:,1] -= 116
                source[:,:,2] -= 103
            if img_proc & Tensor.IMG_PROC.WHITENING:
                def rgb_statsf(data:numpy.ndarray):
                    n = data.size
                    total = data.sum()
                    square = lambda x: x * x
                    sq_total = square(data).sum()
                    mean = total/n
                    variance = sq_total / n - mean * mean
                    stddev = math.sqrt(variance)
                    return n, mean, stddev
                n, mean, stddev = rgb_statsf(source)
                std_adj = max(stddev, 1/math.sqrt(n))
                normalize = lambda x: (x-mean)/std_adj
                source = normalize(source)
            
            self.copy_from(source)
            return
        raise ValueError("ERROR Tensor type unsupported")

    def tensor_offset(self, *dims):
        dims = [ffi.cast("int32_t", x) for x in dims]
        return lib.nn_tensor_offsetv(self.ptr, *dims)