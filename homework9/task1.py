# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

from pathlib import Path

my_dir = Path.cwd()
first_path = Path("test_file/task1_data.txt")
second_path = Path("test_file/task1_answer.txt")

path_to_the_first_file = f'{my_dir}/{first_path}'
path_to_the_second_file = f'{my_dir}/{second_path}'

first_file_text = open(path_to_the_first_file, 'r', encoding='utf-8')

new_file = open(path_to_the_second_file, "a", encoding='utf-8')

lst_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in first_file_text.read():
    if i in lst_of_numbers:
        pass
    else:
        new_file.write(i)

new_file.close()

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонным"
print('Всё ок')
