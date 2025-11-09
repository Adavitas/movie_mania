"""
Animation utilities for Movie Mania game.
Contains text animation and visual effects.
"""

import time
from src.config import TEXT_ANIMATION_DELAY, BLINK_DURATION, FADE_STEP


def animate_text(canvas, text, x, y, font, font_size, color, delay=TEXT_ANIMATION_DELAY):
    """
    Display text with a typewriter animation effect.
    
    Args:
        canvas: Canvas object to draw on
        text: Text string to animate
        x, y: Position coordinates
        font: Font name
        font_size: Size of font
        color: Text color
        delay: Delay between characters
    
    Returns:
        text_id: ID of the created text object
    """
    text_id = canvas.create_text(
        x, y, text="", font=font, 
        font_size=font_size, color=color, anchor="center"
    )
    current_text = ""
    for char in text:
        current_text += char
        canvas.change_text(text_id, current_text)
        time.sleep(delay)
    return text_id


def blink_text(canvas, text_id, color1, color2, times=3):
    """
    Make text blink by alternating between two colors.
    
    Args:
        canvas: Canvas object
        text_id: ID of text to blink
        color1: First color
        color2: Second color
        times: Number of blinks
    """
    for _ in range(times):
        canvas.set_color(text_id, color2)
        time.sleep(BLINK_DURATION)
        canvas.set_color(text_id, color1)
        time.sleep(BLINK_DURATION)


def fade_out_text(canvas, text_id, base_color="240,240,240"):
    """
    Fade out text by decreasing alpha channel.
    
    Args:
        canvas: Canvas object
        text_id: ID of text to fade
        base_color: RGB values as string (e.g., "240,240,240")
    """
    for alpha in range(100, -1, -FADE_STEP):
        canvas.set_color(text_id, f"rgba({base_color},{alpha/100})")
        time.sleep(0.15)  # Much slower fade


def animate_progress_bar(canvas, x1, y1, x2, y2, target_width, color):
    """
    Animate a progress bar filling up.
    
    Args:
        canvas: Canvas object
        x1, y1: Top-left corner coordinates
        x2, y2: Bottom-right corner coordinates
        target_width: Final width of progress bar
        color: Base color for gradient
    """
    for w in range(0, int(target_width), 5):
        # Create gradient color, capping values at 255 (0xFF)
        shade_val = min(w//5 + 180, 255)
        shade = f"#00{shade_val:02x}{shade_val:02x}"
        canvas.create_rectangle(x1, y1, x1+w, y2, color=shade)
        time.sleep(0.03)  # Much slower progress bar


def create_sparkle_effect(canvas, center_x, center_y, count=10):
    """
    Create sparkle effect around a point.
    
    Args:
        canvas: Canvas object
        center_x, center_y: Center coordinates
        count: Number of sparkles
    """
    import random
    for i in range(count):
        x = center_x + random.randint(-100, 100)
        y = center_y + random.randint(-100, 100)
        canvas.create_oval(x-10, y-10, x+10, y+10, 
                          color="#00b7b7", outline="")
        time.sleep(0.15)  # Much slower sparkle effect
