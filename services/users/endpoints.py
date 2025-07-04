from config.links import Links


class Endpoints:
    create_user = f"{Links.HOST}/users"
    get_user_by_id = lambda self, uuid: f"{Links.HOST}/users/{uuid}"
    get_all_users = lambda self, offset, limit: f"{Links.HOST}/users?offset={offset}&limit={limit}"
