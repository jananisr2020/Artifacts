"""Unit tests for Tic-Tac-Toe game logic."""

import unittest

from tic_tac_toe import (
    best_move,
    format_board,
    is_draw,
    make_move,
    new_board,
    winner,
)


class TicTacToeTests(unittest.TestCase):
    def test_new_board_has_nine_empty_squares(self):
        self.assertEqual(new_board(), [" "] * 9)

    def test_move_rejects_occupied_or_out_of_range_square(self):
        board = new_board()
        self.assertTrue(make_move(board, 0, "X"))
        self.assertFalse(make_move(board, 0, "O"))
        self.assertFalse(make_move(board, 9, "O"))
        self.assertFalse(make_move(board, -1, "O"))

    def test_rejects_invalid_symbol(self):
        with self.assertRaises(ValueError):
            make_move(new_board(), 0, "A")

    def test_detects_row_win(self):
        self.assertEqual(winner(["X", "X", "X", "O", " ", "O", " ", " ", " "]), "X")

    def test_detects_column_win(self):
        self.assertEqual(winner(["O", "X", " ", "O", "X", " ", " ", "X", " "]), "X")

    def test_detects_diagonal_win(self):
        self.assertEqual(winner(["O", " ", "X", " ", "X", " ", "X", "O", "O"]), "X")

    def test_detects_draw(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(is_draw(board))
        self.assertIsNone(winner(board))

    def test_ai_takes_winning_move(self):
        board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
        self.assertEqual(best_move(board), 2)

    def test_ai_blocks_human_winning_move(self):
        board = ["X", "X", " ", "O", " ", " ", " ", " ", "O"]
        self.assertEqual(best_move(board), 2)

    def test_ai_never_changes_board_while_thinking(self):
        board = ["X", " ", " ", " ", "O", " ", " ", " ", " "]
        original = board.copy()
        best_move(board)
        self.assertEqual(board, original)

    def test_board_display_contains_square_numbers(self):
        display = format_board(new_board())
        for number in "123456789":
            self.assertIn(number, display)


if __name__ == "__main__":
    unittest.main()
