import allure
import requests

from config.headers import Headers
from services.games.endpoints import Endpoints
from utils.helper import Helper


class GamesAPI(Helper):

    def __init__(self):
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Получение всех доступных игр с фильтрацией")
    def get_all_games(self, offset, limit):
        response = requests.get(
            url=self.endpoints.get_all_games(offset, limit),
            headers=self.headers.basic
        )
        self.attach_response(response.json())
        return response

    @allure.step("Поиск игр по имени с фильтрацией")
    def search_games_by_name(self, query, offset, limit):
        response = requests.get(
            url=self.endpoints.search_games_by_name(query, offset, limit),
            headers=self.headers.basic
        )
        self.attach_response(response.json())
        return response

    @allure.step("Получение игры по id")
    def get_game_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_game_by_id(uuid),
            headers=self.headers.basic
        )
        self.attach_response(response.json())
        return response
