"""
Graphics utilities for Movie Mania game.
Contains background, UI elements, and visual components.
"""

import time
import random
from src.config import (
    WIDTH, HEIGHT, BACKGROUND_COLOR, GLOW_COLOR, PANEL_COLOR,
    BAR_COLOR, ACCENT_COLOR, TEXT_COLOR, QUESTION_FONT,
    TITLE_FONT_SIZE, QUESTION_FONT_SIZE, ANSWER_FONT_SIZE
)
from src.ui.animations import animate_text, animate_progress_bar


def create_cinematic_background(canvas):
    """
    Create a cinematic background with starry sky and soft gradients.
    
    Args:
        canvas: Canvas object to draw on
    """
    # Base background
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, color=BACKGROUND_COLOR)
    
    # Gradient panels
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT//3, color="#0f2a4a")
    canvas.create_rectangle(0, 2*HEIGHT//3, WIDTH, HEIGHT, color="#0f2a4a")
    
    # Stars
    for _ in range(20):
        x = random.randint(20, WIDTH-20)
        y = random.randint(0, HEIGHT-20)
        size = random.randint(2, 5)
        canvas.create_oval(
            x-size, y-size, x+size, y+size, 
            color="rgba(255,255,255,0.5)", outline=""
        )
        time.sleep(0.05)  # Much slower star animation
    
    # Decorative elements
    canvas.create_rectangle(25, 25, WIDTH-25, 27, color=GLOW_COLOR)
    canvas.create_oval(
        WIDTH//4-20, HEIGHT//4-20, 
        WIDTH//4+20, HEIGHT//4+20, 
        outline=GLOW_COLOR
    )
    canvas.create_oval(
        3*WIDTH//4-20, 3*HEIGHT//4-20, 
        3*WIDTH//4+20, 3*HEIGHT//4+20, 
        outline=GLOW_COLOR
    )


def draw_progress_bar(canvas, question_num, total_questions):
    """
    Draw animated progress bar showing game progress.
    
    Args:
        canvas: Canvas object
        question_num: Current question number
        total_questions: Total number of questions
    """
    progress = (question_num / total_questions) * 100
    bar_width = (WIDTH - 100) * (progress / 100)
    
    # Bar container
    canvas.create_rectangle(
        50, 30, WIDTH-50, 50, 
        color=PANEL_COLOR, outline=GLOW_COLOR
    )
    
    # Animated fill
    animate_progress_bar(canvas, 50, 30, WIDTH-50, 50, bar_width, ACCENT_COLOR)
    
    # Blink effect
    _add_bar_blink_effect(canvas, bar_width)
    
    # Progress text
    canvas.create_text(
        WIDTH//2, 40, 
        text=f"Question {question_num}/{total_questions} ({int(progress)}%)", 
        font=QUESTION_FONT, font_size=18, 
        color=TEXT_COLOR, anchor="center"
    )


def _add_bar_blink_effect(canvas, bar_width):
    """Add blinking effect to progress bar."""
    for _ in range(2):
        canvas.create_rectangle(
            50, 30, 50+bar_width, 50, 
            outline="rgba(0,183,183,0.5)"
        )
        time.sleep(0.4)  # Slower blink
        canvas.create_rectangle(
            50, 30, 50+bar_width, 50, 
            outline=GLOW_COLOR
        )
        time.sleep(0.4)  # Slower blink


def draw_title_with_shadow(canvas, text, x, y):
    """
    Draw title text with shadow effect.
    
    Args:
        canvas: Canvas object
        text: Title text
        x, y: Position coordinates
    """
    # Shadow layers
    for offset in [2, -2, 2, -2]:
        canvas.create_text(
            x+offset, y+offset, text=text, 
            font=QUESTION_FONT, font_size=TITLE_FONT_SIZE, 
            color=f"rgba(230,184,0,{0.2 if abs(offset) == 2 else 0.3})", 
            anchor="center"
        )
    
    # Main title
    canvas.create_text(
        x, y, text=text, 
        font=QUESTION_FONT, font_size=TITLE_FONT_SIZE, 
        color=GLOW_COLOR, anchor="center"
    )


def draw_answer_options(canvas, options, start_y=300):
    """
    Draw answer option boxes with letters.
    
    Args:
        canvas: Canvas object
        options: List of answer options
        start_y: Starting Y coordinate
    
    Returns:
        dict: Mapping of letters to text IDs
    """
    letters = ['A', 'B', 'C', 'D']
    answer_ids = {}
    
    for i in range(len(options)):
        x = WIDTH//4 + (i % 2) * (WIDTH//2)
        y = start_y + (i // 2) * 120
        
        _draw_single_answer_box(canvas, x, y)
        
        # Answer text
        answer_ids[letters[i]] = canvas.create_text(
            x, y, text=f"{letters[i]}: {options[i]}", 
            font=QUESTION_FONT, font_size=ANSWER_FONT_SIZE, 
            color=TEXT_COLOR, anchor="center"
        )
    
    return answer_ids


def _draw_single_answer_box(canvas, x, y):
    """Draw a single answer option box with decorations."""
    # Option box
    canvas.create_rectangle(
        x-180, y-35, x+180, y+35, 
        color=PANEL_COLOR, outline=GLOW_COLOR
    )
    
    # Corner decorations
    for cx, cy in [(x-180, y-35), (x-180, y+35), 
                   (x+180, y-35), (x+180, y+35)]:
        canvas.create_oval(
            cx-5, cy-5, cx+5, cy+5, 
            color=PANEL_COLOR, outline=GLOW_COLOR
        )
    
    # Inner border
    canvas.create_rectangle(
        x-178, y-33, x+178, y+33, 
        outline="rgba(230,184,0,0.25)"
    )
