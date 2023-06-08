# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчанию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S

import datetime
import time


def func_log(file_log='log.txt'):
    """
    Декоратор, который дозаписывает в файл имя вызываемой функции, дату и время вызова в заданном формате.

    :param file_log: Путь до файла по умолчанию
    :return: Запись названия функции и время ее вызова в новый файл
    """
    def function_decorator(any_func):
        def wrapper():
            with open(file_log, mode='a', encoding='utf-8') as file:
                our_time = datetime.datetime.now()
                right_time_format = our_time.strftime('%d.%m %H:%M:%S')
                file.write(f'{any_func.__name__} вызвана {right_time_format}\n')
                any_func()
        return wrapper
    return function_decorator


@func_log()
def func1():
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    time.sleep(5)


func1()
func2()
func1()
