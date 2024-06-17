# Task 10

# Напишите декоратор с параметрами decorator, который делает так,
# что задекорированная функция, будет возвращать результат в следующем формате:
# @decorator(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
# def identity(x):
#   return x
# print(identity(42))
# >>> ((1, 2, 3, [1, 2, 3], 'one', 'two', 'three'),
# {'two': 2, 'one': 1, 'three': 3})
# >>> 42
# @decorator()
# def identity(x):
#   return x
# print(identity(42))
# >>> ((), {})
# >>> 42


def decorator(*args, **kwargs):
    print((args, kwargs))

    def func_decorator(func):
        def wrapper(func_args):
            return func(func_args)

        return wrapper

    return func_decorator


@decorator(1, 2, 3, [1, 2, 3], 'one', 'two', 'three',
           one=1, two=2, three=3)
def identity(x):
    return x


print(identity(42))


@decorator()
def identity(x):
    return x


print(identity(42))
