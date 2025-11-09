"""
Movie Mania - A trivia quiz game about movies.
Main entry point for the game.
"""

from graphics import Canvas
from src.config import WIDTH, HEIGHT, PRIZE_VALUES, TOTAL_QUESTIONS
from src.ui.screens import show_splash_screen
from src.game.input import get_player_name
from src.game.questions import select_game_questions, shuffle_question_options
from src.game.quiz import run_quiz_game
from src.game.leaderboard import save_to_leaderboard, display_leaderboard


def main():
    """
    Main entry point for Movie Mania game.
    Orchestrates game flow from start to finish.
    """
    # Initialize canvas
    canvas = Canvas(WIDTH, HEIGHT)
    
    # Get player name
    player_name = get_player_name(canvas)
    
    # Show splash screen
    show_splash_screen(canvas, player_name)
    
    # Select and prepare questions
    selected_questions = select_game_questions()
    selected_questions = [
        shuffle_question_options(q.copy()) 
        for q in selected_questions
    ]
    
    # Run the quiz game
    final_score = run_quiz_game(canvas, selected_questions)
    
    # Handle game completion
    if final_score == TOTAL_QUESTIONS:
        # Winner - save to leaderboard and display
        prize_amount = PRIZE_VALUES[final_score]
        save_to_leaderboard(player_name, prize_amount)
        display_leaderboard(canvas)
    else:
        # Did not complete - just wait for click
        canvas.wait_for_click()


if __name__ == '__main__':
    main()
