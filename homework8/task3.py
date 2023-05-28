# Напишите функцию segment
# На вход подается два кортежа с координатами точек (x1, y1), (x2, y2)

# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception. И если это исключение поймано,
# то функция возвращает текст исключения задом наперед (Нужно обратиться к атрибуту экзепляра класса Exception)
# Если исключения не произошло, то функция возвращает сумму всех координат


def segment(first_coordinates, second_coordinates):
    """
    Функция принимает на вход два кортежа с координатами точек.
    Если исключения не произошло, функция возвращает сумму всех координат.
    Если произошло - возвращает текст исключения задом наперед.

    :param first_coordinates: Первый кортеж с координатами точек
    :param second_coordinates: Второй кортеж с координатами точек
    :return: Либо текст исключения задом наперед, либо сумму всех координат
    """
    try:
        sum_coordinates = first_coordinates[0] + first_coordinates[1] + second_coordinates[0] + second_coordinates[1]

    except Exception as e:
        mistake_text = e.args[0]
        reversed_text = ''.join(reversed(mistake_text))
        return reversed_text
    else:
        return sum_coordinates


data = [
    ((2, 3), (4, 5)),
    ((2, -3), (4, 5)),
    ((2, 3), ('4', 5)),
    (('a', 3), (4, 5)),
]

test_data = [
    14,
    8,
    "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu",
    'rts ot )"tni" ton( rts etanetacnoc ylno nac']


for i, d in enumerate(data):
    assert segment(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
