import punq
from src.domain.use_cases.add_user import AddUserUseCase


def test_add_user_success(
    container: punq.Container,
) -> None:
    use_case = container.resolve(AddUserUseCase)

    result = use_case.execute()

    assert result == "some user entity"
