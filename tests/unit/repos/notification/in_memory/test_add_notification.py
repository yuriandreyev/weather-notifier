from datetime import datetime
import uuid

from src.notification.repos.in_memory import NotificationInMemoryRepo
from src.domain.entities import Notification


def test_add_notification_success() -> None:
    notification_id = uuid.uuid4()
    user_id = uuid.uuid4()
    notification = Notification(
        method="tg",
        target="tg_user_id",
        time=datetime.now(),
        lat=0.0,
        long=0.0,
        user_id=user_id,
        id=notification_id,
    )
    repo = NotificationInMemoryRepo()

    repo.add_notification(notification)

    assert repo.notifications == {notification_id: notification}
    repo.delete_notification(notification_id=notification_id)
