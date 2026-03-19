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
            id: uuid.UUID,
            user_id: uuid.UUID,
    ) -> None:
        self.id = id
        self.method = method
        self.target = target
        self.time = time
        self.lat = lat
        self.long = long
        self.user_id = user_id
