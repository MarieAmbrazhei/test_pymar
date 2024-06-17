import string

# Task 1

# Свяжите переменную с любой строкой, состоящей не менее чем из 15
# символов.
any_string = string.ascii_letters[:15]
assert len(any_string) == 15
# Извлеките из строки первый символ
first_letter = any_string[0]
assert first_letter == 'a'
# Извлеките из строки последний символ
last_letter = any_string[-1]
assert last_letter == 'o'
# Извлеките из строки третий с начала
third_letter = any_string[2]
assert third_letter == 'c'
# Извлеките из строки третий с конца
third_letter_from_the_end = any_string[-3]
assert third_letter_from_the_end == 'm'
# Переверните строку
reverted_string = any_string[::-1]
assert reverted_string == 'onmlkjihgfedcba'
# Извлеките первые восемь символов
first_eight_letters = any_string[:8]
assert first_eight_letters == 'abcdefgh'
