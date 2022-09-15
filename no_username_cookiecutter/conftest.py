import pytest

from no_username_cookiecutter.users.models import CustomUser
from no_username_cookiecutter.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> CustomUser:
    return UserFactory()
