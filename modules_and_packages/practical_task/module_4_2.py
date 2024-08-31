def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
"""
Функция inner_function не может быть вызвана вне test_function, так как существует только внутри функции test_function.
"""
print(any([value == "inner_function" for value in dir(test_function)]))
