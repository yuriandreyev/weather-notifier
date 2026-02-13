import uuid

from src.domain.entities import User


class AddUserUseCase:
    def execute(self, user_name: str) -> User:
        return User(name=user_name, user_id=uuid.uuid4())
