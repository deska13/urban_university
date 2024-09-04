def custom_write(file_name: str, strings: list[str]) -> dict[tuple[int, int], str]:
    writeable_strings: dict[tuple[int, int], str] = {}
    with open(file_name, "w", encoding="utf-8") as file:
        for i, string in enumerate(strings):
            start_string = file.tell()
            file.write(f"{string} \n")
            writeable_strings[(i + 1, start_string)] = string
    return writeable_strings


info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)
for elem in result.items():
    print(elem)
