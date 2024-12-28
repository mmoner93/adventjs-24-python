import pytest
from solutions.day_7_ataque_grinch import fix_packages


def test_ataque_grinch_1():
    assert fix_packages("a(cb)de") == "abcde"


def test_ataque_grinch_2():
    assert fix_packages("a(bc(def)g)h") == "agdefcbh"


def test_ataque_grinch_3():
    assert fix_packages("abc(def(gh)i)jk") == "abcighfedjk"


def test_ataque_grinch_4():
    assert fix_packages("a(b(c))e") == "acbe"


if __name__ == "__main__":
    pytest.main()
