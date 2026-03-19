import uuid

from dataclasses import dataclass
from datetime import datetime

from src.domain.entities import Notification
from src.notification.domain.repos.notification import NotificationRepo


@dataclass
class AddNotificationUseCaseParams:
    method: str
    target: str
    time: datetime
    lat: float
    long: float
    id: uuid.UUID
    user_id: uuid.UUID


class AddNotificationUseCase:
    def __init__(self, notification_repo: NotificationRepo) -> None:
        self.notification_repo = notification_repo

    def execute(self, params: AddNotificationUseCaseParams) -> Notification:
        notification = Notification(
            method=params.method,
            target=params.target,
            time=params.time,
            lat=params.lat,
            long=params.long,
            user_id=params.user_id,
            id=params.id,
        )
        self.notification_repo.add_notification(notification)

        return notification
