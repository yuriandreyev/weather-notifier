import uuid

from src.domain.entities import User
from src.domain.repos.user import UserRepo


class AddUserUseCase:
    def __init__(self, user_repo: UserRepo) -> None:
        self.user_repo = user_repo

    def execute(self, user_name: str) -> User:
        user = User(name=user_name, user_id=uuid.uuid4())
        self.user_repo.add_user(user)

        return user
