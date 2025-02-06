import pytest
from solutions.day_9_tren_magico import move_train

board = ["······", "·*····", "·@····", "·o····", "·o····"]


def test_move_train_1():
    assert move_train(board, "U") == "eat"


def test_move_train_2():
    assert move_train(board, "D") == "crash"


def test_move_train_3():
    assert move_train(board, "L") == "crash"


def test_move_train_4():
    assert move_train(board, "R") == "none"


if __name__ == "__main__":
    pytest.main()
