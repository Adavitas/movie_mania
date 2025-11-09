"""
Leaderboard management for Movie Mania game.
"""

import json
import os
from datetime import datetime
from src.config import (
    LEADERBOARD_FILE, LEADERBOARD_TOP_N, LEADERBOARD_DISPLAY_N,
    WIDTH, HEIGHT, PANEL_COLOR, GLOW_COLOR, ACCENT_COLOR, 
    TEXT_COLOR, QUESTION_FONT
)
from src.ui.graphics import create_cinematic_background
from src.ui.animations import animate_text


def save_to_leaderboard(name, score):
    """
    Save winner's name, score, and timestamp to leaderboard.
    
    Args:
        name: Player name
        score: Final score/prize amount
    """
    leaderboard = _load_leaderboard()
    
    # Add new entry with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    leaderboard.append({
        "name": name, 
        "score": score, 
        "timestamp": timestamp
    })
    
    # Sort by score (descending) and keep top entries
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:LEADERBOARD_TOP_N]
    
    # Save updated leaderboard
    _save_leaderboard(leaderboard)


def display_leaderboard(canvas):
    """
    Display top leaderboard scores with timestamps.
    
    Args:
        canvas: Canvas object
    """
    leaderboard = _load_leaderboard()
    
    canvas.clear()
    create_cinematic_background(canvas)
    
    # Leaderboard panel
    canvas.create_rectangle(
        WIDTH//4, HEIGHT//4, 3*WIDTH//4, 3*HEIGHT//4, 
        color=PANEL_COLOR, outline=GLOW_COLOR
    )
    
    # Title
    animate_text(
        canvas, "Leaderboard - Top 5", WIDTH//2, HEIGHT//4+50, 
        QUESTION_FONT, 36, ACCENT_COLOR, delay=0.03
    )
    
    # Display entries
    _show_leaderboard_entries(canvas, leaderboard)
    
    # Exit instruction
    animate_text(
        canvas, "Click to exit", WIDTH//2, 3*HEIGHT//4-50, 
        QUESTION_FONT, 18, GLOW_COLOR, delay=0.02
    )
    canvas.wait_for_click()


def _show_leaderboard_entries(canvas, leaderboard):
    """Display leaderboard entries or empty message."""
    if not leaderboard:
        animate_text(
            canvas, "No winners yet!", WIDTH//2, HEIGHT//2, 
            QUESTION_FONT, 24, TEXT_COLOR, delay=0.03
        )
    else:
        for i, entry in enumerate(leaderboard[:LEADERBOARD_DISPLAY_N]):
            text = (
                f"{i+1}. {entry['name']}: ${entry['score']:,} "
                f"({entry.get('timestamp', 'Unknown')})"
            )
            animate_text(
                canvas, text, WIDTH//2, HEIGHT//2+i*50, 
                QUESTION_FONT, 20, TEXT_COLOR, delay=0.02
            )


def _load_leaderboard():
    """Load leaderboard from file."""
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading leaderboard: {e}")
        return []


def _save_leaderboard(leaderboard):
    """Save leaderboard to file."""
    try:
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(leaderboard, f, indent=2)
    except IOError as e:
        print(f"Error saving leaderboard: {e}")
