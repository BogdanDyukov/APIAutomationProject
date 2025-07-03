import pytest

from services.games.api_games import GamesAPI


@pytest.fixture(scope="class", autouse=True)
def init_api_games(request):
    request.cls.api_games = GamesAPI()
