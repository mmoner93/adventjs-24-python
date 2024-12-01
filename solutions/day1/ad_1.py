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
