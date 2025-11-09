"""
Timer display module for Movie Mania game.
"""

import time
from src.config import (
    WIDTH, BAR_COLOR, ACCENT_COLOR, GLOW_COLOR,
    TIMER_TEXT_COLOR, QUESTION_FONT, TIMER_FONT_SIZE, TIMER_DURATION
)


def create_timer_display(canvas):
    """
    Create circular timer display in top-right corner.
    
    Args:
        canvas: Canvas object
    
    Returns:
        text_id: ID of timer text object
    """
    # Outer circle
    canvas.create_oval(
        WIDTH-100, 40, WIDTH-20, 120, 
        color=BAR_COLOR, outline=ACCENT_COLOR
    )
    
    # Inner circle
    canvas.create_oval(
        WIDTH-100, 40, WIDTH-20, 120, 
        color="#2a4a6a"
    )
    
    # Border highlight
    canvas.create_oval(
        WIDTH-98, 42, WIDTH-22, 118, 
        outline="rgba(0,183,183,0.5)"
    )
    
    # Timer text
    text_id = canvas.create_text(
        WIDTH-60, 80, text=f"{TIMER_DURATION}s", 
        font=QUESTION_FONT, font_size=TIMER_FONT_SIZE, 
        color=TIMER_TEXT_COLOR, anchor="center"
    )
    
    return text_id


def update_timer_display(canvas, time_left_id, time_left):
    """
    Update timer display with current time and visual indicator.
    
    Args:
        canvas: Canvas object
        time_left_id: ID of timer text
        time_left: Seconds remaining
    """
    # Only update the progress circle and text - don't redraw background
    # This prevents flickering
    
    # Progress indicator - yellow circle that shrinks
    radius = 40 * (time_left / TIMER_DURATION)
    canvas.create_oval(
        WIDTH-60-radius, 80-radius, 
        WIDTH-60+radius, 80+radius, 
        color="", outline=GLOW_COLOR
    )
    
    # Update text
    canvas.change_text(time_left_id, f"{time_left}s")


def flash_timer_timeout(canvas, time_left_id):
    """
    Flash timer when time runs out.
    
    Args:
        canvas: Canvas object
        time_left_id: ID of timer text
    """
    from src.config import PANEL_COLOR
    
    for _ in range(3):
        canvas.set_color(time_left_id, TIMER_TEXT_COLOR)
        time.sleep(0.25)
        canvas.set_color(time_left_id, PANEL_COLOR)
        time.sleep(0.25)
