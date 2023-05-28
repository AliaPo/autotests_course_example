# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    """
    Функция содержит локальную функцию
    :return: Возвращает новое значение переменной, полученное в локальной функции
    """
    msg = 1

    def local_function():
        """
    Функция меняет значение переменной, заданной в объемлющей функции
        :return: Возвращает новое значение переменной msg
        """
        nonlocal msg
        msg = 2
        return msg

    local_function()
    return msg


global_function()

assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')