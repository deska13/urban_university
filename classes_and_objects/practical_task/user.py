class User:
    def __init__(
        self,
        nickname: str,
        password: str,
        age: int,
    ) -> None:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self) -> str:
        return f"{self.nickname}"

    def check_password(self, password: str) -> bool:
        return self.password == hash(password)
