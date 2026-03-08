import uuid
from abc import ABC, abstractmethod

from src.domain.entities import User


class UserRepo(ABC):
    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    def delete_user(self, user_id: uuid.UUID) -> None:
        pass
