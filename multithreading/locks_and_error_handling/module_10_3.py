import time
from random import randint
from threading import Lock, Thread


class Bank:
    def __init__(self) -> None:
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            random_number = randint(50, 500)
            self.balance += random_number
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {random_number}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            random_number = randint(50, 500)
            print(f"Запрос на {random_number}")
            self.balance -= random_number
            if self.balance >= random_number:
                print(f"Снятие: {random_number}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
