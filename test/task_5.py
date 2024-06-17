# Task 5

# Напишите программу, которая принимает от пользователя строку и проверяет,
# является ли она палиндромом (читается одинаково слева направо и справа
# налево)

def check_palindrome(given_string: str = None):
    given_string = input('Please enter string to be checked: ') \
        if not given_string else given_string
    if isinstance(given_string, str):
        if given_string == given_string[::-1]:
            print(f'given string "{given_string}" is palindrome')
            return True
        else:
            print(f'given string "{given_string}" is NOT palindrome')
            return False


assert check_palindrome('level')
assert check_palindrome('aba')
assert check_palindrome('qwerty') is False
