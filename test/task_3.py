# Task 3

# Напишите функцию, которая принимает строку и возвращает
# кол-во заглавных и строчных букв.
# 'The quick Brow Fox' => Upper case characters: 3, Lower case characters: 12
def count_low_upper_case_letters(given_string: str):
    upper_case_letters = 0
    lower_case_letters = 0
    for letter in given_string:
        if letter.islower():
            lower_case_letters += 1
        elif letter.isupper():
            upper_case_letters += 1
    print(f'Upper case characters: {upper_case_letters},'
          f' Lower case characters: {lower_case_letters}')
    return upper_case_letters, lower_case_letters


assert count_low_upper_case_letters('The quick Brow Fox') == (3, 12)
