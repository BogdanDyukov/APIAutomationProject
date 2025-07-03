import allure
import requests

from config.headers import Headers
from services.users.endpoints import Endpoints
from utils.helper import Helper


class UsersAPI(Helper):

    def __init__(self):
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Создание пользователя")
    def create_user(self, user_payload):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=user_payload
        )
        self.attach_response(response.json())
        return response

    @allure.step("Получение пользователя по id")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        self.attach_response(response.json())
        return response

    @allure.step("Получение всех доступных пользователей с фильтрацией")
    def get_all_users_with_filtering(self, offset, limit):
        response = requests.get(
            url=self.endpoints.get_users_with_filtering(offset, limit),
            headers=self.headers.basic
        )
        self.attach_response(response.json())
        return response
