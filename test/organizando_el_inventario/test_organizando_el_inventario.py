"""
Description: This file has the tests for the organizeInventory function.
"""

import pytest
from solutions.organizando_el_inventario.main import organizeInventory


def test_organize_inventory_1():
    inventory = [
        {"name": "doll", "quantity": 5, "category": "toys"},
        {"name": "car", "quantity": 3, "category": "toys"},
        {"name": "ball", "quantity": 2, "category": "sports"},
        {"name": "car", "quantity": 2, "category": "toys"},
        {"name": "racket", "quantity": 4, "category": "sports"},
    ]
    expected_result = {
        "toys": {"doll": 5, "car": 5},
        "sports": {"ball": 2, "racket": 4},
    }
    assert organizeInventory(inventory) == expected_result

def test_organize_inventory_2():
    inventory2 = [
        {"name": "book", "quantity": 10, "category": "education"},
        {"name": "book", "quantity": 5, "category": "education"},
        {"name": "paint", "quantity": 3, "category": "art"},
    ]
    expected_result2 = {"education": {"book": 15}, "art": {"paint": 3}}
    assert organizeInventory(inventory2) == expected_result2


if __name__ == "__main__":
    pytest.main()
