import os


# Task 6
# Реализуйте функцию которая умеет работать с файлами (читать из
# заданного файла, записывать в заданный файл).
# Программа считает количество строк, слов и букв в заданном файле
# и дописывает эту информацию обратно в файл,
# так же выводит эту информацию на экран.


def read_write_to_file(file_path):
    # to create file if it not exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    count_lines = len(lines)
    count_words = sum(len(line.split()) for line in lines)

    count_letters = 0
    for line in lines:
        for word in line.split():
            count_letters += len(word)

    result = (
        f"\n Count of lines: {count_lines}; "
        f"Count of words: {count_words}; Count of letters: {count_letters} \n"
    )
    print(result)
    # and write it back
    with open(file_path, 'a') as file:
        file.write(result)
