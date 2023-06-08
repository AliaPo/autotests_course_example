import pytest
import datetime


@pytest.fixture(scope='class')
def time_tests():
    start_test = datetime.datetime.now()
    start_test_format = start_test.strftime('%d.%m %H:%M:%S')
    yield start_test_format
    end_test = datetime.datetime.now()
    end_test_format = end_test.strftime('%d.%m %H:%M:%S')
    print(f'\nНачало выполнения класса: {start_test_format}'
          f'\nОкончание выполнения класса: {end_test_format}')


@pytest.fixture()
def working_time():
    start_test = datetime.datetime.now()
    yield start_test
    end_test = datetime.datetime.now()
    subtraction_time = end_test - start_test
    work_time = subtraction_time.total_seconds()
    print(f' Время выполнения теста: {work_time}')
