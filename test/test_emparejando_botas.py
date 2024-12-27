import pytest
from solutions.day_5_emparejando_botas import organizeShoes


def test_organize_shoes_1():
    shoes1 = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 42},
    ]
    assert organizeShoes(shoes1) == [38, 42]


def test_organize_shoes_2():
    shoes2 = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
        {"type": "I", "size": 38},
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
    ]
    assert organizeShoes(shoes2) == [38, 38]


def test_organize_shoes_3():
    shoes3 = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 36},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 43},
    ]
    assert organizeShoes(shoes3) == []


def test_organize_shoes_4():
    shoes4 = [
        {"type": "I", "size": 40},
        {"type": "R", "size": 40},
        {"type": "I", "size": 40},
        {"type": "R", "size": 40},
    ]
    assert organizeShoes(shoes4) == [40, 40]


def test_organize_shoes_5():
    shoes5 = [
        {"type": "I", "size": 39},
        {"type": "R", "size": 39},
        {"type": "I", "size": 39},
        {"type": "R", "size": 39},
        {"type": "I", "size": 39},
    ]
    assert organizeShoes(shoes5) == [39, 39]


if __name__ == "__main__":
    pytest.main()
