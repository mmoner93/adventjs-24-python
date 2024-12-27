def organizeInventory(inventory):
    """
    This function receives a list of dictionaries with the inventory of a store.
    Each dictionary has the keys "name", "quantity" and "category".
    The function returns a dictionary with the categories as keys and the items as values.
    Each item is a dictionary with the name of the item as key and the total quantity as value.

    Args:
        inventory (list): A list of dictionaries with the inventory of a store.

    Returns:
        dict: A dictionary with the categories as keys and the items as values.
    """
    category = {}
    for item in inventory:
        cat = item["category"]
        name = item["name"]
        quantity = item["quantity"]
        if cat not in category:
            category[cat] = {}
        if name not in category[cat]:
            category[cat][name] = 0
        category[cat][name] += quantity
    return category


if __name__ == "__main__":
    inventary = [
        {"name": "doll", "quantity": 5, "category": "toys"},
        {"name": "car", "quantity": 3, "category": "toys"},
        {"name": "ball", "quantity": 2, "category": "sports"},
        {"name": "car", "quantity": 2, "category": "toys"},
        {"name": "racket", "quantity": 4, "category": "sports"},
    ]

    print(
        organizeInventory(inventary)
    )  # Expected {'toys': {'doll': 5, 'car': 5}, 'sports': {'ball': 2, 'racket': 4}}

    inventary2 = [
        {"name": "book", "quantity": 10, "category": "education"},
        {"name": "book", "quantity": 5, "category": "education"},
        {"name": "paint", "quantity": 3, "category": "art"},
    ]

    print(
        organizeInventory(inventary2)
    )  # Expected {'education': {'book': 15}, 'art': {'paint': 3}}
