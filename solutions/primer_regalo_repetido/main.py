"""
This module provides a function to prepare gifts by sorting and removing duplicates.
"""

def prepare_gifts(gifts: list[str]) -> list[str]:
    """
    Prepare the gifts by sorting and removing duplicates.

    Args:
        gifts (list): A list of gifts.

    Returns:
        list: A sorted list of unique gifts.
    """
    return list(dict.fromkeys(sorted(gifts)))


if __name__ == "__main__":
    print(prepare_gifts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))