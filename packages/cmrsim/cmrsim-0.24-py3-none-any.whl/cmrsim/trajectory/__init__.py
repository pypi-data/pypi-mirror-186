""" This module contains various implementations of CMRsim compatible trajectory modules.
The implementation requirements are defined as abstract base class (BaseTrajectoryModule), which
should serve as primary superclass for all concrete trajectory module.

The general use of Trajectory modules can be summarized by two methods:

    1. Increment particle positions: A tf.function compatible method that takes the current position
    of particles and a temporal step width as input and returns the new positions. Additionally,
    a dictionary is returned that is not empty if a look-up is involved in the method.

    2. Calling the module (invoking __call__) which directly computes the position of particles for
    a specified set of time points. This can be used for pre-computation of positions .
"""
import glob
import os
import importlib

from cmrsim.trajectory._base import *
from cmrsim.trajectory._flow import *
from cmrsim.trajectory._taylor import *
from cmrsim.trajectory._diffusion import *
from cmrsim.trajectory._proper_ortho_decomp import *

# Compose __all__ on import
module_names = glob.glob(os.path.join(os.path.dirname(__file__), "_*.py"))
alls = [importlib.import_module("cmrsim.trajectory." + os.path.basename(f)[:-3]).__all__
        for f in module_names if os.path.isfile(f) and not f.endswith('__init__.py')]
__all__ = [a for alls_sub in alls for a in alls_sub]
