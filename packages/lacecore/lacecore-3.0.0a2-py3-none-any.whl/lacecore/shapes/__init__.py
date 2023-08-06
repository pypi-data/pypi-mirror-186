"""
Functions for creating meshes for tesselated 3D shapes.

See also:
    https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)
"""

from . import _shapes
from ._shapes import *  # noqa: F401,F403

__all__ = _shapes.__all__
