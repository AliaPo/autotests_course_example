# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


class TestExample:

    def test1(self, time_tests, working_time):
        time.sleep(1)

    def test2(self, time_tests):
        time.sleep(1)

    def test3(self, time_tests, working_time):
        time.sleep(1)

    def test4(self, time_tests):
        time.sleep(1)
