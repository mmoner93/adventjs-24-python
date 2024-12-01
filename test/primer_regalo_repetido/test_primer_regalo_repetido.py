"""
This module contains tests for the prepare_gifts function
from the solutions.primer_regalo_repetido.main module.
"""

import pytest
from solutions.primer_regalo_repetido.main import prepare_gifts


def test_prepare_gifts() -> None:
    """
    Test the prepare_gifts function with various test cases.
    """
    assert prepare_gifts([3, 1, 2, 3, 4, 2, 5]) == [1, 2, 3, 4, 5]
    assert prepare_gifts([6, 5, 5, 5, 5]) == [5, 6]
    assert prepare_gifts([]) == []
    assert prepare_gifts([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]
    assert prepare_gifts([1, 1, 1, 1, 1]) == [1]


if __name__ == "__main__":
    pytest.main()
