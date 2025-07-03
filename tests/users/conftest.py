import pytest

from services.users.api_users import UsersAPI


@pytest.fixture(scope="class", autouse=True)
def init_api_users(request):
    request.cls.api_users = UsersAPI()
