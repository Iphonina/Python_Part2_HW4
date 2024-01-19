# Напишите программу банкомат.
# Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти.
# Сумма пополнения м снятия кратна 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются 3%.
# Нельзя снять больше, чем на счёте. При превышении суммы на 5 млн, вычитать
# налог на богатство 10% перед каждой операцией, даже ошибочной.
# Любое действие выводит сумму денег.Дополнительно сохраняйте все операции
# поступления и снятия средств в список.


def atm():
    balance = 0
    operations = []

    def deposit(amount):
        nonlocal balance
        nonlocal operations

        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратной 50.")
            return

        if balance > 5000000:
            balance -= balance * 0.1

        balance += amount
        operations.append("Пополнение на сумму: " + str(amount))

        if len(operations) % 3 == 0:
            balance += balance * 0.03

        print("На вашем счете: " + str(balance) + " у.е.")

    def withdraw(amount):
        nonlocal balance
        nonlocal operations

        if amount % 50 != 0:
            print("Сумма снятия должна быть кратной 50.")
            return

        if amount > balance:
            print("Недостаточно средств на счете.")
            return

        if balance > 5000000:
            balance -= balance * 0.1

        fee = amount * 0.015
        fee = 30 if fee < 30 else fee
        fee = 600 if fee > 600 else fee

        balance -= amount + fee
        operations.append("Снятие на сумму: " + str(amount) + ", комиссия: " + str(fee))

        if len(operations) % 3 == 0:
            balance += balance * 0.03

        print("На вашем счете: " + str(balance) + " у.е.")

    def print_operations():
        for operation in operations:
            print(operation)

    while True:
        action = input("Введите действие (пополнить, снять, выйти): ")

        if action == "пополнить":
            amount = int(input("Введите сумму пополнения: "))
            deposit(amount)
        elif action == "снять":
            amount = int(input("Введите сумму снятия: "))
            withdraw(amount)
        elif action == "выйти":
            print_operations()
            break
        else:
            print("Некорректное действие, повторите попытку.")


atm()
