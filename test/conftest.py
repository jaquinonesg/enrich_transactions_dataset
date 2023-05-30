##Just for windows
import os
import sys

sys.path.append(os.getcwd())

import pytest
from app.main import app
from fastapi.testclient import TestClient
from httpx import AsyncClient


BASE_URL = "http://localhost"


@pytest.fixture
def client():
    yield TestClient(app)


@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        yield client
