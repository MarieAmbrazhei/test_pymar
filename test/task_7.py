import string


# Task 7

# Напишите функцию, преобразующую входную строку в выходную как в примерах,
# Пусть s = "abcdef...xyz", тогда вывод будет таким:
# f(s, 1) => "a"
# f(s, 2) => "aba"
# f(s, 3) => "abcba"
# f(s, 4) => "abcdcba"

def refactor_string(given_string: str, index: int):
    if isinstance(given_string, str):
        first_part = given_string[:index]
        second_part = first_part[::-1][1:]
        return first_part + second_part
    else:
        print(f'given string {given_string} is not valid string! ')
        return False


my_string = string.ascii_letters
assert refactor_string(my_string, 1) == 'a'
assert refactor_string(my_string, 2) == 'aba'
assert refactor_string(my_string, 3) == 'abcba'
assert refactor_string(my_string, 4) == 'abcdcba'
assert refactor_string(123, 2) is False
