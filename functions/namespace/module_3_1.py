calls = 0


def counts_calls():
    global calls
    calls += 1


def string_info(info: str):
    counts_calls()
    return len(info), info.upper(), info.lower()


def is_contains(src: str, arr: list[str]):
    counts_calls()
    return any(i.lower() == src.lower() for i in arr)


print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))  # Urban ~ urBAN
print(is_contains("cycle", ["recycling", "cyclic"]))  # No matches
print(calls)
