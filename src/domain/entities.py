import uuid
from datetime import datetime


class User:
    def __init__(self, user_id: uuid.UUID, name: str) -> None:
        self.id = user_id
        self.name = name


class Notification:
    def __init__(
            self,
            method: str,
            target: str,
            time: datetime,
            lat: float,
            long: float,
    ) -> None:
        self.method = method
        self.target = target
        self.time = time
        self.lat = lat
        self.long = long
