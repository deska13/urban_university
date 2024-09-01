import time

from video import Video


class User:
    watch_history: dict[Video, int] = {}

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

    def watch(self, video: Video) -> None:
        if video.adult_mode and self.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        self.watch_history[video] = 0
        while self.watch_history[video] < video.duration:
            self.watch_history[video] += 1
            print(self.watch_history[video], end=" ")
            time.sleep(1)
        print("Конец видео")
