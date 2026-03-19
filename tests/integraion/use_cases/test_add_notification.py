import punq
import uuid
from datetime import datetime
from src.domain.use_cases.add_notification import (
    AddNotificationUseCase,
    AddNotificationUseCaseParams,
)
from src.notification.domain.repos import NotificationRepo


def test_add_notification_success(
    container: punq.Container,
) -> None:
    notification_id = uuid.uuid4()
    user_id = uuid.uuid4()
    use_case = container.resolve(AddNotificationUseCase)
    notification_repo = container.resolve(NotificationRepo)

    result = use_case.execute(params=AddNotificationUseCaseParams(
        method="tg",
        target="tg_user_id",
        time=datetime.now(),
        lat=0.0,
        long=0.0,
        user_id=user_id,
        id=notification_id,
    ))

    notification_repo.delete_notification(notification_id=result.id)
