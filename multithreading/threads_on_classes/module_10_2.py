import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        count_enemy = 100
        number_day = 0
        while count_enemy > 0:
            number_day += 1
            count_enemy -= self.power
            print(
                f"{self.name} сражается {number_day} дней..., осталось {count_enemy} воинов."
            )
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {number_day} дней(дня).")


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
knights = (first_knight, second_knight)

for knight in knights:
    knight.start()
for knight in knights:
    knight.join()
