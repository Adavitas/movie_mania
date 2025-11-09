"""
Stanford CS106A Graphics Library - Compatible Implementation
A tkinter-based implementation of the Canvas class for educational graphics.
"""

import tkinter as tk
from typing import Dict, List
from . import drawing, input as input_module, utils


class Canvas:
    """
    A canvas for drawing graphics, compatible with Stanford CS106A style.
    """
    
    def __init__(self, width: int = 800, height: int = 600, 
                 title: str = "Graphics Window"):
        """
        Create a new Canvas window.
        
        Args:
            width: Width of the canvas in pixels
            height: Height of the canvas in pixels
            title: Title of the window
        """
        self.width = width
        self.height = height
        self.title = title
        
        # Create the tkinter window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        
        # Create the canvas
        self.canvas = tk.Canvas(
            self.root,
            width=width,
            height=height,
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Track objects and key presses
        self.objects: Dict = {}
        self.key_presses: List[str] = []
        self.last_keys: List[str] = []
        
        # Bind key events
        self.root.bind('<KeyPress>', self._on_key_press)
        
        # Make sure the window has focus for keyboard input
        self.root.focus_force()
        self.canvas.focus_set()
        
        # Update the window
        self.root.update()
    
    def _on_key_press(self, event):
        """Handle key press events."""
        # Use keysym for special keys, char for regular characters
        if event.keysym in ['Return', 'KP_Enter']:
            key = 'RETURN'  # Normalize Enter key
        elif event.keysym == 'BackSpace':
            key = 'BACKSPACE'  # Normalize Backspace
        elif event.keysym == 'Escape':
            key = 'ESCAPE'
        elif event.char:
            key = event.char  # Regular character
        else:
            key = event.keysym  # Other special keys
        
        if key not in self.key_presses:
            self.key_presses.append(key)
    
    # Drawing methods (delegated)
    def create_rectangle(self, x1: float, y1: float, x2: float, y2: float,
                        color: str = 'black', outline: str = '') -> int:
        """Create a rectangle on the canvas."""
        return drawing.create_rectangle(self, x1, y1, x2, y2, color, outline)
    
    def create_oval(self, x1: float, y1: float, x2: float, y2: float,
                   color: str = 'black', outline: str = '') -> int:
        """Create an oval/circle on the canvas."""
        return drawing.create_oval(self, x1, y1, x2, y2, color, outline)
    
    def create_text(self, x: float, y: float, text: str, font: str = 'Arial',
                   size: int = 12, font_size: int = None, color: str = 'black',
                   anchor: str = 'center') -> int:
        """Create text on the canvas."""
        return drawing.create_text(
            self, x, y, text, font, size, font_size, color, anchor
        )
    
    def create_line(self, x1: float, y1: float, x2: float, y2: float,
                   color: str = 'black', width: int = 1) -> int:
        """Create a line on the canvas."""
        return drawing.create_line(self, x1, y1, x2, y2, color, width)
    
    # Input methods (delegated)
    def get_new_key_presses(self) -> List[str]:
        """Get all new key presses since the last call."""
        return input_module.get_new_key_presses(self)
    
    def wait_for_click(self):
        """Wait for a mouse click."""
        input_module.wait_for_click(self)
    
    def get_mouse_x(self) -> int:
        """Get the current mouse x position."""
        return input_module.get_mouse_x(self)
    
    def get_mouse_y(self) -> int:
        """Get the current mouse y position."""
        return input_module.get_mouse_y(self)
    
    # Object manipulation methods
    def delete(self, obj_id: int):
        """
        Delete an object from the canvas.
        
        Args:
            obj_id: Object ID to delete
        """
        self.canvas.delete(obj_id)
        if obj_id in self.objects:
            del self.objects[obj_id]
        self.root.update()
    
    def clear(self):
        """Clear all objects from the canvas."""
        self.canvas.delete('all')
        self.objects.clear()
        self.root.update()
    
    def set_color(self, obj_id: int, color: str):
        """
        Change the color of an object.
        
        Args:
            obj_id: Object ID
            color: New color
        """
        try:
            # Convert RGBA to RGB (tkinter doesn't support alpha)
            color = utils.convert_rgba_to_rgb(color)
            self.canvas.itemconfig(obj_id, fill=color)
            self.root.update()
        except tk.TclError:
            pass  # Object might not exist
    
    def change_text(self, obj_id: int, new_text: str):
        """
        Change the text of a text object.
        
        Args:
            obj_id: Object ID
            new_text: New text string
        """
        try:
            self.canvas.itemconfig(obj_id, text=new_text)
            self.root.update()
        except tk.TclError:
            pass
    
    def update(self):
        """Update the canvas display."""
        try:
            self.root.update()
        except tk.TclError:
            pass
    
    def mainloop(self):
        """Start the tkinter main event loop."""
        self.root.mainloop()
    
    def close(self):
        """Close the canvas window."""
        try:
            self.root.destroy()
        except:
            pass
