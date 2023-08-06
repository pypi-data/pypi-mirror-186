"""The submodules contained in this module are implementations of the encoding process in MRI. The
shared calculation (namely the evaluating the fourier phase for each k-space point) are implemented
in the build class. The actual definition of the k-space trajectory is done in a corresponding
subclass."""
import importlib

from cmrsim.analytic.encoding.base import *
from cmrsim.analytic.encoding.cartesian import *
from cmrsim.analytic.encoding._from_sequence import GenericEncoding

_submodules = ["base", "cartesian", "_from_sequence"]
mod_handles = [importlib.import_module(f"cmrsim.analytic.encoding.{m}") for m in _submodules]
__all__ = [item for m in mod_handles for item in getattr(m, '__all__')]
