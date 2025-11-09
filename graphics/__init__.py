"""
Graphics Package for Movie Mania
Provides the Canvas class and graphics utilities.
"""

from .canvas import Canvas
from .utils import rgb_to_hex, hex_to_rgb, convert_rgba_to_rgb

__all__ = ['Canvas', 'rgb_to_hex', 'hex_to_rgb', 'convert_rgba_to_rgb']
