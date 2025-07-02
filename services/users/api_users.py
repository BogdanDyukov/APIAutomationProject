import requests

from config.headers import Headers
from services.users.endpoints import Endpoints
from services.users.models.user_model import UserModel
from services.users.payloads import Payloads
from utils.helper import Helper


class UsersAPI(Helper):

    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return UserModel(**response.json())

    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return UserModel(**response.json())
