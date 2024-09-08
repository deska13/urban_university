import time
from datetime import datetime
from threading import Thread


def bencmark(func):
    def wrapper(*args, **kwargs):
        start_at = datetime.now()
        res = func(*args, **kwargs)
        end_at = datetime.now()
        func_execution_at = end_at - start_at
        print(f"Время выполнения функции {func.__name__}: {func_execution_at}")
        return res

    return wrapper


def wite_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


@bencmark
def write_with_func():
    data_for_func = [
        (10, "example1.txt"),
        (30, "example2.txt"),
        (200, "example3.txt"),
        (0, "example4.txt"),
    ]
    for x, y in data_for_func:
        wite_words(x, y)


@bencmark
def write_with_thread():
    data_for_thread = [
        (10, "example5.txt"),
        (30, "example6.txt"),
        (200, "example7.txt"),
        (0, "example8.txt"),
    ]
    threads = []
    for x, y in data_for_thread:
        thread = Thread(target=wite_words, args=(x, y))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


write_with_func()
write_with_thread()
