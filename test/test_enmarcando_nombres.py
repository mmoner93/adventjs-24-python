"""
This module contains tests for the createFrame function
from the solutions.enmarcando_nombres.main module.
"""

import pytest
from solutions.day_2_enmarcando_nombres import createFrame


def test_create_frame_1() -> None:
    assert createFrame(["midu", "madeval", "educalvolpz"]).split("\n") == [
        "***************",
        "* midu        *",
        "* madeval     *",
        "* educalvolpz *",
        "***************",
    ]
def test_create_frame_2() -> None:
    assert createFrame(["midu"]).split("\n") == ["********", "* midu *", "********"]
def test_create_frame_3() -> None:
    assert createFrame(["a", "bb", "ccc"]).split("\n") == [
        "*******",
        "* a   *",
        "* bb  *",
        "* ccc *",
        "*******",
    ]
def test_create_frame_4() -> None:
    assert createFrame(["a", "bb", "ccc", "dddd"]).split("\n") == [
        "********",
        "* a    *",
        "* bb   *",
        "* ccc  *",
        "* dddd *",
        "********",
    ]

if __name__ == "__main__":
    pytest.main()
