def fix_packages(packages):
    while "(" in packages:
        # Find the last opening parenthesis and its corresponding closing parenthesis
        start = packages.rfind("(")
        end = packages.find(")", start)
        # Rebuild the string by replacing the content inside the parentheses
        packages = (
            packages[:start] + packages[start + 1 : end][::-1] + packages[end + 1 :]
        )
    return packages


if __name__ == "__main__":
    fix_packages("(12(34)56)")
