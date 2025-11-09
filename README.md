<div align="center">
  <h1>🎬 Movie Mania 🎬</h1>
  <p><strong>A Cinematic Movie Trivia Quiz Game</strong></p>
  <p>Final Project for Stanford Code in Place 2025</p>
  
  [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
  [![Course](https://img.shields.io/badge/Stanford-Code%20in%20Place-red.svg)](https://codeinplace.stanford.edu/)
</div>

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

---

## 🎯 About

**Movie Mania** is an interactive trivia game inspired by "Who Wants to Be a Millionaire?" designed and developed as the final project for [Stanford's Code in Place](https://codeinplace.stanford.edu/) course. The game challenges players with movie-related questions across varying difficulty levels, offering an engaging experience with lifelines, a timer system, and a dynamic leaderboard.

This project demonstrates proficiency in:
- Object-oriented programming
- Event-driven programming
- GUI development with custom graphics library
- Modular architecture and clean code practices
- Data structures and algorithms

---

## ✨ Features

### 🎮 Core Gameplay
- **100+ Movie Trivia Questions** - Covering various genres and difficulty levels
- **Progressive Difficulty** - 2 easy, 3 medium, 3 hard questions per game
- **30-Second Timer** - Adds pressure and excitement to each question
- **Prize System** - Win from $500 to $1,000,000!

### 🆘 Lifelines (3 Available)
1. **50/50** - Eliminates two wrong answers
2. **Phone a Friend** - Get a suggestion (80% accuracy)
3. **Audience Poll** - See what the audience thinks

### 🎨 Visual Features
- Custom-built graphics library (Stanford CS106A compatible)
- Cinematic background with starry effects
- Smooth animations and visual feedback
- Professional UI with progress bars

### 📊 Additional Features
- **Leaderboard System** - Tracks top scores
- **Randomized Questions** - Shuffled options for replay value
- **Instant Feedback** - Quick response to player actions
- **Prize Display** - Shows winnings even for partial completion

---

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- tkinter library (usually comes with Python)

### Linux/Ubuntu
```bash
# Install tkinter if not already installed
sudo apt-get update
sudo apt-get install python3-tk

# Clone the repository
git clone https://github.com/yourusername/movie_mania.git
cd movie_mania

# Run the game
python3 main.py
```

### macOS
```bash
# tkinter comes pre-installed with Python on macOS
# Clone and run
git clone https://github.com/yourusername/movie_mania.git
cd movie_mania
python3 main.py
```

### Windows
```bash
# tkinter comes with Python installer
# Clone and run
git clone https://github.com/yourusername/movie_mania.git
cd movie_mania
python main.py
```

---

## 🎮 Usage

### Starting the Game

```bash
python3 main.py
```

### How to Play

1. **Enter Your Name**
   - Type your name (max 15 characters)
   - Press `Enter` to continue

2. **Answer Questions**
   - Press `A`, `B`, `C`, or `D` to select an answer
   - You have 30 seconds per question

3. **Use Lifelines** (Optional)
   - Press `1` for 50/50
   - Press `2` for Phone a Friend
   - Press `3` for Audience Poll
   - Each lifeline can only be used once

4. **Goal**
   - Answer all 8 questions correctly
   - Win $1,000,000!
   - Prize is awarded based on questions answered

### Controls

| Key | Action |
|-----|--------|
| `A` | Select answer A |
| `B` | Select answer B |
| `C` | Select answer C |
| `D` | Select answer D |
| `1` | Use 50/50 lifeline |
| `2` | Use Phone a Friend lifeline |
| `3` | Use Audience Poll lifeline |
| `Enter` | Confirm name input |
| `Backspace` | Delete character (name entry) |
| `Mouse Click` | Continue/Close screens |

---

## 📖 Game Rules

### Question Structure
- **Total Questions:** 8 per game
- **Difficulty Distribution:**
  - Questions 1-2: Easy
  - Questions 3-5: Medium
  - Questions 6-8: Hard

### Prize Ladder
| Questions Answered | Prize Amount |
|-------------------|--------------|
| 1 | $500 |
| 2 | $1,000 |
| 3 | $5,000 |
| 4 | $10,000 |
| 5 | $50,000 |
| 6 | $100,000 |
| 7 | $250,000 |
| 8 | **$1,000,000** 🎉 |

### Winning Conditions
- Answer all 8 questions correctly to win the grand prize
- Prize is awarded for partial completion (you keep what you earned)
- Game ends on wrong answer or timeout

---

## 📁 Project Structure

```
movie_mania/
├── main.py                      # Entry point
├── README.md                    # This file
├── leaderboard.json            # High scores (auto-generated)
│
├── graphics/                    # Custom graphics library
│   ├── __init__.py
│   ├── canvas.py               # Canvas class (203 lines, 17 methods)
│   ├── drawing.py              # Shape/text drawing (4 functions)
│   ├── input.py                # Keyboard/mouse input (4 functions)
│   └── utils.py                # Color utilities (3 functions)
│
└── src/                        # Game source code
    ├── config.py               # Game constants & settings
    │
    ├── data/
    │   └── questions.py        # 100 trivia questions
    │
    ├── game/                   # Core game logic
    │   ├── input.py            # Player input handling
    │   ├── leaderboard.py      # High score system
    │   ├── lifelines.py        # Lifeline implementations
    │   ├── questions.py        # Question management
    │   └── quiz.py             # Main game loop
    │
    └── ui/                     # User interface
        ├── animations.py       # Visual effects
        ├── graphics.py         # UI components
        ├── screens.py          # Game screens
        └── timer.py            # Timer display
```

---

## 🔧 Technical Details

### Architecture
- **Modular Design**: Separation of concerns across graphics, game logic, and UI
- **Custom Graphics Library**: Built from scratch using tkinter, compatible with Stanford CS106A API
- **Event-Driven**: Responsive to keyboard and mouse events
- **Data-Driven**: Questions stored in structured format for easy expansion

### Code Standards
- **Function Limits**: 
  - `graphics/`: Maximum 60 lines per function
  - `src/`: Maximum 40 lines per function
- **File Organization**: Maximum 6 functions per file (except data files)
- **Clean Code**: Descriptive names, comprehensive docstrings, clear structure

### Performance Optimizations
- Instant question display (no slow animations)
- Fast lifeline responses
- Smooth timer updates without flickering
- Efficient canvas rendering

### Technologies Used
- **Language**: Python 3.6+
- **GUI**: tkinter
- **Graphics**: Custom library built on tkinter Canvas
- **Data Storage**: JSON (for leaderboard)
- **Design Pattern**: MVC-inspired architecture

---

## 👤 Author

**Nobu**
- Stanford Code in Place Student
- Final Project: Movie Mania
- Course: [Code in Place 2024](https://codeinplace.stanford.edu/)

---

## 🙏 Acknowledgments

- **Stanford Code in Place** - For the excellent course and teaching materials
- **Stanford CS106A** - For the graphics library inspiration
- **"Who Wants to Be a Millionaire?"** - For the game concept and format
- **Instructors and Section Leaders** - For guidance and support throughout the course

---

## 📜 License

This project is part of Stanford Code in Place coursework. Please refer to Stanford's academic policies regarding code sharing and usage.

---

<div align="center">
  <p><strong>Developed with ❤️ as part of Stanford Code in Place</strong></p>
  <p>🎬 Enjoy the game! 🍿</p>
  
  [![Stanford](https://img.shields.io/badge/Stanford-Code%20in%20Place-red.svg)](https://codeinplace.stanford.edu/)
</div>
