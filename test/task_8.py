# Task 8

# Создайте класс "Банковский счет" с методами для внесения и снятия денег,
# а также для проверки баланса.
# Учтите возможность возникновения ошибок при операциях со счетом.

class Bank:

    def __init__(self, amount):
        self.amount = amount

    def deposit(self, money):
        self.amount += money
        return self.amount

    def withdraw_money(self, money):
        if self.amount - money < 0:
            print(f'Insufficient sum, available amount is {self.amount}')
            return False
        self.amount -= money
        return self.amount

    def check_balance(self):
        print(f'current balance is {self.amount}')
        return self.amount


user = Bank(amount=1000)
assert user.check_balance() == 1000
assert user.deposit(1111) == 2111
assert user.withdraw_money(1111) == 1000
assert user.withdraw_money(1000000) is False
