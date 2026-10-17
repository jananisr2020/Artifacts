# Tic-Tac-Toe: Human vs Smart AI

A fun command-line Tic-Tac-Toe game built with Python. Play against a friend or challenge an unbeatable computer opponent powered by the **Minimax algorithm**.

## Features

- Two game modes: Human vs AI and two-player mode
- Smart AI that chooses optimal moves using Minimax
- Input validation for occupied squares and invalid entries
- Clear 3×3 board display and win/draw detection
- Replay option after each round
- Unit tests using Python's built-in `unittest`
- No external packages required

## Requirements

- Python 3.9 or newer
- No third-party dependencies

## Run the game

```bash
git clone https://github.com/jananisr2020/Artifacts.git
cd Artifacts/python-tic-tac-toe-game
python main.py
```

On some systems, use `python3 main.py` instead.

## How to play

1. Choose **1** to play against the AI or **2** for two players.
2. Enter a number from **1 to 9** to select a square.
3. The board positions are:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Get three of your symbols in a row, column, or diagonal to win.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Concepts demonstrated

- Functions, loops, conditionals, and lists
- Input validation and separation of game logic from the interface
- Recursion and the Minimax decision-making algorithm
- Unit testing and clean project structure

## Project structure

```text
python-tic-tac-toe-game/
├── main.py
├── tic_tac_toe.py
├── tests/
│   └── test_tic_tac_toe.py
├── .gitignore
└── README.md
```

## Resume description

**Tic-Tac-Toe with Minimax AI | Python**  
Developed an interactive command-line game with Human-vs-AI and two-player modes. Implemented the Minimax algorithm for optimal AI moves, validated player input, handled win/draw states, and wrote unit tests using Python's standard library.
