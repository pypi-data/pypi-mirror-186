# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

"""
DeepViewRT for Python provides Python bindings for the target run-time of the
DeepView Machine Learning Toolkit implementing neural network primitives and
model inference support.  The Python bindings are implemented using the CFFI
module to interact directly with the DeepViewRT C ABI.  To use this module,
libdeepview-rt.so needs to be available in the library search path along with
any engines that are to be used (ex: deepview-rt-opencl.so).  On Windows the
library will be called deepview-rt.dll and on MacOSX it will be called
libdeepview-rt.dylib, otherwise the usage remains the same.
"""

from typing import List, Optional
from .librt import lib, ffi
from .errors import *
from .tensor import Tensor
from .engine import Engine, EngineContext
from .context import Context
from .ops.activation import Activation
from .modelclient import ModelClient

from .common import version, init
from . import ops
