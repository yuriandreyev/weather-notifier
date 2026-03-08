import uuid

from src.domain.entities import User
from src.domain.repos.user import UserRepo


class UserInMemoryRepo(UserRepo):
    users: dict[uuid.UUID, User] = {}

    def add_user(self, user: User) -> None:
        self.users[user.id] = user

    def delete_user(self, user_id: uuid.UUID) -> None:
        del self.users[user_id]
