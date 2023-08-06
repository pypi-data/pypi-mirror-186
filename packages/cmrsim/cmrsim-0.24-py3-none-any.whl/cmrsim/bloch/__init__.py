""" Module containing functionality to perform bloch simulation """

from cmrsim.bloch._base import *
from cmrsim.bloch._generic import *
from cmrsim.bloch._ideal import *
from cmrsim.bloch._multi_coil import *
import cmrsim.bloch.submodules

import importlib
_submodules = ["_base", "_generic", "_ideal", "_multi_coil"]
mod_handles = [importlib.import_module(f"cmrsim.bloch.{m}") for m in _submodules]
__all__ = [item for m in mod_handles for item in getattr(m, '__all__')] + ["submodules"]

