def compile(instructions):
    result = {}
    index = 0

    while index < len(instructions):
        parts = instructions[index].split(" ")
        comm = parts[0]
        x = parts[1] if len(parts) > 1 else None
        y = parts[2] if len(parts) > 2 else None

        if x and x not in result:
            result[x] = 0

        if comm == "DEC":
            result[x] -= 1
        elif comm == "INC":
            result[x] += 1
        elif comm == "MOV":
            result[y] = result[x] if not x.isdigit() else int(x)
        elif comm == "JMP" and result[x] == 0:
            index = int(y) - 1

        index += 1

    return result["A"]


if __name__ == "__main__":
    instructions = [
        "MOV -1 C",  # copia -1 al registro 'C'
        "INC C",  # incrementa el valor del registro 'C'
        "JMP C 1",  # salta a la instrucción en el índice 1 si 'C' es 0
        "MOV C A",  # copia el registro 'C' al registro 'a'
        "INC A",  # incrementa el valor del registro 'a'
    ]

    print(compile(instructions))  # 2

    instructions = [
        "INC C",  # incrementa el valor del registro 'C'
        "DEC B",
        "MOV C Y",
        "INC Y",
    ]
    print(compile(instructions))
