class Product:
    def __init__(self, name: str, weight: float, category: str) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self) -> None:
        self.__file_name = "products.txt"

    def get_products(self) -> str:
        with open(self.__file_name, "r", encoding="utf-8") as file:
            return file.read()

    def add(self, *products: Product) -> None:
        with open(self.__file_name, "a+", encoding="utf-8") as file:
            for product in products:
                is_find_product = False
                file.seek(0)
                for line in file:
                    if str(product) == line.split("\n")[0]:
                        is_find_product = True
                        print(f"Продукт {product} уже есть в магазине")
                        break
                if not is_find_product:
                    file.write(f"{product}\n")


s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
