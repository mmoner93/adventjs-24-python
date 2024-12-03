def createXmasTree(height, ornament):
    lines = [
        "_" * (height - i - 1) + ornament * (2 * i + 1) + "_" * (height - i - 1)
        for i in range(height)
    ]
    trunk = "_" * (height - 1) + "#" + "_" * (height - 1)
    lines.extend([trunk, trunk])
    return "\n".join(lines)


if __name__ == "__main__":
    print(createXmasTree(5, "*"))
    print(createXmasTree(3, "o"))
    print(createXmasTree(4, "x"))
    print(createXmasTree(2, "a"))
    print(createXmasTree(1, "b"))
    print(createXmasTree(0, "c"))
    print(createXmasTree(6, "d"))
    print(createXmasTree(7, "e"))
    print(createXmasTree(8, "f"))
