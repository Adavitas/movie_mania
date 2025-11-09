"""
Player input handling for Movie Mania game.
"""

import time
from src.config import (
    WIDTH, HEIGHT, MAX_NAME_LENGTH, GLOW_COLOR, 
    TEXT_COLOR, QUESTION_FONT
)
from src.ui.graphics import create_cinematic_background
from src.ui.animations import animate_text


def get_player_name(canvas):
    """
    Prompt user to enter their name with keyboard input.
    
    Args:
        canvas: Canvas object
    
    Returns:
        str: Player name (defaults to "Player" if empty)
    """
    canvas.clear()
    create_cinematic_background(canvas)
    
    # Prompt
    animate_text(
        canvas, "Enter Your Name", WIDTH//2, HEIGHT//2-50, 
        QUESTION_FONT, 36, GLOW_COLOR, delay=0.03
    )
    
    # Name display
    name_id = canvas.create_text(
        WIDTH//2, HEIGHT//2+50, text="", 
        font=QUESTION_FONT, font_size=24, 
        color=TEXT_COLOR, anchor="center"
    )
    
    return _name_input_loop(canvas, name_id)


def _name_input_loop(canvas, name_id):
    """Handle name input loop."""
    name = ""
    
    while True:
        keys = canvas.get_new_key_presses()
        for key in keys:
            key_normalized = key.upper()
            
            if key_normalized in ["RETURN", "ENTER"] and name.strip():
                time.sleep(0.5)
                return name.strip() or "Player"
            elif key_normalized == "BACKSPACE" and len(name) > 0:
                name = name[:-1]
            elif len(key) == 1 and key.isalpha() and len(name) < MAX_NAME_LENGTH:
                name += key
            
            canvas.change_text(name_id, name)
        
        time.sleep(0.005)


def wait_for_answer_or_lifeline(canvas, lifelines_available):
    """
    Wait for player to select answer (A-D) or use lifeline (1-3).
    
    Args:
        canvas: Canvas object
        lifelines_available: Dict of available lifelines
    
    Returns:
        str or None: Key pressed (A-D, 1-3) or None
    """
    keys = canvas.get_new_key_presses()
    if not keys:
        return None
    
    key = keys[0].upper()
    
    # Check for valid answer
    if key in ['A', 'B', 'C', 'D']:
        return key
    
    # Check for valid lifeline
    if key == '1' and not lifelines_available.get("5050"):
        return '1'
    elif key == '2' and not lifelines_available.get("phone"):
        return '2'
    elif key == '3' and not lifelines_available.get("audience"):
        return '3'
    
    return None


def highlight_selected_answer(canvas, letter):
    """
    Highlight the selected answer option.
    
    Args:
        canvas: Canvas object
        letter: Letter of selected answer (A-D)
    
    Returns:
        int: ID of highlight rectangle
    """
    from src.config import ACCENT_COLOR
    
    # Calculate position based on letter
    index = ord(letter) - ord('A')
    x = WIDTH//4 + (index % 2) * (WIDTH//2)
    y = 300 + (index // 2) * 120
    
    # Draw highlight
    rect_id = canvas.create_rectangle(
        x-180, y-35, x+180, y+35, outline=ACCENT_COLOR
    )
    canvas.create_rectangle(
        x-178, y-33, x+178, y+33, 
        outline="rgba(0,183,183,0.6)"
    )
    
    time.sleep(0.25)
    return rect_id


def show_correct_answer_effect(canvas):
    """
    Display visual effect for correct answer.
    
    Args:
        canvas: Canvas object
    """
    from src.config import ACCENT_COLOR
    
    # Just show a quick "Correct!" message - no animations
    effect_id = canvas.create_text(
        WIDTH//2, HEIGHT-100, text="✓ Correct!", 
        font=QUESTION_FONT, font_size=28, 
        color=ACCENT_COLOR, anchor="center"
    )
