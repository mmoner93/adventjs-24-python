def draw_race(indices, length):
    length = length - 1
    lines = len(indices)
    result = []
    for i in range(lines):
        index = indices[i] if indices[i] >= 0 else length + indices[i] + 1
        r = "r" if index != 0 else "~"
        line = (
            f"{' ' * (lines - 1 - i)}"
            f"{'~' * index}"
            f"{r}"
            f"{'~' * (length - index)}"
            f" /{i + 1}"
        )
        result.append(line)
    return "\n".join(result)


if __name__ == "__main__":
    print(draw_race([0, 5, -3], 10))
