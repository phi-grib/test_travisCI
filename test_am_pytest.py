from astonishing_math import multiply, suma


def test_numbers_3_4():
    assert multiply(3, 4) == 12
    assert suma(3, 4) == 7


def test_strings_a_3():
    assert multiply('a', 3) == 'aaa'
    assert suma('a', 'a') == 'aa'

