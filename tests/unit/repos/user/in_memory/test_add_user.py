import uuid

from src.user.repos.in_memory import UserInMemoryRepo
from src.domain.entities import User


def test_add_user_success() -> None:
    user_id = uuid.uuid4()
    user = User(name="some-user", user_id=user_id)
    repo = UserInMemoryRepo()

    repo.add_user(user)

    assert repo.users == {user.id: user}
    repo.delete_user(user_id=user_id)
