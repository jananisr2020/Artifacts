"""Game logic for Tic-Tac-Toe, including a Minimax-powered AI."""

from math import inf
from typing import List, Optional

Board = List[str]
EMPTY = " "


def new_board() -> Board:
    """Return an empty board containing nine squares."""
    return [EMPTY] * 9


def available_moves(board: Board) -> List[int]:
    """Return indexes of all unoccupied squares."""
    return [index for index, square in enumerate(board) if square == EMPTY]


def winner(board: Board) -> Optional[str]:
    """Return 'X' or 'O' if that player won, otherwise None."""
    winning_lines = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )
    for a, b, c in winning_lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: Board) -> bool:
    """Return True when the board is full and nobody has won."""
    return winner(board) is None and EMPTY not in board


def make_move(board: Board, position: int, symbol: str) -> bool:
    """Place a symbol in a zero-based position; return False if invalid."""
    if symbol not in ("X", "O"):
        raise ValueError("Symbol must be 'X' or 'O'.")
    if position not in range(9) or board[position] != EMPTY:
        return False
    board[position] = symbol
    return True


def minimax(board: Board, maximizing: bool, ai_symbol: str, human_symbol: str) -> int:
    """Score a position recursively: AI win=1, draw=0, human win=-1."""
    result = winner(board)
    if result == ai_symbol:
        return 1
    if result == human_symbol:
        return -1
    if EMPTY not in board:
        return 0

    if maximizing:
        best_score = -inf
        for position in available_moves(board):
            board[position] = ai_symbol
            score = minimax(board, False, ai_symbol, human_symbol)
            board[position] = EMPTY
            best_score = max(best_score, score)
        return int(best_score)

    best_score = inf
    for position in available_moves(board):
        board[position] = human_symbol
        score = minimax(board, True, ai_symbol, human_symbol)
        board[position] = EMPTY
        best_score = min(best_score, score)
    return int(best_score)


def best_move(board: Board, ai_symbol: str = "O", human_symbol: str = "X") -> int:
    """Choose an optimal move for the AI; ties are resolved by board order."""
    if ai_symbol not in ("X", "O") or human_symbol not in ("X", "O"):
        raise ValueError("Symbols must be 'X' or 'O'.")
    if ai_symbol == human_symbol:
        raise ValueError("AI and human symbols must be different.")
    if winner(board) is not None or is_draw(board):
        raise ValueError("No moves are available in a finished game.")

    best_score = -inf
    choice = -1
    for position in available_moves(board):
        board[position] = ai_symbol
        score = minimax(board, False, ai_symbol, human_symbol)
        board[position] = EMPTY
        if score > best_score:
            best_score = score
            choice = position
    return choice


def format_board(board: Board) -> str:
    """Render the board with numbered hints for empty squares."""
    if len(board) != 9:
        raise ValueError("A Tic-Tac-Toe board must contain exactly nine squares.")
    cells = [
        str(index + 1) if value == EMPTY else value
        for index, value in enumerate(board)
    ]
    return (
        f" {cells[0]} | {cells[1]} | {cells[2]}\n"
        "---+---+---\n"
        f" {cells[3]} | {cells[4]} | {cells[5]}\n"
        "---+---+---\n"
        f" {cells[6]} | {cells[7]} | {cells[8]}"
    )
