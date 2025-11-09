"""
Lifeline functionality for Movie Mania game.
"""

import time
import random
from src.config import (
    WIDTH, HEIGHT, BAR_COLOR, GLOW_COLOR, 
    ACCENT_COLOR, QUESTION_FONT
)
from src.ui.animations import animate_text, fade_out_text


def use_50_50_lifeline(canvas, correct_letter, answer_ids):
    """
    Implement 50/50 lifeline - eliminate two wrong answers.
    
    Args:
        canvas: Canvas object
        correct_letter: Letter of correct answer
        answer_ids: Dictionary mapping letters to text IDs
    """
    # Only use letters that actually exist in answer_ids
    available_letters = list(answer_ids.keys())
    wrong_choices = [c for c in available_letters if c != correct_letter]
    eliminated = random.sample(wrong_choices, min(2, len(wrong_choices)))
    
    for letter in eliminated:
        # Instant elimination - no animation
        canvas.change_text(answer_ids[letter], f"{letter}: ---")
        canvas.set_color(answer_ids[letter], "gray")


def use_phone_friend_lifeline(canvas, question):
    """
    Implement phone a friend lifeline - show friend's suggestion.
    
    Args:
        canvas: Canvas object
        question: Question dictionary with options and answer
    
    Returns:
        text_id: ID of the displayed message
    """
    choices = question["options"]
    correct_answer = question["answer"]
    
    # Friend has 80% chance of being correct
    weights = [
        0.8 if choice == correct_answer else 0.2/(len(choices)-1) 
        for choice in choices
    ]
    friend_choice = random.choices(choices, weights=weights, k=1)[0]
    
    # Display panel
    _draw_phone_panel(canvas)
    
    # Display text instantly - no animation
    text_id = canvas.create_text(
        WIDTH//2, HEIGHT-125, text=f"📞 Friend says: {friend_choice}", 
        font=QUESTION_FONT, font_size=18, 
        color=ACCENT_COLOR, anchor="center"
    )
    
    return text_id


def _draw_phone_panel(canvas):
    """Draw phone a friend panel."""
    canvas.create_rectangle(
        WIDTH//4, HEIGHT-150, 3*WIDTH//4, HEIGHT-100, 
        color=BAR_COLOR, outline=GLOW_COLOR
    )
    canvas.create_rectangle(
        WIDTH//4, HEIGHT-150, 3*WIDTH//4, HEIGHT-125, 
        color="#2a4a6a"
    )
    canvas.create_rectangle(
        WIDTH//4+2, HEIGHT-148, 3*WIDTH//4-2, HEIGHT-102, 
        outline="rgba(230,184,0,0.3)"
    )


def use_audience_poll_lifeline(canvas, question, correct_letter):
    """
    Implement audience poll lifeline - show poll results.
    
    Args:
        canvas: Canvas object
        question: Question dictionary
        correct_letter: Letter of correct answer
    
    Returns:
        tuple: (bar_ids, text_ids, title_id)
    """
    letters = ['A', 'B', 'C', 'D']
    correct_index = ord(correct_letter) - ord('A')
    
    # Generate audience poll data (90% chance correct answer is highest)
    audience_data = _generate_audience_data(
        len(question["options"]), 
        correct_index
    )
    
    # Display poll results
    return _draw_audience_poll(canvas, audience_data, letters)


def _generate_audience_data(num_options, correct_index):
    """Generate realistic audience poll percentages."""
    correct_highest = random.random() < 0.9
    audience_data = [0] * num_options
    
    if correct_highest:
        audience_data[correct_index] = random.randint(60, 80)
        remaining = 100 - audience_data[correct_index]
        non_correct = [i for i in range(num_options) if i != correct_index]
        for i in non_correct[:-1]:
            audience_data[i] = random.randint(0, min(20, remaining))
            remaining -= audience_data[i]
        audience_data[non_correct[-1]] = remaining
    else:
        incorrect_index = random.choice(
            [i for i in range(num_options) if i != correct_index]
        )
        audience_data[incorrect_index] = random.randint(50, 70)
        remaining = 100 - audience_data[incorrect_index]
        audience_data[correct_index] = random.randint(20, min(40, remaining))
        remaining -= audience_data[correct_index]
        other_indices = [
            i for i in range(num_options) 
            if i not in [correct_index, incorrect_index]
        ]
        for i in other_indices[:-1]:
            audience_data[i] = random.randint(0, min(15, remaining))
            remaining -= audience_data[i]
        if other_indices:
            audience_data[other_indices[-1]] = remaining
    
    return audience_data


def _draw_audience_poll(canvas, audience_data, letters):
    """Draw audience poll results panel."""
    _draw_audience_panel(canvas)
    
    title_id = canvas.create_text(
        WIDTH//2, HEIGHT-180, text="🎬 Audience Poll Results", 
        font=QUESTION_FONT, font_size=14, 
        color="#f0f0f0", anchor="center"
    )
    
    # Animated bars
    bar_ids, text_ids = _draw_audience_bars(canvas, audience_data, letters)
    
    return bar_ids, text_ids, title_id


def _draw_audience_panel(canvas):
    """Draw audience poll panel background."""
    canvas.create_rectangle(
        WIDTH//3, HEIGHT-200, 2*WIDTH//3, HEIGHT-80, 
        color=BAR_COLOR, outline=GLOW_COLOR
    )
    canvas.create_rectangle(
        WIDTH//3, HEIGHT-200, 2*WIDTH//3, HEIGHT-150, 
        color="#2a4a6a"
    )
    canvas.create_rectangle(
        WIDTH//3+2, HEIGHT-198, 2*WIDTH//3-2, HEIGHT-82, 
        outline="rgba(230,184,0,0.3)"
    )


def _draw_audience_bars(canvas, audience_data, letters):
    """Draw audience poll bars instantly."""
    bar_ids = []
    text_ids = []
    bar_spacing = (WIDTH//3) // (len(audience_data) + 1)
    
    for i, percentage in enumerate(audience_data):
        x = WIDTH//3 + (i + 0.5) * bar_spacing
        y = HEIGHT-100
        bar_height = percentage * 0.7
        
        # Draw full bar instantly - no animation
        bar_ids.append(
            canvas.create_rectangle(
                x-20, y-bar_height, x+20, y, color=GLOW_COLOR
            )
        )
        
        text_ids.append(
            canvas.create_text(
                x, y-10-bar_height, 
                text=f"{letters[i]}: {percentage}%", 
                font=QUESTION_FONT, font_size=12, 
                color=ACCENT_COLOR, anchor="center"
            )
        )
    
    return bar_ids, text_ids
