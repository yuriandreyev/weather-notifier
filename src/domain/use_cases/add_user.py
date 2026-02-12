from src.domain.entities import User


class AddUserUseCase:
    def execute(self) -> User:
        return User()