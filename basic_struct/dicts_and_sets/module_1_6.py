my_dict = {
    "Apple": "fruit",
    "Cucumber": "vegetable",
}
print(my_dict)
print(my_dict["Apple"])
print(my_dict.get("Tomato"))
my_dict.update(
    {"Tea": "drink", "Strawberry": "berry"},
)
deleted_values = my_dict.pop("Apple")
print(deleted_values)
print(my_dict)

my_set = {
    1,
    1,
    "text",
    True,
    False,
    True,
    4,
    5,
}  # True не был добавлен, так как True == 1 и 1 был добавлен раньше
print(my_set)
my_set.update({2, 3})
my_set.remove(1)
print(my_set)
