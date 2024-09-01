from user import User
from video import Video


class UrTube:
    users: list[User] = []
    videos: list[Video] = []
    current_user: User | None = None

    def __init__(self) -> None:
        self.videos = []

    def log_in(self, nickname: str, password: str) -> None:
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                return
        raise ValueError("Неверное имя пользователя или пароль")

    def log_out(self) -> None:
        self.current_user = None

    def register(self, nickname: str, password: str, age: int) -> None:
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(User(nickname, password, age))
        print(f"Пользователь {nickname} успешно зарегистрирован")
        self.log_in(nickname, password)

    def add(self, *videos: Video) -> None:
        for video in videos:
            if video in self.videos:
                continue
            self.videos.append(video)

    def get_videos(self, query: str) -> list[str]:
        return [video.title for video in self.videos if query in video]

    def watch_video(self, title: str) -> None:
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                self.current_user.watch(video)
