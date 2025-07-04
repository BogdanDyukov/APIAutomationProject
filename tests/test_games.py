import allure
import pytest

from services.games.api_games import GamesAPI
from services.games.models.all_games_response import AllGamesResponse
from services.games.models.game_response import GameResponse


@pytest.fixture(scope="class", autouse=True)
def init_api_games(request):
    request.cls.api_games = GamesAPI()


@pytest.mark.games
@allure.epic("Управление играми")
class TestGames:
    api_games: GamesAPI

    @allure.feature("Получение списка игр")
    @allure.title("Корректное получение всех игр")
    def test_get_all_games(self):
        response = self.api_games.get_all_games(0, 20)
        assert response.status_code == 200, response.json()
        AllGamesResponse(**response.json())

    @allure.feature("Поиск игр по имени")
    @allure.title("Корректный поиск игр ({case_name})")
    @pytest.mark.parametrize("query, case_name", [
        ("", "имя не передается"),
        ("Elden Ring", "имя существующей игры"),
        ("123##", "имя несуществующей игры"),
    ], ids=["empty_name", "real_name", "unreal_name"])
    def test_search_games_by_name(self, query, case_name):
        response = self.api_games.search_games_by_name(query, 0, 20)
        assert response.status_code == 200, response.json()
        AllGamesResponse(**response.json())

    @allure.feature("Получение игры по id")
    @allure.title("Получение существующей игры по id")
    def test_get_game_by_id(self):
        response = self.api_games.get_all_games(0, 1)
        assert response.status_code == 200, response.json()
        games = AllGamesResponse(**response.json())
        assert len(games.games) > 0, "There are no games in the system"

        response = self.api_games.get_game_by_id(games.games[0].uuid)
        assert response.status_code == 200, response.json()
        GameResponse(**response.json())
