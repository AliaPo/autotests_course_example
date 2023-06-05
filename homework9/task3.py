# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

from pathlib import Path

path = Path("test_file/task_3.txt")
my_dir = Path.cwd()
whole_path = f'{my_dir}/{path}'
file_text = open(whole_path, 'r', encoding='utf-8')

numbers_list = []
sum_purchase = 0

for i in file_text.readlines():
    if i == '\n':
        numbers_list.append(sum_purchase)
        sum_purchase = 0
        continue
    else:
        sum_purchase += int(i)

max_numbers = []

while len(max_numbers) < 3:
    for number in numbers_list:
        if number == max(numbers_list):
            max_numbers.append(number)
            index_number = numbers_list.index(number)
            numbers_list[index_number] = 0
            break

three_most_expensive_purchases = sum(max_numbers)

file_text.close()

assert three_most_expensive_purchases == 202346
