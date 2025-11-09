"""
Question management for Movie Mania game.
"""

import random
from src.data.questions import QUESTIONS
from src.config import (
    EASY_QUESTIONS_COUNT, MEDIUM_QUESTIONS_COUNT, 
    HARD_QUESTIONS_COUNT
)


def select_game_questions():
    """
    Select questions for a game session.
    Selects 2 easy, 3 medium, 3 hard questions, ordered by difficulty.
    
    Returns:
        list: Selected questions ordered by difficulty
    
    Raises:
        ValueError: If insufficient questions in any category
    """
    easy = [q for q in QUESTIONS if q['difficulty'] == 'easy']
    medium = [q for q in QUESTIONS if q['difficulty'] == 'medium']
    hard = [q for q in QUESTIONS if q['difficulty'] == 'hard']
    
    if (len(easy) < EASY_QUESTIONS_COUNT or 
        len(medium) < MEDIUM_QUESTIONS_COUNT or 
        len(hard) < HARD_QUESTIONS_COUNT):
        raise ValueError("Insufficient questions in one or more categories")
    
    selected = (
        random.sample(easy, EASY_QUESTIONS_COUNT) +
        random.sample(medium, MEDIUM_QUESTIONS_COUNT) +
        random.sample(hard, HARD_QUESTIONS_COUNT)
    )
    
    # Sort by difficulty
    difficulty_order = {'easy': 1, 'medium': 2, 'hard': 3}
    selected.sort(key=lambda x: difficulty_order[x['difficulty']])
    
    return selected


def shuffle_question_options(question):
    """
    Shuffle answer options and update answer letter accordingly.
    
    Args:
        question: Question dictionary to shuffle
    
    Returns:
        dict: Question with shuffled options and updated answer_letter
    """
    # Keep original options before shuffling
    original_options = question["options"].copy()
    options = question["options"].copy()
    random.shuffle(options)
    
    # Find new position of correct answer
    new_answer_index = options.index(question["answer"])
    question["options"] = options
    question["answer_letter"] = chr(ord('A') + new_answer_index)
    
    # Rearrange audience poll data to match new order
    new_audience = [0] * len(options)
    for i, opt in enumerate(options):
        old_index = original_options.index(opt)
        new_audience[i] = question["audience"][old_index]
    question["audience"] = new_audience
    
    return question


def get_prize_text(question_num):
    """
    Get prize text for a given question number.
    
    Args:
        question_num: Number of questions answered (0-8)
    
    Returns:
        str: Prize description text
    """
    from src.config import PRIZE_VALUES
    
    prizes = {
        0: "$0 - Thanks for playing!",
        1: "$500",
        2: "$1,000",
        3: "$5,000",
        4: "$10,000",
        5: "$50,000",
        6: "$100,000",
        7: "$250,000",
        8: "$1,000,000 - You're a Millionaire!"
    }
    
    return prizes.get(question_num, "$0")
