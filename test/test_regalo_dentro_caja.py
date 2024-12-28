import pytest
from solutions.day_6_regalo_dentro_caja import in_box


def test_regalo_dentro_caja_1():
    assert in_box(["###", "#*#", "###"]) == True


def test_regalo_dentro_caja_2():
    assert in_box(["####", "#* #", "#  #", "####"]) == True


def test_regalo_dentro_caja_3():
    assert in_box(["#####", "#   #", "#  #*", "#####"]) == False


def test_regalo_dentro_caja_4():
    assert in_box(["#####", "#   #", "#   #", "#   #", "#####"]) == False


if __name__ == "__main__":
    pytest.main()
