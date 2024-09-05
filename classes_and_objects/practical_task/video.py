import time

from user import User


class Video:
    def __init__(
        self,
        title: str,
        duration: float,
        adult_mode: bool = False,
    ) -> None:
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Video):
            return self.title == value.title
        return False

    def __contains__(self, value: object) -> bool:
        if isinstance(value, str):
            return value.lower() in self.title.lower()
        return False

    def __str__(self) -> str:
        return self.title

    def watch(self, user: User) -> None:
        if self.adult_mode and user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        while self.time_now < self.duration:
            self.time_now += 1
            print(self.time_now, end=" ")
            time.sleep(1)
        self.time_now = 0
        print("Конец видео")
