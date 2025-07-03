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
    def get_all_games_with_filtering(self, offset, limit):
        response = requests.get(
            url=self.endpoints.get_all_games_with_filtering(offset, limit),
            headers=self.headers.basic
        )
        self.attach_response(response.json())
        return response

