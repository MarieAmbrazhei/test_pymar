# Task 2

# Которая запрашивает у пользователя число и выводит его квадрат
def square_digit(digit=None):
    digit = input('Please enter digit to be squared: ') if not digit else digit
    try:
        digit = int(digit)
    except ValueError:
        print(f'Please enter digit! Given value "{digit}" is not digit!')
        return False
    else:
        result = digit ** 2
        print(f'squared digit equal {result}')
        return result


assert square_digit(5) == 25
assert square_digit(-1) == 1
assert square_digit('asd') is False


# Которая запрашивает у пользователя число и определяет,
# является ли оно четным или нечетным
def check_even_or_not(digit=None):
    digit = input('Please enter digit to be checked: ') if not digit else digit
    try:
        digit = int(digit)
    except ValueError:
        print(f'Please enter digit! Given value "{digit}" is not digit!')
        return False
    if digit % 2 == 0:
        print(f'Given digit "{digit}" is even')
        return True
    print(f'Given digit "{digit}" is odd')
    return True
