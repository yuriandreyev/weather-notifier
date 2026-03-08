import punq
from src.domain.use_cases.add_user import AddUserUseCase
from src.domain.repos.user import UserRepo


def test_add_user_success(
    container: punq.Container,
) -> None:
    use_case = container.resolve(AddUserUseCase)
    user_repo = container.resolve(UserRepo)

    result = use_case.execute(user_name="Summer")

    assert result.name == "Summer"
    user_repo.delete_user(user_id=result.id)

