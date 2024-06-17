# Task 4

# Напишите программу которая умеет добавлять единицу
# к числу и возращает список.
# Число хранится в виде списка. Например число 123 будет
# храниться в виде списка: [1, 2, 4].
# [9] => [10]
# [1,2,3] => [1,2,4]
# [1,1,9] => [1,2,0]
# [9,9,9] => [1,0,0,0]
def increment_digit(given_digit: list):
    n = len(given_digit)

    for i in range(n - 1, -1, -1):
        given_digit[i] += 1

        if given_digit[i] < 10:
            return given_digit

        given_digit[i] = 0

    # if all digits were 9
    return [1] + given_digit


assert increment_digit([9]) == [1, 0]
assert increment_digit([1, 2, 3]) == [1, 2, 4]
assert increment_digit([1, 1, 9]) == [1, 2, 0]
assert increment_digit([9, 9, 9]) == [1, 0, 0, 0]
