import uuid
from abc import ABC, abstractmethod

from src.domain.entities import Notification


class NotificationRepo(ABC):
    @abstractmethod
    def add_notification(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def delete_notification(self, notification_id: uuid.UUID) -> None:
        pass
