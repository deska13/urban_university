from datetime import datetime
from multiprocessing import Pool


def read_info(name: str) -> None:
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        all_data.extend([line.strip() for line in file])


if __name__ == "__main__":
    file_names = [f"./file {number}.txt" for number in range(1, 5)]
    t = datetime.now()
    for file_name in file_names:
        read_info(file_name)
    print(datetime.now() - t, "(линейный)")

    t = datetime.now()
    with Pool() as pool:
        pool.map(read_info, file_names)
    print(datetime.now() - t, "(многопроцессный)")
