"""
Utility functions for the graphics package.
Color conversion and helper functions.
"""

def convert_rgba_to_rgb(color: str) -> str:
    """
    Convert RGBA color to RGB (tkinter doesn't support alpha channel).
    
    Args:
        color: Color string (can be rgba(...) or hex or named color)
        
    Returns:
        RGB color string
    """
    if not isinstance(color, str):
        return str(color)
    
    # Handle rgba(r,g,b,a) format
    if color.startswith('rgba('):
        try:
            # Extract rgba values
            values = color[5:-1].split(',')
            r, g, b = values[0].strip(), values[1].strip(), values[2].strip()
            # alpha = values[3].strip() # Ignore alpha for tkinter
            return f'#{int(r):02x}{int(g):02x}{int(b):02x}'
        except:
            return 'black'
    
    return color


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB values to hex color string.
    
    Args:
        r: Red value (0-255)
        g: Green value (0-255)
        b: Blue value (0-255)
        
    Returns:
        Hex color string (e.g., '#ff0000')
    """
    return f'#{r:02x}{g:02x}{b:02x}'


def hex_to_rgb(hex_color: str) -> tuple:
    """
    Convert hex color string to RGB tuple.
    
    Args:
        hex_color: Hex color string (e.g., '#ff0000')
        
    Returns:
        Tuple of (r, g, b) values
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
