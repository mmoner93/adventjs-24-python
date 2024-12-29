import pytest
from solutions.day_8_carrera_de_renos import draw_race


def test_draw_race_1(capsys):
    assert draw_race([0, 5, -3], 10).split("\n") == [
        "  ~~~~~~~~~~ /1",
        " ~~~~~r~~~~ /2",
        "~~~~~~~r~~ /3",
    ]


def test_draw_race_2(capsys):
    assert draw_race([2, -1, 0, 5], 8).split("\n") == [
        "   ~~r~~~~~ /1",
        "  ~~~~~~~r /2",
        " ~~~~~~~~ /3",
        "~~~~~r~~ /4",
    ]


def test_draw_race_3(capsys):
    assert draw_race([3, 7, -2], 12).split("\n") == [
        "  ~~~r~~~~~~~~ /1",
        " ~~~~~~~r~~~~ /2",
        "~~~~~~~~~~r~ /3",
    ]


if __name__ == "__main__":
    pytest.main()
