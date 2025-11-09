"""
Screen display module for splash screens and end game screens.
"""

import time
from src.config import (
    WIDTH, HEIGHT, QUESTION_FONT, TITLE_FONT_SIZE,
    GLOW_COLOR, ACCENT_COLOR, TEXT_COLOR, PANEL_COLOR
)
from src.ui.graphics import create_cinematic_background, draw_title_with_shadow
from src.ui.animations import animate_text, blink_text


def show_splash_screen(canvas, name):
    """
    Display splash screen with player's name and animated title.
    
    Args:
        canvas: Canvas object
        name: Player name
    """
    canvas.clear()
    create_cinematic_background(canvas)
    
    # Animated title with shadow and blink
    _show_animated_title(canvas)
    
    # Welcome message
    animate_text(
        canvas, f"Welcome, {name}!", WIDTH//2, HEIGHT//2+100, 
        QUESTION_FONT, 32, TEXT_COLOR, delay=0.03
    )
    animate_text(
        canvas, "Press any key to start", WIDTH//2, HEIGHT//2+150, 
        QUESTION_FONT, 24, ACCENT_COLOR, delay=0.02
    )
    
    # Loading dots
    _show_loading_dots(canvas)
    
    # Wait for keypress with timeout
    _wait_for_key_with_timeout(canvas, timeout=30)


def _show_animated_title(canvas):
    """Show animated title with blink effect."""
    draw_title_with_shadow(canvas, "MOVIE MANIA", WIDTH//2, HEIGHT//2)
    title_id = animate_text(
        canvas, "MOVIE MANIA", WIDTH//2, HEIGHT//2, 
        QUESTION_FONT, TITLE_FONT_SIZE, GLOW_COLOR, delay=0.03
    )
    blink_text(canvas, title_id, GLOW_COLOR, ACCENT_COLOR, times=3)


def _show_loading_dots(canvas):
    """Show loading dot animation."""
    for i in range(5):
        canvas.create_oval(
            WIDTH//2-50+i*20, HEIGHT//2+200, 
            WIDTH//2-30+i*20, HEIGHT//2+220, 
            color="gray", outline=GLOW_COLOR
        )
        time.sleep(0.25)  # Much slower dot animation


def show_prize_screen(canvas, question_num, prize_text, game_over=False, 
                     correct_answer=None):
    """
    Display prize won screen with animation.
    
    Args:
        canvas: Canvas object
        question_num: Number of questions answered
        prize_text: Prize description text
        game_over: Whether this is a game over (not all questions answered)
        correct_answer: Correct answer if game over
    """
    canvas.clear()
    create_cinematic_background(canvas)
    
    # Determine colors based on win/loss
    if game_over:
        outline_color = "orange"
        title = "GAME OVER"
        title_color = "orange"
    else:
        outline_color = GLOW_COLOR
        title = "🎉 CONGRATULATIONS! 🎉"
        title_color = ACCENT_COLOR
    
    # Prize panel
    canvas.create_rectangle(
        WIDTH//4, HEIGHT//4, 3*WIDTH//4, 3*HEIGHT//4, 
        color=PANEL_COLOR, outline=outline_color
    )
    canvas.create_rectangle(
        WIDTH//4+2, HEIGHT//4+2, 3*WIDTH//4-2, 3*HEIGHT//4-2, 
        outline=f"rgba(230,184,0,0.3)"
    )
    
    # Title
    canvas.create_text(
        WIDTH//2, HEIGHT//4 + 40, text=title, 
        font=QUESTION_FONT, font_size=32, 
        color=title_color, anchor="center"
    )
    
    # Score
    canvas.create_text(
        WIDTH//2, HEIGHT//2 - 40, 
        text=f"Questions Answered: {question_num}/8", 
        font=QUESTION_FONT, font_size=24, 
        color=TEXT_COLOR, anchor="center"
    )
    
    # Prize text
    canvas.create_text(
        WIDTH//2, HEIGHT//2 + 20, 
        text=f"Prize Won: {prize_text}", 
        font=QUESTION_FONT, font_size=28, 
        color=ACCENT_COLOR, anchor="center"
    )
    
    # Show correct answer if game over
    if game_over and correct_answer:
        canvas.create_text(
            WIDTH//2, HEIGHT//2 + 80, 
            text=f"Correct answer: {correct_answer}", 
            font=QUESTION_FONT, font_size=18, 
            color="gray", anchor="center"
        )
    
    # Click to continue message
    canvas.create_text(
        WIDTH//2, 3*HEIGHT//4 - 40, 
        text="Click to continue...", 
        font=QUESTION_FONT, font_size=18, 
        color=GLOW_COLOR, anchor="center"
    )
    
    time.sleep(0.5)


def show_game_over_screen(canvas, correct_answer):
    """
    Display game over screen with correct answer.
    
    Args:
        canvas: Canvas object
        correct_answer: The correct answer to display
    """
    canvas.clear()
    create_cinematic_background(canvas)
    
    # Game over panel
    canvas.create_rectangle(
        WIDTH//4, HEIGHT//4, 3*WIDTH//4, 3*HEIGHT//4, 
        color=PANEL_COLOR, outline="red"
    )
    canvas.create_rectangle(
        WIDTH//4+2, HEIGHT//4+2, 3*WIDTH//4-2, 3*HEIGHT//4-2, 
        outline="rgba(255,0,0,0.3)"
    )
    
    # Game over message
    animate_text(
        canvas, "GAME OVER", WIDTH//2, HEIGHT//3, 
        QUESTION_FONT, 48, "red", delay=0.06
    )
    animate_text(
        canvas, f"Correct answer was: {correct_answer}", 
        WIDTH//2, HEIGHT//2, QUESTION_FONT, 24, 
        TEXT_COLOR, delay=0.06
    )
    animate_text(
        canvas, "Better luck next time!", WIDTH//2, 2*HEIGHT//3, 
        QUESTION_FONT, 20, GLOW_COLOR, delay=0.06
    )
    time.sleep(3)


def _wait_for_key_with_timeout(canvas, timeout=30):
    """
    Wait for key press with timeout to prevent infinite loop.
    
    Args:
        canvas: Canvas object
        timeout: Timeout in seconds
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        keys = canvas.get_new_key_presses()
        if keys:
            time.sleep(0.5)
            break
        time.sleep(0.005)
    else:
        time.sleep(1)
