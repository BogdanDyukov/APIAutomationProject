import allure
import pytest

from config.base_test import BaseTest


@pytest.mark.users
@allure.epic("Управление пользователями")
class TestUsers(BaseTest):

    @allure.title("Создание нового пользователя с проверкой")
    def test_create_user(self):
        with allure.step("Создание нового пользователя"):
            user = self.api_users.create_user()

        with allure.step("Получение пользователя по id"):
            self.api_users.get_user_by_id(user.uuid)

@pytest.mark.simple
def test_simple():
    assert True
