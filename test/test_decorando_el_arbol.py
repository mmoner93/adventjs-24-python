"""
This module contains tests for the createXmasTree function
from the solutions.decorando_el_arbol.main module.
"""

import pytest
from solutions.day_4_decorando_el_arbol import createXmasTree


def test_create_xmas_tree_5():
    tree = createXmasTree(5, "*").split("\n")
    expected = [
        "____*____",
        "___***___",
        "__*****__",
        "_*******_",
        "*********",
        "____#____",
        "____#____",
    ]
    assert tree == expected


def test_create_xmas_tree_3():
    tree = createXmasTree(3, "+").split("\n")
    expected = ["__+__", "_+++_", "+++++", "__#__", "__#__"]
    assert tree == expected


def test_create_xmas_tree_6():
    tree = createXmasTree(6, "@").split("\n")
    expected = [
        "_____@_____",
        "____@@@____",
        "___@@@@@___",
        "__@@@@@@@__",
        "_@@@@@@@@@_",
        "@@@@@@@@@@@",
        "_____#_____",
        "_____#_____",
    ]
    assert tree == expected


def test_create_xmas_tree_1():
    tree = createXmasTree(1, "$").split("\n")
    expected = ["$", "#", "#"]
    assert tree == expected


def test_create_xmas_tree_4():
    tree = createXmasTree(4, "&").split("\n")
    expected = ["___&___", "__&&&__", "_&&&&&_", "&&&&&&&", "___#___", "___#___"]
    assert tree == expected


if __name__ == "__main__":
    pytest.main()
