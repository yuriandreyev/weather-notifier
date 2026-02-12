import punq
import pytest

from src.app.helpers import create_container


@pytest.fixture()
def container() -> punq.Container:
    container = create_container()
    return container
