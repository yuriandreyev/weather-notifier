import uuid

from src.domain.entities import Notification
from src.notification.domain.repos import NotificationRepo


class NotificationInMemoryRepo(NotificationRepo):
    notifications: dict[uuid.UUID, Notification] = {}

    def add_notification(self, notification: Notification) -> None:
        self.notifications[notification.id] = notification

    def delete_notification(self, notification_id: uuid.UUID) -> None:
        del self.notifications[notification_id]
