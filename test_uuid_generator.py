# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_generate_uuid():
    response = client.get("/api/v1/uuid/")
    assert response.status_code == 200
