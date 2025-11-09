"""
Main quiz game loop for Movie Mania.
"""

import time
from graphics import Canvas
from src.config import (
    WIDTH, HEIGHT, TIMER_DURATION, PRIZE_VALUES, 
    QUESTION_FONT, TEXT_COLOR, GLOW_COLOR, BLINK_DURATION
)
from src.ui.graphics import (
    create_cinematic_background, draw_progress_bar, 
    draw_title_with_shadow, draw_answer_options
)
from src.ui.timer import (
    create_timer_display, update_timer_display, flash_timer_timeout
)
from src.ui.screens import show_prize_screen, show_game_over_screen
from src.ui.animations import animate_text, blink_text
from src.game.lifelines import (
    use_50_50_lifeline, use_phone_friend_lifeline, 
    use_audience_poll_lifeline
)
from src.game.input import (
    wait_for_answer_or_lifeline, highlight_selected_answer,
    show_correct_answer_effect
)
from src.game.questions import get_prize_text


def run_quiz_game(canvas, selected_questions):
    """
    Run the main quiz game loop.
    
    Args:
        canvas: Canvas object
        selected_questions: List of questions for the game
    
    Returns:
        int: Final score (number of correct answers)
    """
    lifelines = {"5050": False, "phone": False, "audience": False}
    score = 0
    
    for i, question in enumerate(selected_questions):
        result = play_question(canvas, question, i, lifelines)
        
        if result == "correct":
            score += 1
            # No extra wait - already waited in _handle_answer
        elif result == "wrong":
            # Show prize for partial completion
            prize_text = get_prize_text(score)
            show_prize_screen(canvas, score, prize_text, game_over=True, 
                            correct_answer=question['answer'])
            canvas.wait_for_click()
            return score
        elif result == "timeout":
            # Show prize for partial completion
            prize_text = get_prize_text(score)
            show_prize_screen(canvas, score, prize_text, game_over=True, 
                            correct_answer=question['answer'])
            canvas.wait_for_click()
            return score
    
    # All questions answered correctly - WINNER!
    prize_text = get_prize_text(score)
    show_prize_screen(canvas, score, prize_text, game_over=False)
    return score


def play_question(canvas, question, question_index, lifelines):
    """
    Display and handle a single question.
    
    Args:
        canvas: Canvas object
        question: Question dictionary
        question_index: Index of current question
        lifelines: Dictionary of lifeline usage status
    
    Returns:
        str: Result - "correct", "wrong", or "timeout"
    """
    # Setup display
    correct_letter = question['answer_letter']
    correct_answer = question['answer']
    time_left_id = create_timer_display(canvas)
    audience_elements = ([], [], None)
    phone_text_id = None
    
    # Draw question UI
    answer_ids = _draw_question_ui(canvas, question, question_index, lifelines)
    
    # Question loop
    return _question_loop(
        canvas, question, correct_letter, correct_answer,
        answer_ids, lifelines, time_left_id, 
        False, audience_elements, phone_text_id
    )


def _draw_question_ui(canvas, question, question_index, lifelines):
    """Draw question UI elements."""
    canvas.clear()
    create_cinematic_background(canvas)
    draw_progress_bar(canvas, question_index+1, 8)
    draw_title_with_shadow(canvas, "MOVIE MANIA", WIDTH//2, 80)
    
    canvas.create_text(
        WIDTH//2, 120, text=f"Genre: {question['genre']}", 
        font=QUESTION_FONT, font_size=20, 
        color=TEXT_COLOR, anchor="center"
    )
    
    # Display question instantly - no animation
    canvas.create_text(
        WIDTH//2, 180, text=f"Q{question_index+1}: {question['question']}", 
        font=QUESTION_FONT, font_size=24, 
        color=TEXT_COLOR, anchor="center"
    )
    
    answer_ids = draw_answer_options(canvas, question["options"])
    _draw_lifeline_menu(canvas, lifelines)
    
    return answer_ids


def _draw_lifeline_menu(canvas, lifelines):
    """Draw available lifelines menu."""
    lifeline_text = []
    if not lifelines["5050"]:
        lifeline_text.append("1: 50/50")
    if not lifelines["phone"]:
        lifeline_text.append("2: Phone a Friend")
    if not lifelines["audience"]:
        lifeline_text.append("3: Audience Poll")
    
    lifeline_id = canvas.create_text(
        WIDTH//2, HEIGHT-50, text=" | ".join(lifeline_text), 
        font=QUESTION_FONT, font_size=18, 
        color=GLOW_COLOR, anchor="center"
    )
    
    blink_text(canvas, lifeline_id, GLOW_COLOR, "#00b7b7", times=2)
    return lifeline_id


def _question_loop(canvas, question, correct_letter, correct_answer,
                   answer_ids, lifelines, time_left_id, 
                   audience_active, audience_elements, phone_text_id):
    """Main question timing and input loop."""
    time_left = TIMER_DURATION
    start_time = time.time()
    
    while time_left > 0:
        # Check for input
        key = wait_for_answer_or_lifeline(canvas, lifelines)
        
        if key in ['A', 'B', 'C', 'D']:
            return _handle_answer(
                canvas, key, correct_letter, correct_answer,
                audience_elements, phone_text_id
            )
        elif key in ['1', '2', '3']:
            audience_active, audience_elements, phone_text_id = _handle_lifeline(
                canvas, key, question, correct_letter, 
                answer_ids, lifelines, audience_elements, phone_text_id
            )
        
        # Update timer
        time_left = max(0, TIMER_DURATION - int(time.time() - start_time))
        update_timer_display(canvas, time_left_id, time_left)
        time.sleep(0.005)
    
    # Timeout
    _cleanup_lifeline_displays(canvas, audience_elements, phone_text_id)
    flash_timer_timeout(canvas, time_left_id)
    return "timeout"


def _handle_answer(canvas, key, correct_letter, correct_answer,
                   audience_elements, phone_text_id):
    """Handle answer selection."""
    highlight_selected_answer(canvas, key)
    _cleanup_lifeline_displays(canvas, audience_elements, phone_text_id)
    
    if key == correct_letter:
        show_correct_answer_effect(canvas)
        time.sleep(0.3)  # Very brief pause to see correct answer
        return "correct"
    else:
        return "wrong"


def _handle_lifeline(canvas, key, question, correct_letter, 
                     answer_ids, lifelines, audience_elements, phone_text_id):
    """Handle lifeline usage."""
    if key == '1':
        use_50_50_lifeline(canvas, correct_letter, answer_ids)
        lifelines["5050"] = True
    elif key == '2':
        phone_text_id = use_phone_friend_lifeline(canvas, question)
        lifelines["phone"] = True
    elif key == '3':
        audience_elements = use_audience_poll_lifeline(
            canvas, question, correct_letter
        )
        lifelines["audience"] = True
        return True, audience_elements, phone_text_id
    
    return False, audience_elements, phone_text_id


def _cleanup_lifeline_displays(canvas, audience_elements, phone_text_id):
    """Clean up lifeline display elements."""
    bar_ids, text_ids, title_id = audience_elements
    for bid in bar_ids:
        canvas.delete(bid)
    for tid in text_ids:
        canvas.delete(tid)
    if title_id:
        canvas.delete(title_id)
    if phone_text_id:
        canvas.delete(phone_text_id)
