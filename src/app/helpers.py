import punq

from src.domain.use_cases.add_user import AddUserUseCase
from src.domain.repos.user import UserRepo

from src.user.repos import UserInMemoryRepo


def create_container() -> punq.Container:
    container = punq.Container()
    container.register(UserRepo, factory=UserInMemoryRepo)
    _register_use_cases(container)

    return container


def _register_use_cases(container: punq.Container) -> None:
    container.register(AddUserUseCase)
