from typing import List, Literal


def move_train(
    board: List[str], mov: Literal["U", "D", "R", "L"]
) -> Literal["none", "crash", "eat"]:
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    for i, row in enumerate(board):
        if "@" in row:
            train_row, train_col = i, row.index("@")
            break
    new_row, new_col = train_row + directions[mov][0], train_col + directions[mov][1]
    if board[new_row].get(new_col, False) == "*":
        return "eat"
    elif board[new_row][new_col] == "·":
        return "none"

    return "crash"


if __name__ == "__main__":
    board = ["·····", "*····", "@····", "o····", "o····"]
    result = move_train(board, "U")
    result = move_train(board, "D")
    result = move_train(board, "L")
    result = move_train(board, "R")

    board = ["·····", "·····", "·····", "o····", "@····"]
    result = move_train(board, "D")
