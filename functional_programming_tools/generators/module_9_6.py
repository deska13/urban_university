def all_variants(text):
    for i in range(len(text)):
        for symbol in text[i:]:
            yield text[:i] + symbol


variants = all_variants("abc")
for variant in variants:
    print(variant)
