import pytest
from django.test import RequestFactory

from account.models import Profile

# from account.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> Profile:
    # return UserFactory()
    pass


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
