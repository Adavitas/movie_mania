"""
Configuration file for Movie Mania game.
Contains all constants for display, colors, fonts, and game settings.
"""

# Display dimensions
WIDTH = 800
HEIGHT = 800

# Font settings
QUESTION_FONT = "Arial"
TITLE_FONT_SIZE = 48
QUESTION_FONT_SIZE = 24
ANSWER_FONT_SIZE = 20
TIMER_FONT_SIZE = 20

# Color scheme
GLOW_COLOR = "#e6b800"  # Soft gold
ACCENT_COLOR = "#00b7b7"  # Vibrant teal
BACKGROUND_COLOR = "#0a1a2a"  # Deep navy
TEXT_COLOR = "#f0f0f0"  # Bright white
PANEL_COLOR = "#1e2a3a"  # Dark slate
BAR_COLOR = "#1a3c5a"  # Rich blue
TIMER_TEXT_COLOR = "#ff0000"  # Red for timer

# Game settings
TIMER_DURATION = 30  # seconds
MAX_NAME_LENGTH = 15
LEADERBOARD_FILE = "leaderboard.json"
LEADERBOARD_TOP_N = 10
LEADERBOARD_DISPLAY_N = 5

# Question distribution
EASY_QUESTIONS_COUNT = 2
MEDIUM_QUESTIONS_COUNT = 3
HARD_QUESTIONS_COUNT = 3
TOTAL_QUESTIONS = EASY_QUESTIONS_COUNT + MEDIUM_QUESTIONS_COUNT + HARD_QUESTIONS_COUNT

# Prize values
PRIZE_VALUES = {
    0: 0,
    1: 500,
    2: 1000,
    3: 5000,
    4: 10000,
    5: 50000,
    6: 100000,
    7: 250000,
    8: 1000000
}

# Animation settings
TEXT_ANIMATION_DELAY = 0.1  # Much slower typewriter effect
TITLE_ANIMATION_DELAY = 0.15  # Much slower title animation
BLINK_DURATION = 0.6  # Longer blink duration
FADE_STEP = 3  # Much slower fade effect - smaller steps
