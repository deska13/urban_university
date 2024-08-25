def single_root_words(root_word: str, *other_words: str):
    same_words: list[str] = [
        other_word
        for other_word in other_words
        if (
            root_word.lower() in other_word.lower()
            or other_word.lower() in root_word.lower()
        )
    ]
    return same_words


result1 = single_root_words("rich", "richiest", "orichalcum", "cheers", "richies")
result2 = single_root_words("Disablement", "Able", "Mable", "Disable", "Bagel")
print(result1)
print(result2)
