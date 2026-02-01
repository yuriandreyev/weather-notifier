import punq
import pytest


@pytest.fixture()
def container() -> punq.Container:
    return punq.Container()
