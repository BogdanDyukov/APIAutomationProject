import os

import pytest
import requests
from dotenv import load_dotenv


load_dotenv()

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" else "https://release-gs.qa-playground.com/api/v1"


@pytest.fixture(scope="session", autouse=True)
def init_environment():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 205