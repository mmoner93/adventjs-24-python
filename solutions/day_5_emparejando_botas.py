def organizeShoes(shoes):
    # Pre-initialize all sizes with a default structure
    sizes = {shoe["size"]: {"I": 0, "R": 0} for shoe in shoes}
    pairs = []

    # Single loop to count and form pairs
    for shoe in shoes:
        size = shoe["size"]
        type_ = shoe["type"]

        # Increment the respective type count
        sizes[size][type_] += 1

        # Form a pair immediately if possible
        if sizes[size]["I"] > 0 and sizes[size]["R"] > 0:
            pairs.append(size)
            sizes[size]["I"] -= 1
            sizes[size]["R"] -= 1

    return pairs


if __name__ == "__main__":
    shoes1 = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 42},
    ]
    pairs = organizeShoes(shoes1)
    print(pairs)
    shoes2 = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 36},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 42},
    ]
    pairs = organizeShoes(shoes2)
    print(pairs)
