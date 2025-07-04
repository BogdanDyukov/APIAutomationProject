import os

import pytest
import requests
from dotenv import load_dotenv

from config.links import Links

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def init_environment():
    print("hello")
    response = requests.post(
        url=f"{Links.HOST}/setup",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 205
