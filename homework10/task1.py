# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv
import random


def generate_random_name():
    latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        first_word = ''
        second_word = ''
        for first in range(random.randint(1, 15)):
            for letter_for_first_word in random.choice(latin_alphabet):
                first_word += ''.join(letter_for_first_word)

        for second in range(random.randint(1, 15)):
            for letter_for_second_word in random.choice(latin_alphabet):
                second_word += ''.join(letter_for_second_word)

        yield f'{first_word} {second_word}'


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
