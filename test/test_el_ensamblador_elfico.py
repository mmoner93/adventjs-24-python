import pytest
from solutions.day_10_el_ensamblador_elfico import compile


def test_compile_1():
    instructions = [
        "MOV -1 C",  # copia -1 al registro 'C'
        "INC C",  # incrementa el valor del registro 'C'
        "JMP C 1",  # salta a la instrucción en el índice 1 si 'C' es 0
        "MOV C A",  # copia el registro 'C' al registro 'a'
        "INC A",  # incrementa el valor del registro 'a'
    ]
    assert compile(instructions) == 2


def test_compile_2():
    instructions = ["MOV 0 A", "INC A"]
    assert compile(instructions) == 1


def test_compile_3():
    instructions = [
        "INC A",
        "INC A",
        "DEC A",
        "MOV A B",
    ]
    assert compile(instructions) == 1


def test_compile_4():
    instructions = ["MOV 5 B", "DEC B", "MOV B A", "INC A"]
    assert compile(instructions) == 5


def test_compile_5():
    instructions = [
        "INC C",
        "DEC B",
        "MOV C Y",
        "INC Y",
    ]
    with pytest.raises(KeyError, match="'A'"):
        compile(instructions)


def test_compile_6():
    instructions = ["MOV 2 X", "DEC X", "DEC X", "JMP X 1", "MOV X A"]
    assert compile(instructions) == -2


def test_compile_7():
    instructions = ["MOV 3 C", "DEC C", "DEC C", "DEC C", "JMP C 3", "MOV C A"]
    assert compile(instructions) == -1


if __name__ == "__main__":
    pytest.main()
