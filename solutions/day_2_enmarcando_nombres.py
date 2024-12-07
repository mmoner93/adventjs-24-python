"""
This module contains function to print a frame around a list of names.
"""


def createFrame(names: list[str]) -> str:
    """
    Create a frame around a list of names.

    Args:
        names (list): A list of names.

    Returns:
        str: A string representing the frame around the names.
    """
    if not names:
        return "*"
    max_len = max(map(len, names))
    border = "*" * (max_len + 4)
    framed_names = [f"* {name.ljust(max_len)} *" for name in names]
    return "".join([border] + [f"\n{name}" for name in framed_names] + [f"\n{border}"])


if __name__ == "__main__":
    print(createFrame(["midu", "madeval", "educalvolpz"]))
    print(createFrame(["midu"]))
    print(createFrame(["a", "bb", "ccc"]))
    print(createFrame(["a", "bb", "ccc", "dddd"]))
