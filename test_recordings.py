import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from pathlib import Path
from .main import app  # или ваш основной файл приложения

client = TestClient(app)

def test_get_recording_success():
    with patch('your_module.user_has_access', return_value=True):
        with patch('pathlib.Path.exists', return_value=True):
            response = client.get("/recordings/test123")
            assert response.status_code == 200
            assert response.headers["content-type"] == "video/mp4"

def test_get_recording_access_denied():
    with patch('your_module.user_has_access', return_value=False):
        response = client.get("/recordings/test123")
        assert response.status_code == 403

def test_get_recording_not_found():
    with patch('your_module.user_has_access', return_value=True):
        with patch('pathlib.Path.exists', return_value=False):
            response = client.get("/recordings/test123")
            assert response.status_code == 404
