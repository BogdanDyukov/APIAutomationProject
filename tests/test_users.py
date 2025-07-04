import allure
import pytest

from services.users.api_users import UsersAPI
from services.users.models.all_users_response import AllUsersResponse
from services.common.models.error_response import ErrorResponse
from services.users.models.user_response import UserResponse
from services.users.payloads import Payloads


@pytest.fixture(scope="class", autouse=True)
def init_api_users(request):
    request.cls.api_users = UsersAPI()


@pytest.mark.users
@allure.epic("Управление пользователями")
class TestUsers:
    api_users: UsersAPI

    @allure.feature("Создание пользователя")
    @allure.title("Корректное создание пользователя с проверкой")
    def test_create_valid_user(self):
        response = self.api_users.create_user(Payloads.valid_user)
        assert response.status_code == 200, response.json()
        user = UserResponse(**response.json())

        response = self.api_users.get_user_by_id(user.uuid)
        assert response.status_code == 200, response.json()
        UserResponse(**response.json())

    @allure.feature("Создание пользователя")
    @allure.title("Некорректное создание пользователя ({case_name})")
    @pytest.mark.parametrize("user_payload, case_name", [
        (Payloads.user_without_nickname, "не передается никнейм"),
        (Payloads.user_without_name, "не передается имя"),
        (Payloads.user_without_password, "не передается пароль"),
        (Payloads.user_without_email, "не передается почта")
    ], ids=["missing_nickname", "missing_name", "missing_password", "missing_email"])
    def test_create_invalid_user(self, user_payload, case_name):
        response = self.api_users.create_user(user_payload)
        assert response.status_code == 400, response.json()
        ErrorResponse(**response.json())

    @allure.feature("Получение списка пользователей")
    @allure.title("Корректное получение всех пользователей")
    def test_get_all_users(self):
        response = self.api_users.get_all_users(0, 20)
        assert response.status_code == 200, response.json()
        AllUsersResponse(**response.json())
