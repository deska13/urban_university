import random
import time
from queue import Queue
from threading import Thread


class Table:
    def __init__(self, number: int) -> None:
        self.number = number
        self.quest: "Guest" | None = None


class Guest(Thread):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def run(self) -> None:
        time.sleep(random.randint(3, 10))
        return super().run()


class Cafe:
    def __init__(self, *tables: Table) -> None:
        self.tables = tables
        self.queue: "Queue[Guest]" = Queue()

    def guest_arrival(self, *guests: Guest) -> None:
        for guest in guests:
            is_find_table = False
            for table in self.tables:
                if table.quest is None:
                    table.quest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    guest.start()
                    is_find_table = True
                    break
            if not is_find_table:
                print(f"{guest.name} в очереди")
                self.queue.put(guest)

    def discuss_guests(self) -> None:
        while not self.queue.empty() or any(
            table.quest is not None for table in self.tables
        ):
            is_empty_table = False
            while not is_empty_table:
                for table in self.tables:
                    if table.quest is not None and not table.quest.is_alive():
                        print(f"{table.quest.name} покушал(-а) и ушёл(ушла)")
                        table.quest = None
                        is_empty_table = True
                        break
                time.sleep(1)
            if not self.queue.empty():
                guest = self.queue.get()
                for table in self.tables:
                    if table.quest is None:
                        table.quest = guest
                        guest.start()
                        print(
                            f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}",
                        )
                        break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    "Maria",
    "Oleg",
    "Vakhtang",
    "Sergey",
    "Darya",
    "Arman",
    "Vitoria",
    "Nikita",
    "Galina",
    "Pavel",
    "Ilya",
    "Alexandra",
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
