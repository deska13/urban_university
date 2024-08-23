immutable_var = 1, 1.5, False, "Text"
print(immutable_var)
# immutable_var[0] = 0
# Tuple не поддерживает изменение значения по индексу, так как является неизменяемым типом данных.

mutable_list = [1, 4.5, True, "Test"]
mutable_list[1] = 8.9
print(mutable_list)
