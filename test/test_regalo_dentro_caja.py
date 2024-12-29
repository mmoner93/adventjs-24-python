import pytest
from solutions.day_6_regalo_dentro_caja import in_box


def test_regalo_dentro_caja_1():
    assert in_box(["###", "#*#", "###"])


def test_regalo_dentro_caja_2():
    assert in_box(["####", "#* #", "#  #", "####"])


def test_regalo_dentro_caja_3():
    assert not in_box(["#####", "#   #", "#  #*", "#####"])


def test_regalo_dentro_caja_4():
    assert not in_box(["#####", "#   #", "#   #", "#   #", "#####"])


if __name__ == "__main__":
    pytest.main()
