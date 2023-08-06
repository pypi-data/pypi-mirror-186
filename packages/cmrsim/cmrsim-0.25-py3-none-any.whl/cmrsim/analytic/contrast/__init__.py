""" This module contains operators corresponding to analytical solutions to the bloch equations. """
import importlib

from cmrsim.analytic.contrast.base import *
from cmrsim.analytic.contrast.coil_sensitivities import *
from cmrsim.analytic.contrast.diffusion_weighting import *
from cmrsim.analytic.contrast.phase_tracking import *
from cmrsim.analytic.contrast.sequences import *
from cmrsim.analytic.contrast.t2_star import *

_submodules = ["base", "coil_sensitivities", "diffusion_weighting", "phase_tracking", "sequences",
               "t2_star"]
mod_handles = [importlib.import_module(f"cmrsim.analytic.contrast.{m}") for m in _submodules]
__all__ = [item for m in mod_handles for item in getattr(m, '__all__')]
