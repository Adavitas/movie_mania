"""
Drawing methods for Canvas class.
Provides methods to create shapes and text on the canvas.
"""

from .utils import convert_rgba_to_rgb


def create_rectangle(canvas_obj, x1: float, y1: float, x2: float, y2: float, 
                    color: str = 'black', outline: str = '') -> int:
    """
    Create a rectangle on the canvas.
    
    Args:
        canvas_obj: Canvas instance
        x1, y1: Top-left corner
        x2, y2: Bottom-right corner
        color: Fill color
        outline: Outline color (default: no outline)
        
    Returns:
        Object ID
    """
    color = convert_rgba_to_rgb(color)
    outline = convert_rgba_to_rgb(outline) if outline else color
    
    obj_id = canvas_obj.canvas.create_rectangle(
        x1, y1, x2, y2,
        fill=color,
        outline=outline,
        width=0 if not outline else 1
    )
    canvas_obj.objects[obj_id] = ('rectangle', x1, y1, x2, y2, color)
    canvas_obj.root.update()
    return obj_id


def create_oval(canvas_obj, x1: float, y1: float, x2: float, y2: float,
               color: str = 'black', outline: str = '') -> int:
    """
    Create an oval/circle on the canvas.
    
    Args:
        canvas_obj: Canvas instance
        x1, y1: Top-left corner of bounding box
        x2, y2: Bottom-right corner of bounding box
        color: Fill color
        outline: Outline color
        
    Returns:
        Object ID
    """
    color = convert_rgba_to_rgb(color)
    outline = convert_rgba_to_rgb(outline) if outline else color
    
    obj_id = canvas_obj.canvas.create_oval(
        x1, y1, x2, y2,
        fill=color,
        outline=outline,
        width=0 if not outline else 1
    )
    canvas_obj.objects[obj_id] = ('oval', x1, y1, x2, y2, color)
    canvas_obj.root.update()
    return obj_id


def create_text(canvas_obj, x: float, y: float, text: str,
               font: str = 'Arial', size: int = 12, font_size: int = None,
               color: str = 'black', anchor: str = 'center') -> int:
    """
    Create text on the canvas.
    
    Args:
        canvas_obj: Canvas instance
        x, y: Position of the text
        text: The text string
        font: Font family
        size: Font size (alternative: font_size)
        font_size: Font size (alternative: size)
        color: Text color
        anchor: Text anchor position
        
    Returns:
        Object ID
    """
    # Accept either 'size' or 'font_size'
    if font_size is not None:
        size = font_size
    
    color = convert_rgba_to_rgb(color)
    font_spec = (font, size)
    obj_id = canvas_obj.canvas.create_text(
        x, y,
        text=text,
        font=font_spec,
        fill=color,
        anchor=anchor
    )
    canvas_obj.objects[obj_id] = ('text', x, y, text, font, size, color)
    canvas_obj.root.update()
    return obj_id


def create_line(canvas_obj, x1: float, y1: float, x2: float, y2: float,
               color: str = 'black', width: int = 1) -> int:
    """
    Create a line on the canvas.
    
    Args:
        canvas_obj: Canvas instance
        x1, y1: Start point
        x2, y2: End point
        color: Line color
        width: Line width
        
    Returns:
        Object ID
    """
    color = convert_rgba_to_rgb(color)
    obj_id = canvas_obj.canvas.create_line(
        x1, y1, x2, y2,
        fill=color,
        width=width
    )
    canvas_obj.objects[obj_id] = ('line', x1, y1, x2, y2, color)
    canvas_obj.root.update()
    return obj_id
