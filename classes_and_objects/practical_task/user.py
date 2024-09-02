import time

from video import Video


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

    def watch(self, video: Video) -> None:
        if video.adult_mode and self.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        while video.time_now < video.duration:
            video.time_now += 1
            print(video.time_now, end=" ")
            time.sleep(1)
        video.time_now = 0
        print("Конец видео")
