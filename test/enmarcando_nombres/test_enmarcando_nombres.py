"""
This module contains tests for the createFrame function
from the solutions.enmarcando_nombres.main module.
"""

import pytest
from solutions.enmarcando_nombres.main import createFrame


def test_create_frame() -> None:
    """
    Test the createFrame function with various test cases.
    """

    assert createFrame(["midu", "madeval", "educalvolpz"]).split("\n") == [
        "***************",
        "* midu        *",
        "* madeval     *",
        "* educalvolpz *",
        "***************",
    ]
    assert createFrame(["midu"]).split("\n") == ["********", "* midu *", "********"]
    assert createFrame(["a", "bb", "ccc"]).split("\n") == [
        "*******",
        "* a   *",
        "* bb  *",
        "* ccc *",
        "*******",
    ]
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
