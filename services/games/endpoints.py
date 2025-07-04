from config.links import Links


class Endpoints:
    get_all_games = lambda self, offset, limit: f"{Links.HOST}/games?offset={offset}&limit={limit}"
    get_game_by_id = lambda self, uuid: f"{Links.HOST}/games/{uuid}"

    def search_games_by_name(self, query, offset, limit):
        return f"{Links.HOST}/games/search?query={query}&offset={offset}&limit={limit}" \
            if query \
            else f"{Links.HOST}/games/search?offset={offset}&limit={limit}"
