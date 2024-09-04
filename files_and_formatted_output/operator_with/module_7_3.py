import re
from collections import defaultdict


class WordsFinder:
    def __init__(self, *file_names: str) -> None:
        self.file_names = file_names

    def get_all_words(self) -> dict[str, list[str]]:
        all_words = {}
        for file_name in self.file_names:
            words: list[str] = []
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file:
                    for value in re.split(r"[\n ,.=!?;:]+", line.lower()):
                        if value and value != "-":
                            words.append(value)
            all_words[file_name] = words
        return all_words

    def find(self, word: str) -> dict[str, int]:
        result: dict[str, int] = {}
        word = word.lower()
        for key, values in self.get_all_words().items():
            for i, value in enumerate(values):
                if value == word:
                    result[key] = i + 1
                    break
        return result

    def count(self, word: str) -> dict[str, int]:
        result: defaultdict[str, int] = defaultdict(int)
        word = word.lower()
        for key, values in self.get_all_words().items():
            for value in values:
                if value == word:
                    result[key] += 1
        return dict(result)


finder2 = WordsFinder("hyphen.txt", "test.txt", "products.txt")
print(finder2.get_all_words())
print(finder2.find("TEXT"))
print(finder2.count("teXT"))
print(finder2.count("potato"))
