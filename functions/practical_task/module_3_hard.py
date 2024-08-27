def calculate_structure_sum(*args):
    struct_sum = 0.0
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                struct_sum += calculate_structure_sum(key)
                struct_sum += calculate_structure_sum(value)
        elif isinstance(arg, (list, tuple, set)):
            for value in arg:
                struct_sum += calculate_structure_sum(value)
        elif isinstance(arg, str):
            struct_sum += len(arg)
        else:
            struct_sum += arg
    return struct_sum


data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]

result = calculate_structure_sum(data_structure)
print(result)
