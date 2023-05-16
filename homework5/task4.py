# Игра "Эрудит"
# Нужно написать программу scrabble, которая помогает считать кол-во очков (points), полученное за слово (word)
# По одному очку вы получите за буквы а, в, е=ё, и, н, о, р, с, т.
# Два очка стоит д, к, л, м, п, у.
# Три балла получают за б, г, ь, а также я.
# Четыре балла стоят буквы й, ы.
# 5 очков засчитывается за ж, з, х, ц, ч.
# 6 и 7 очков не предусмотрено.
# Восемь можно получить за букву ф, ш, э, ю.
# 10 баллов стоит буква щ,
# а 15 - ъ
# Например (Ввод --> Вывод):
# курс --> 6 (к=2, у=2, р=1, с=1)


def scrabble(word):
    """
    Функция принимает на вход строку (word) и возвращает сумму баллов (points),
    полученных за каждую букву слова

    :param word: Слово
    :return: Сумма баллов за каждую букву слова
    """
    new_dict = {}
    one_point = ['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т']
    two_points = ['д', 'к', 'л', 'м', 'п', 'у']
    three_points = ['б', 'г', 'ь', 'я']
    four_points = ['й', 'ы']
    five_points = ['ж', 'з', 'х', 'ц', 'ч']
    eight_points = ['ф', 'ш', 'э', 'ю']
    ten_points = ['щ']
    fifteen_points = ['ъ']
    for letter in word:
        if letter in one_point:
            new_dict[letter] = word.count(letter) * 1
        if letter in two_points:
            new_dict[letter] = word.count(letter) * 2
        if letter in three_points:
            new_dict[letter] = word.count(letter) * 3
        if letter in four_points:
            new_dict[letter] = word.count(letter) * 4
        if letter in five_points:
            new_dict[letter] = word.count(letter) * 5
        if letter in eight_points:
            new_dict[letter] = word.count(letter) * 8
        if letter in ten_points:
            new_dict[letter] = word.count(letter) * 10
        if letter in fifteen_points:
            new_dict[letter] = word.count(letter) * 15

    lst = []
    for one_value in new_dict.values():
        lst.append(str(one_value))

    points = 0

    for number in lst:
        points += int(number)

    return points


data = ["курс", 'авеинорстё', 'дклмпеу', 'бгья', 'йы', 'жзхцч', 'фшэю', 'щъ', "карабасбарабас", "околоводопроводного",
        "еженедельное", 'эхоэнцефалограф', 'человеконенавистничество', 'делопроизводительница']

test_data = [6, 10, 13, 12, 8, 25, 32, 25, 21, 26, 20, 54, 34, 36]

for i, d in enumerate(data):
    assert scrabble(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
