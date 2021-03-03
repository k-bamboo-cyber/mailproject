import pytest
from functions.check import checkdiv


class TestInt:

    @pytest.mark.parametrize(
        "dividend, divider",
        [(0, 1), (56, 8),
         pytest.param(4567, 0, marks=pytest.mark.xfail),
         pytest.param(1, 9, marks=pytest.mark.xfail),
         pytest.param(-1, 567, marks=pytest.mark.xfail),
         (343, -1)]
    )
    def test_check_divisibility(self, dividend, divider):
        """Тест на делимость"""
        assert checkdiv(dividend, divider) == True, "Число не делится без остатка"

    @pytest.mark.parametrize(
        "a, b", [(56, 50),
                 pytest.param(-46, -46, marks=pytest.mark.xfail),
                 pytest.param(0, 0, marks=pytest.mark.xfail)]
    )
    def test_check_inequality(self, a, b):
        "Негативный тест на проверку неравенства двух чисел"
        assert a != b, "Числa равны"


class TestSet:
    @pytest.mark.parametrize(
        "s, l",
        [({'a', 'b', 'c', 'd'}, 4), ({}, 0),
         pytest.param({'a', 'b'}, 7, marks=pytest.mark.xfail),
         ]
    )
    def test_check_length(self, s, l):
        """Тест на проверку кол-ва элементов"""
        assert len(s) == l, "Длина множества не соответствует заявленной"
