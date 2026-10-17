"""Interactive command-line interface for Tic-Tac-Toe."""

from tic_tac_toe import best_move, format_board, is_draw, make_move, new_board, winner


def ask_mode() -> str:
    """Ask for a valid game mode."""
    while True:
        choice = input("Choose mode: 1) Play against AI  2) Two players: ").strip()
        if choice in ("1", "2"):
            return choice
        print("Please enter 1 or 2.")


def ask_position(board: list[str], symbol: str) -> int:
    """Read a legal square number from the current player."""
    while True:
        raw = input(f"Player {symbol}, choose a square (1-9): ").strip()
        try:
            position = int(raw) - 1
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue
        if make_move(board, position, symbol):
            return position
        print("That square is unavailable. Choose an empty square from 1 to 9.")


def play_round(mode: str) -> None:
    """Run one complete round."""
    board = new_board()
    current = "X"
    print("\nBoard positions:")
    print(format_board(board))

    while winner(board) is None and not is_draw(board):
        if mode == "1" and current == "O":
            position = best_move(board, ai_symbol="O", human_symbol="X")
            make_move(board, position, "O")
            print(f"AI chooses square {position + 1}.")
        else:
            ask_position(board, current)

        print()
        print(format_board(board))
        if winner(board) is not None or is_draw(board):
            break
        current = "O" if current == "X" else "X"

    result = winner(board)
    if result:
        print(f"\nPlayer {result} wins!")
    else:
        print("\nIt's a draw!")


def main() -> None:
    print("=" * 34)
    print("       TIC-TAC-TOE")
    print("=" * 34)
    while True:
        mode = ask_mode()
        play_round(mode)
        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing. See you next time!")
            break


if __name__ == "__main__":
    main()
