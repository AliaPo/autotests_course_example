# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1():
    assert all_division(4, 2) == 2


def test_new2():
    assert all_division(2, 0) == 0


def test3():
    assert all_division(20, 5) == 4


@pytest.mark.smoke
def test_new4():
    assert all_division(100, 10) == 10


def test_new5():
    assert all_division(6, 3) == 2
