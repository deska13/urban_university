class Video:
    def __init__(
        self,
        title: str,
        duration: float,
        # time_now: float = 0.0,
        adult_mode: bool = False,
    ) -> None:
        self.title = title
        self.duration = duration
        # self.time_now = time_now в таком варианте для всех пользователей будет одно и то же время остановки видео
        self.adult_mode = adult_mode

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, value: object) -> bool:
        return isinstance(value, Video) and self.title == value.title

    def __contains__(self, value: object) -> bool:
        return isinstance(value, str) and value.lower() in self.title.lower()

    def __str__(self) -> str:
        return self.title
