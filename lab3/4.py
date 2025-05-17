from datetime import datetime

class BankAccount:
    # Баланс и история транзакций
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0.0            # начинальный баланс
        self.__transactions = []        # список (дата, тип, сумма)

    # Пополнение счёта
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            # логируем операцию с текущим временем
            self.__transactions.append((datetime.now(), 'Деп', amount))
        else:
            print("Сумма пополнения должна быть положительной.")

    # Снятие со счёта
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
            return
        if amount > self.__balance:
            print("Недостаточно средств.")
            return
        self.__balance -= amount
        self.__transactions.append((datetime.now(), 'Оплата', amount))

    # Свойство для чтения баланса
    @property
    def balance(self):
        return self.__balance

    # Вывод истории операций
    def show_transactions(self):
        print(f"История операций для {self.owner}:")
        for dt, ttype, amt in self.__transactions:
            print(f"  {dt.strftime('%Y-%m-%d %H:%M:%S')} | {ttype:<7} | {amt:.2f}")

# Пример:
if __name__ == "__main__":
    acc = BankAccount("Дробин")  # создаём счёт
    acc.deposit(1000)             # положили 1000
    acc.withdraw(250)             # сняли 250
    acc.withdraw(10000)           # пробуем снять слишком много
    print("Текущий баланс:", acc.balance)
    acc.show_transactions()       # показываем лог