def in_box(box):
    for i in range(1, len(box) - 1):
        if "*" not in box[i]:
            continue
        left, right = box[i].split("*")
        if left[0] == "#" and right.endswith("#"):
            return True
    return False


if __name__ == "__main__":
    in_box(["###", "#*#", "###"])

    in_box(["####", "#* #", "#  #", "####"])

    in_box(["#####", "#   #", "#  #*", "#####"])

    in_box(["#####", "#   #", "#   #", "#   #", "#####"])
