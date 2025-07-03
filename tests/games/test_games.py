import allure
import pytest

from services.games.models.all_games_response import AllGamesResponse


@pytest.mark.games
@allure.epic("Управление играми")
class TestGames:

    @allure.feature("Получение списка игр")
    @allure.title("Корректное получение всех игр")
    def test_get_all_games(self):
        response = self.api_games.get_all_games_with_filtering(0, 20)
        assert response.status_code == 200, response.json()
        AllGamesResponse(**response.json())

