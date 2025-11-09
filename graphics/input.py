"""
Input handling methods for Canvas class.
Keyboard and mouse input detection.
"""

import time


def get_new_key_presses(canvas_obj) -> list:
    """
    Get all new key presses since the last call.
    
    Args:
        canvas_obj: Canvas instance
        
    Returns:
        List of key press strings
    """
    canvas_obj.root.update()
    keys = canvas_obj.key_presses.copy()
    canvas_obj.key_presses.clear()
    return keys


def wait_for_click(canvas_obj):
    """
    Wait for a mouse click.
    
    Args:
        canvas_obj: Canvas instance
    """
    click_occurred = [False]
    
    def on_click(event):
        click_occurred[0] = True
    
    click_id = canvas_obj.canvas.bind('<Button-1>', on_click)
    
    while not click_occurred[0]:
        canvas_obj.root.update()
        time.sleep(0.01)
    
    canvas_obj.canvas.unbind('<Button-1>', click_id)


def get_mouse_x(canvas_obj) -> int:
    """
    Get the current mouse x position.
    
    Args:
        canvas_obj: Canvas instance
        
    Returns:
        Mouse x coordinate
    """
    return canvas_obj.root.winfo_pointerx() - canvas_obj.root.winfo_rootx()


def get_mouse_y(canvas_obj) -> int:
    """
    Get the current mouse y position.
    
    Args:
        canvas_obj: Canvas instance
        
    Returns:
        Mouse y coordinate
    """
    return canvas_obj.root.winfo_pointery() - canvas_obj.root.winfo_rooty()
