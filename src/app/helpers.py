import punq

from src.domain.use_cases.add_notification import AddNotificationUseCase
from src.domain.use_cases.add_user import AddUserUseCase
from src.domain.repos.user import UserRepo
from src.notification.domain.repos import NotificationRepo

from src.user.repos import UserInMemoryRepo
from src.notification.repos import NotificationInMemoryRepo


def create_container() -> punq.Container:
    container = punq.Container()
    container.register(UserRepo, factory=UserInMemoryRepo)
    container.register(NotificationRepo, factory=NotificationInMemoryRepo)
    _register_use_cases(container)

    return container


def _register_use_cases(container: punq.Container) -> None:
    container.register(AddUserUseCase)
    container.register(AddNotificationUseCase)
