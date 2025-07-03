from config.links import Links


class Endpoints:
    get_all_games_with_filtering = lambda self, offset, limit: f"{Links.HOST}/games?offset={offset}&limit={limit}"
